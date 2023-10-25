import aioredis

from options import redis_url


async def get_redis_connection():
    return await aioredis.from_url(redis_url)


async def get_ttl(key):
    redis_conn = await get_redis_connection()
    ttl = await redis_conn.ttl(key)
    return ttl


async def redis_clear_cache(keys):
    try:
        redis_conn = await get_redis_connection()
        await redis_conn.delete(*keys)
    except Exception as e:
        print({"error": str(e)})
