from datetime import datetime, timedelta

import tornado.web
import ujson as json
from cemir_print.ccprint import ccprint
from cryptography.fernet import Fernet
import aioredis

from func_dbs import db_query, db_insert
from options import token_expire_minutes, fernet_key, redis_url

fernet = Fernet(fernet_key)


async def get_redis_connection():
    return await aioredis.from_url(redis_url)


# datetime.datetime nesnesini JSON uyumlu bir şekilde seri hale getir
def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Object of type datetime is not JSON serializable")


class APIHandler(tornado.web.RequestHandler):
    async def post(self):
        email = self.get_argument("email")
        password = self.get_argument("password")

        status, user_data = await db_query("SELECT id, content->>'email', content->>'password' FROM public.company__staffs WHERE content->>'email' = %s", params=email, fetchall=None, servertiming_number=1, servertiming_desc="None")

        staffs_id = user_data[0]
        password_ = user_data[2]

        if status and password_ == password:  # Parola doğrulaması
            token = await self.get_or_create_token(email, staffs_id)

            try:
                self.write({"token": token})
            except:
                self.write({"token": token.decode('utf-8')})

        else:
            self.set_status(401)
            self.write(json.dumps({"status": 401, "message": "Hatalı kullanıcı adı veya parola"}))

    async def get_or_create_token(self, email_, staffs_id):
        # Redis bağlantısını al
        redis_conn = await get_redis_connection()
        try:
            # Kullanıcının mevcut token bilgisini Redis'ten kontrol et
            redis_key = f"user_token:{staffs_id}"
            token = await redis_conn.get(redis_key)

            expiration_time = datetime.now() + timedelta(minutes=token_expire_minutes)
            token_data = {
                "email": email_,
                "staffs_id": staffs_id,
                "expiration_time": expiration_time
            }

            if token and await self.is_valid_token(token_data):
                return token
            else:
                # Token geçerli değilse veya Redis'te yoksa, veritabanından al veya oluştur
                token = await self.create_new_token(email_, staffs_id)
                # Redis'e yeni token'ı kaydet
                # Token'ı Redis'e kaydet ve süresini ayarla (expire)
                await redis_conn.set(redis_key, token)
                await redis_conn.expire(redis_key, token_expire_minutes)

                return token
        finally:
            # Redis bağlantısını kapat
            await redis_conn.close()

    async def create_new_token(self, email_, staffs_id):
        # Yeni token üret
        expiration_time = datetime.now() + timedelta(minutes=token_expire_minutes)
        token_data = {
            "email": email_,
            "staffs_id": staffs_id,
            "expiration_time": expiration_time
        }
        token = await self.encrypt_token(token_data)

        inserted_id = await db_insert("INSERT INTO user_tokens (staffs_id, token_expiration, token) VALUES (%s, %s, %s)", params=(staffs_id, expiration_time, token))

        return token if inserted_id else False

    async def is_valid_token(self, token_data):
        expiration_time = token_data["expiration_time"]
        return expiration_time > datetime.now()

    async def encrypt_token(self, token_data):
        token = fernet.encrypt(json.dumps(token_data, default=serialize_datetime).encode()).decode("utf-8")
        return token
