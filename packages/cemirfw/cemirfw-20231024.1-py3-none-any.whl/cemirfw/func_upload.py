import os
import uuid

import tornado

from func_dbs import db_query, db_insert


async def generate_short_url():
    return str(uuid.uuid4())[:6]


async def add_shortened_link(original_url, short_url):
    await db_insert("INSERT INTO shortened_links (original_url, short_url) VALUES (%s, %s)", (original_url, short_url))


async def get_original_url(short_url):
    status, response_data = await db_query("SELECT original_url FROM shortened_links WHERE short_url = %s", short_url, False, 1, "a")

    return response_data[0] if status else None


async def add_or_increment_uploaded_file(short_url):
    # Belirli bir short_url ile bir kaydı eklemeye çalış.
    # Eğer kayıt zaten varsa, download_count değerini artır.
    status, response_data = await db_query("INSERT INTO downloaded_files (short_url) VALUES (%s) ON CONFLICT (short_url) DO UPDATE SET download_count = downloaded_files.download_count + 1 RETURNING id;", short_url, False, 1, "a")

    if not status:
        # Kayıt eklenmedi, download_count artırıldı
        status, response_data = await db_query("SELECT id FROM downloaded_files WHERE short_url = %s", short_url, False, 1, "a")

    return response_data[0] if status else None


async def log_download(short_url, ip_address):
    await db_insert("INSERT INTO download_logs (short_url, ip_address) VALUES (%s, %s)", (short_url, ip_address))


# WebSocket bağlantılarını takip etmek için bir liste
upload__websocket_connections = []


class BaseHandler(tornado.web.RequestHandler):

    def set_default_headers(self):

        self.set_header("server", "CemirFW")
        self.set_header("x-powered-by", "CemirFW v.2023.09.29")

    def write_error(self, status_code, **kwargs):
        with open(f"errors/{status_code}.html", "r") as file:
            html_content = file.read()
        self.set_status(status_code)
        self.set_header("Content-Type", "text/html; charset=utf-8")
        self.finish(html_content)

class UploadHandler(BaseHandler):

    def get(self):
        self.render("templates/upload.html")

    async def post(self):
        uploaded_files = []
        total_size = 0
        for field_name, files in self.request.files.items():
            for file_info in files:
                get_short_url = await generate_short_url()

                file_path = os.path.join("uploads", f"{get_short_url}_{file_info.filename}")
                with open(file_path, "wb") as file:
                    file.write(file_info.body)


                await add_shortened_link(file_info.filename, get_short_url)
                uploaded_files.append({"name": file_info.filename, "new_link": get_short_url})
                total_size += os.path.getsize(file_path)
                self.send_progress(total_size)
        self.write({"files": uploaded_files})
        self.send_complete(uploaded_files)

    def send_progress(self, total_size):
        progress = int((total_size / int(self.request.headers.get('Content-Length'))) * 100)
        for conn in upload__websocket_connections:
            conn.write_message({"progress": progress})

    def send_complete(self, uploaded_files):
        for conn in upload__websocket_connections:
            conn.write_message({"message": "complete", "progress": 100, "files": uploaded_files})


class DownloadHandler(BaseHandler):

    def get(self, filename):
        try:
            file_path = os.path.join("uploads", filename)

            self.set_header('Content-Disposition', f'attachment; filename="{filename}"')
            with open(file_path, 'rb') as file:
                self.write(file.read())
        except FileNotFoundError:
            self.set_status(404)
            self.write({"message": "not_found"})


class UploadWebSocketHandler(tornado.websocket.WebSocketHandler):

    def set_default_headers(self):
        self.set_header("server", "CemirWS")
        self.set_header("x-powered-by", "CemirFW-WS v.2023.09.29")

    def open(self):
        # Yeni bir WebSocket bağlantısı açıldığında, bağlantıyı listeye ekleyin
        upload__websocket_connections.append(self)

    def on_close(self):
        # WebSocket bağlantısı kapandığında, bağlantıyı listeden kaldırın
        upload__websocket_connections.remove(self)


class GetOriginalLinkHandler(BaseHandler):

    async def get(self, short_url):
        original_url = await get_original_url(short_url)
        if original_url:
            print(original_url)
            await add_or_increment_uploaded_file(short_url)
            await log_download(short_url, self.request.remote_ip)
            self.redirect(f"/download/{short_url}_{original_url}")
        else:
            self.set_status(404)
            self.write({"message": "Kısaltılmış link bulunamadı."})
