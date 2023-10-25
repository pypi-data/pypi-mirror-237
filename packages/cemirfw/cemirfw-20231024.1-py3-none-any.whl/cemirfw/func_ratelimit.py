import subprocess
import time
from datetime import timedelta, datetime
from functools import wraps

import aioredis
import ujson

from func_dbs import db_insert
from options import redis_url, _port, whitelist_ratelimit


async def get_redis_connection():
    return await aioredis.from_url(redis_url)


def rate_limit(limit, period, period_max, block_time):
    def decorator(func):
        @wraps(func)
        async def wrapper(request, *args, **kwargs):

            if request.method == "POST":
                data = ujson.decode(request.body)
                response = await func(request, data)
            else:
                response = await func(request)

            redis_client = await get_redis_connection()

            # İstemcinin IP adresini al
            ip_address = request.remote_ip

            # Redis üzerinde bir anahtar oluştur
            key = f'ratelimit:{ip_address}:{request.uri}'

            # Redis'ten mevcut istek sayısını al
            current_count = await redis_client.get(key)

            # Eğer anahtar daha önce oluşturulmamışsa, sıfırdan başla
            if current_count is None:
                current_count = 0
            else:
                current_count = int(current_count)

            # Şu anki zamanı al
            now = int(time.time())

            # Anahtarın son kullanılma zamanını al (eğer varsa)
            last_used = await redis_client.get(f'last_used:{key}')

            # Eğer anahtar ilk defa kullanılıyorsa veya son kullanılma zamanından belirlenen süre geçtiyse, sayacı sıfırla
            if last_used is None or now - int(last_used) >= period:
                current_count = 0

            # İstek sayısını artır
            current_count += 1

            # Eğer limit aşıldıysa, bir hata mesajı dön
            if current_count > limit:
                await redis_client.set(key, current_count)

                if current_count >= period_max:

                    # Kuralı ekle
                    try:
                        if not ip_address in whitelist_ratelimit:
                            add_rule_command = f"iptables -A INPUT -p tcp --dport {_port} -s {ip_address} -j DROP"
                            subprocess.run(add_rule_command, shell=True, check=True)
                            await db_insert("INSERT INTO blocked_ips (ip_address, block_time_start, block_time_end, request_method) VALUES(%s, %s, %s, %s)", (ip_address, datetime.now(), datetime.now() + timedelta(seconds=block_time), request.method))

                    except subprocess.CalledProcessError as e:
                        print("Kural eklenirken bir hata oluştu.")

                    # raise HTTPError(429, 'Rate Limit Exceededddd', reason=f'current_count: {current_count}')

                return {'status': False, 'message': 'rate_limit', 'current_count': current_count, 'whitelist': True if ip_address in whitelist_ratelimit else False}

            # Eğer limit aşılmadıysa, işlemi devam ettir
            await redis_client.set(key, current_count)
            await redis_client.set(f'last_used:{key}', now)

            return response

        return wrapper

    return decorator
