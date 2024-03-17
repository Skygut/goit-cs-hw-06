import http.server
import socketserver
import os

PORT = 3000
# WEB_DIR = "/mnt/data/front-init/front-init"  # Шлях до вашої папки з веб-контентом
WEB_DIR = "./front-init"  # Шлях до вашої папки з веб-контентом


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Встановлення базової директорії для статичних файлів
        self.directory = WEB_DIR
        # Перевірка на існування файлу
        print((os.path.join(WEB_DIR, self.path[1:])))

        if not os.path.exists(os.path.join(WEB_DIR, self.path[1:])):
            self.path = "error.html"

        # Обробка запиту
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


# Налаштування обробника HTTP запитів
handler_object = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    # print("Сервер стартував на порту", PORT)
    httpd.serve_forever()
