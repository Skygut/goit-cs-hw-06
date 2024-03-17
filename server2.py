from http.server import BaseHTTPRequestHandler, HTTPServer

# Порт, на якому буде запущений веб-сервер
PORT = 4000
# WEB_DIR = "./front-init"  # Шлях до вашої папки з веб-контентом


# Клас, який відповідає за обробку HTTP-запитів
class RequestHandler(BaseHTTPRequestHandler):
    # Функція обробки GET-запитів
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # print((os.path.join(WEB_DIR, self.path[1:])))
            with open("index.html", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/message.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("message.html", "rb") as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404, "File Not Found")


# Запуск веб-сервера на вказаному порті
def run_server():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Starting server on port {PORT}...")
    httpd.serve_forever()


# Запускаємо веб-сервер при запуску файлу
if __name__ == "main":
    run_server()
