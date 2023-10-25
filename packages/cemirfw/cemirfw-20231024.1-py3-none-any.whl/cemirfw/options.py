ssl_enable = False
_ip = "0.0.0.0"
_port = 8081
dsn = "dbname=cemirtest user=postgres password=dD5Yz6xE5m host=admin.makdos.com port=5435"
ssl_options = {"certfile": "/ssl/ssl.crt", "keyfile": "/ssl/ssl.key"}

fernet_key = 'SPtqBk6hXCXjk_vRBJbrxQvSfG_0Ur2dBvIVJfP8Vok='
token_expire_minutes = 1 * 1  # 1*60 = 1 saat

# Redis bağlantı ayarları
redis_url = "redis://localhost:6379"

app_settings = {"cookie_secret": "blabla", "max_clients": 100, "login_url": "/login"}  # max_clients eşzamanlı bağlantı sayısını ayarla

whitelist_ratelimit = ("127.0.0.1", "192.168.1.246")
