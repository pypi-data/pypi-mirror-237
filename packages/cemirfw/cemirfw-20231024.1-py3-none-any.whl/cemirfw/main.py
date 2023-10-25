import importlib
import types
import subprocess
import tornado
from func_handlers import make_app
from options import ssl_enable, ssl_options, _port, _ip

# allowed = ["http://0.0.0.0:8000"]
def check_origin(self, origin):
    if origin in ["http://0.0.0.0:8000"]:
        return 1

if __name__ == "__main__":


    try:

        # region otomatik import
        handlers_module = importlib.import_module("endpoints")
        for item_name in dir(handlers_module):
            item = getattr(handlers_module, item_name)
            if isinstance(item, types.FunctionType):
                globals()[item_name] = item
        # endregion otomatik import

        subprocess.run("clear", shell=True)  ## cls -> Windows
        application = make_app()

        if ssl_enable:
            server = tornado.httpserver.HTTPServer(application, ssl_options=ssl_options)
        else:
            server = tornado.httpserver.HTTPServer(application)

        server.bind(_port, _ip)
        tornado.autoreload.start()

        server.start()
        print(f"Servis başlatıldı!!")
        print(f"http://{_ip}:{_port}")

        tornado.ioloop.IOLoop.current().start()

    except KeyboardInterrupt:
        print("Ctrl+C ile sonlandırıldı.")
