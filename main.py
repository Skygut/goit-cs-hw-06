from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from pathlib import Path
import signal
import urllib.parse
import socket
import threading
import logging
from datetime import datetime
from dotenv import load_dotenv
from connect_db import create_connect

from socket_srv import socket_server

server_running = True
WEB_DIR = "./front-init"

logging.basicConfig(
    filename="server.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

ENV_PATH = Path(__file__).parent / ".env"

load_dotenv(ENV_PATH)

PORT = int(os.getenv("PORT"))
PORT2 = int(os.getenv("PORT2"))


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(os.path.join(WEB_DIR, "index.html"), "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/message.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(os.path.join(WEB_DIR, "message.html"), "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/logo.png":
            self.send_response(200)
            self.send_header("Content-type", "image/png")
            self.end_headers()
            with open(os.path.join(WEB_DIR, "logo.png"), "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/style.css":
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            with open(os.path.join(WEB_DIR, "style.css"), "rb") as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(os.path.join(WEB_DIR, "error.html"), "rb") as file:
                self.wfile.write(file.read())

    def do_POST(self):
        if self.path == "/message":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(("localhost", PORT2))
                sock.sendall(data)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Data sent to socket server")


def run_server(port):
    server_address = ("", port)
    httpd = HTTPServer(server_address, RequestHandler)

    try:
        print(f"Starting server on port {port}...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.error("Server stoping...")
        httpd.shutdown()


def stop_servers(signum, frame):
    global server_running
    print("Stopping servers...")
    server_running = False


signal.signal(signal.SIGINT, stop_servers)


if __name__ == "__main__":
    web_thread = threading.Thread(target=run_server, args=(PORT,))
    web_thread.daemon = True
    web_thread.start()

    socket_server(PORT2)