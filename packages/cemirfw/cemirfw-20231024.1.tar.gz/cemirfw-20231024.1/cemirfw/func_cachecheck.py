import time

import ujson

from func_builtin_def import mmslugify, extract_cookie_info
from func_cacheredis import get_redis_connection
from func_dbs import db_query
from func_token import serialize_datetime


async def checkit(self, func, auth, redis_cache_params, sql_durations_times, get_ttl):
    if auth:
        token = self.request.headers.get("Authorization", None)

        if not token:
            self.set_status(401)
            self.write({"status": False, "code": 401, "message": "unauthorized"})
            return

        else:
            token = token.split("Bearer ")[1]  # Todo: token tekrar kontrol edilmeli
            status, user_data = await db_query("SELECT token_expiration, staffs_id FROM user_tokens WHERE token = %s order by id desc limit 1;", params=token, fetchall=None, servertiming_number=1, servertiming_desc="gettoken")
            if not status:
                self.set_status(403)
                self.write({"status": False, "code": 403, "message": "token_not_match"})
                return

            self.request.headers["token_expiration"] = user_data[0]
            self.request.headers["staffs_id"] = user_data[1]
            self.request.headers["token"] = token

    start_time = time.time()
    server_timing = ""
    redis_time = 0
    cached_data = None
    request = self.request
    nocache = self.get_query_argument("nocache", default=None)

    if nocache != "yes":

        if redis_cache_params and "expire_time" in redis_cache_params and "key" in redis_cache_params:
            expire_time = redis_cache_params["expire_time"]
            key = redis_cache_params["key"]

            redis_conn = await get_redis_connection()

            # Anahtarın başlangıç değeri
            redis_cache_key = f"rediscache_post:{mmslugify(request.method)}_{mmslugify(request.full_url())}"

            # İP adresi varsa anahtara ekle
            remote_ip = request.headers.get("X-Real-IP") or request.headers.get("X-Forwarded-For") or request.remote_ip
            if "ip" in key and remote_ip:
                redis_cache_key += f"ip:{mmslugify(remote_ip)}"

            # User-Agent varsa anahtara ekle
            if "useragent" in key and request.headers.get("User-Agent"):
                if redis_cache_key != redis_cache_key:
                    redis_cache_key += ","
                redis_cache_key += f"useragent:{mmslugify(request.headers.get('User-Agent'))}"

            if "cookie" in key:
                # key'den "cookie:" ile başlayan parametreleri çıkart
                cookie_keys = [param for param in key.split(",") if param.startswith("cookie:")]
                cookie_data = request.headers.get("Cookie")
                for cookie_key in cookie_keys:
                    cookie_param = cookie_key.split(":")[1]  # Örneğin, "cookie:username" ise, "username" elde eder
                    cookie_value = extract_cookie_info(cookie_data, cookie_param)
                    if cookie_value:
                        if redis_cache_key != redis_cache_key:
                            redis_cache_key += ","
                        redis_cache_key += f"{cookie_key}:{cookie_value}"

            cached_data = await redis_conn.get(redis_cache_key)

            if cached_data:
                print("from_cache")
                # Önbellekte veri varsa, önbellekteki veriyi döndür
                self.set_header("CemirFW-Cache-From", "Yes")
                redis_time = int((time.time() - start_time) * 1000)
                response_data = ujson.loads(cached_data.decode('utf-8'))
            else:
                print("not_from_cache")
                # Önbellekte veri yoksa, işlemi gerçekleştir
                self.set_header("CemirFW-Cache-From", "No")
                if self.request.method in ["POST", "PUT"]:
                    response_data = await func(self.request, ujson.decode(self.request.body))
                else:
                    response_data = await func(self.request)

                # İşlem sonucunu önbelleğe al
                await redis_conn.setex(redis_cache_key, expire_time, ujson.dumps(response_data, default=serialize_datetime))

            get_ttltime = await get_ttl(redis_cache_key)

            self.set_header("CemirFW-Cache-Timing-Remaining", str(get_ttltime))
            await redis_conn.close()


        else:
            response_data = await func(self.request, ujson.decode(self.request.body))

    else:
        response_data = await func(self.request, ujson.decode(self.request.body))

    end_time = time.time()

    server_timing += f"""1_full;desc="FULL";dur={int((end_time - start_time) * 1000)}"""  # Tam işlem süresi

    if cached_data:
        server_timing += f""",2_redis;desc="Cache";dur={redis_time}"""  # Rediste geçen süre
        server_timing += f""",3_app;desc="APP: Without Cache";dur={abs(int((end_time - start_time) * 1000) - redis_time)}"""  # Uygulama süresi (redis süresini çıkararak)
    else:
        server_timing += "," + ",".join([f"""2_db;desc="DB: {i}";dur={k}""" for i, k in sql_durations_times.items()])  # Veritabanı işlem süreleri
        server_timing += f""",3_app;desc="APP: Without DB";dur={abs(int((end_time - start_time) * 1000) - sum(sql_durations_times.values()) - redis_time)}"""  # Uygulama süresi (veritabanı sürelerini çıkararak)

    self.set_header("Server-Timing", server_timing)
    self.write(ujson.dumps(response_data, default=serialize_datetime))
