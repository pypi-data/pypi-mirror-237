import os
import uuid

import tornado
import tornado.websocket
from tornado.escape import xhtml_escape, to_unicode

from func_cachecheck import checkit
from func_cacheredis import get_ttl
from func_dbs import sql_durations_times
from func_token import APIHandler
from func_upload import UploadHandler, DownloadHandler, GetOriginalLinkHandler, UploadWebSocketHandler
from options import _ip, _port, app_settings

# application = tornado.web.Application([])
application = tornado.web.Application(**app_settings)


# region methods


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_signed_cookie("logininfos")

    def set_default_headers(self):
        # Tüm kaynaklara izin vermek için CORS başlıkları
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.set_header("server", "Cemir")
        self.set_header("x-powered-by", "CemirFW v.2023.09.29")
        self.set_header("Content-Type", "application/json; charset=utf-8")

    def write_error(self, status_code, **kwargs):
        from tornado import template
        loader = template.Loader("errors")  # Şablonlarınızın bulunduğu dizin
        html_content = loader.load(f"{status_code}.html").generate(reason=self._reason)
        self.set_status(status_code)
        self.set_header("Content-Type", "text/html; charset=utf-8")
        self.finish(html_content)

        # with open(f"errors/{status_code}.html", "r") as file:  #     html_content = file.read()  # self.set_status(status_code)  # self.set_header("Content-Type", "text/html; charset=utf-8")  # self.finish(html_content)


class NotFoundHandler(BaseHandler):

    def prepare(self):
        self.set_status(404)
        self.set_header("Content-Type", "text/html; charset=utf-8")
        with open("errors/404.html", "r") as file:
            html_content = file.read()
        self.finish(html_content)


def cemir_sget(url_pattern, auth=None, redis_cache_params=None):
    def decorator(func):
        class Handler(BaseHandler):
            async def get(self):
                await checkit(self, func, auth, redis_cache_params, sql_durations_times, get_ttl)

        application.add_handlers(r".*", [(url_pattern, Handler)])
        return func

    return decorator


def cemir_spost(url_pattern, auth=False, redis_cache_params=None):
    def decorator(func):
        class Handler(BaseHandler):
            async def post(self):
                await checkit(self, func, auth, redis_cache_params, sql_durations_times, get_ttl)

        application.add_handlers(r".*", [(url_pattern, Handler)])
        return func

    return decorator


def cemir_sput(url_pattern, auth=False, redis_cache_params=None):
    def decorator(func):
        class Handler(BaseHandler):
            async def put(self):
                await checkit(self, func, auth, redis_cache_params, sql_durations_times, get_ttl)

        application.add_handlers(r".*", [(url_pattern, Handler)])
        return func

    return decorator


def secure_params(func):
    async def wrapper(request, *args, **kwargs):
        # Tüm parametreleri al
        secure_args = {}
        for key, values in request.arguments.items():
            # XSS saldırılarına karşı parametreleri temizleme
            secure_values = [xhtml_escape(value.decode("utf-8")) for value in values]
            secure_args[key] = secure_values

        # SQL enjeksiyonuna karşı parametreleri güvenli bir şekilde kullanma
        for key, values in secure_args.items():
            secure_args[key] = [to_unicode(value) for value in values]

        # Güncellenmiş parametreleri fonksiyona iletme
        request.secure_params = secure_args

        # Parametrelere daha kısa bir erişim sağlamak için yeni bir işlev ekle
        request.params = lambda key, default=None: request.secure_params.get(key, [default])[0]

        return await func(request, *args, **kwargs)

    return wrapper


def get(url_pattern, auth=False, redis_cache_params=None):
    def decorator(func):
        # İlk olarak secure_params decorator'ını, sonra cemir_get decorator'ını uygula
        return cemir_sget(url_pattern, auth, redis_cache_params)(secure_params(func))

    return decorator


def post(url_pattern, auth=False, redis_cache_params=None):
    def decorator(func):
        return cemir_spost(url_pattern, auth, redis_cache_params)(secure_params(func))

    return decorator


def put(url_pattern, auth=False, redis_cache_params=None):
    def decorator(func):
        return cemir_sput(url_pattern, auth, redis_cache_params)(secure_params(func))

    return decorator


def check_params(required_params):
    def decorator(func):
        async def wrapper(handler, *args, **kwargs):
            # Tüm gerekli parametreleri kontrol et
            missing_params = [param for param in required_params if param not in handler.arguments]

            if missing_params:
                return {"status": False, "message": f"params ({', '.join(missing_params)}) are missing"}

            # Tüm gerekli parametreler mevcutsa işlemi devam ettir
            return await func(handler, *args, **kwargs)

        return wrapper

    return decorator


def make_app():
    application.add_handlers(r".*", [(r"/apilogin", APIHandler)])
    application.add_handlers(r".*", [(r"/upload", UploadHandler)])
    application.add_handlers(r".*", [(r"/download/(.*)", DownloadHandler)])
    application.add_handlers(r".*", [(r"/uploadws", UploadWebSocketHandler)])
    application.add_handlers(r".*", [(r"/s/(\w+)", GetOriginalLinkHandler)])
    application.add_handlers(r".*", [(r"/static/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "static")})])
    application.add_handlers(r".*", [(r".*", NotFoundHandler)])

    return application


def on_reload():
    print(f"Kod değişikliği algılandı. Yeniden başlatılıyor...")
    print(f"http://{_ip}:{_port}")


tornado.autoreload.add_reload_hook(on_reload)  # endregion methods
