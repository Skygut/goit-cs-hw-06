from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import socket

PORT = 6000


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("index.html", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/message.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("message.html", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/logo.png":
            self.send_response(200)
            self.send_header("Content-type", "image/png")
            self.end_headers()
            with open("logo.png", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/style.css":
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            with open("style.css", "rb") as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404, "File Not Found")

    def do_POST(self):
        if self.path == "/send":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            # Відправка даних на Socket-сервер
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(("localhost", PORT))
                sock.sendall(post_data)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Data sent to socket server")


# Запуск веб-сервера
def run_server():
    server_address = ("", 4000)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Starting server on port 4000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
