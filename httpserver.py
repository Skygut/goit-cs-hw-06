from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

PORT = 3000


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        if pr_url.path == "/":
            self.send_html_file("index.html")
        elif pr_url.path == "/contact":
            self.send_html_file("contact.html")
        else:
            self.send_html_file("error.html", 404)

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(filename, "rb") as fd:
            self.wfile.write(fd.read())


def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ("", PORT)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


# def send_html_file(self, filename, status=200):
#     self.send_response(status)
#     self.send_header("Content-type", "text/html")
#     self.end_headers()
#     with open(filename, "rb") as fd:
#         self.wfile.write(fd.read())


# if pr_url.path == "/":
#     self.send_html_file("index.html")
# elif pr_url.path == "/contact":
#     self.send_html_file("contact.html")
# else:
#     self.send_html_file("error.html", 404)


# def send_static(self):
#     self.send_response(200)
#     mt = mimetypes.guess_type(self.path)
#     if mt:
#         self.send_header("Content-type", mt[0])
#     else:
#         self.send_header("Content-type", "text/plain")
#     self.end_headers()
#     with open(f".{self.path}", "rb") as file:
#         self.wfile.write(file.read())


# <form action="/contact" method="POST" enctype="application/x-www-form-urlencoded" accept-charset="UTF-8">
#     <h1 class="h3 mb-3 font-weight-normal">Write to me</h1>
#     <div class="row mb-3">
#         <label class=""> Your name </label>
#         <input class="form-control" name="username" type="text"/>
#     </div>
#     <div class="row mb-3">
#         <label class=""> Email address </label>
#         <input class="form-control" name="email" type="email"/>
#     </div>
#     <div class="row mb-3">
#         <label class=""> Your text message </label>
#         <textarea class="form-control" name="message"></textarea>
#     </div>
#     <div class="d-flex justify-content-evenly">
#         <button class="btn btn-primary col-4" name="" type="submit">
#             Send
#         </button>
#         <button class="btn btn-secondary col-4" name="" type="reset">
#             Reset
#         </button>
#     </div>
# </form>


def do_POST(self):
    data = self.rfile.read(int(self.headers["Content-Length"]))
    print(data)
    data_parse = urllib.parse.unquote_plus(data.decode())
    print(data_parse)
    data_dict = {
        key: value for key, value in [el.split("=") for el in data_parse.split("&")]
    }
    print(data_dict)
    self.send_response(302)
    self.send_header("Location", "/")
    self.end_headers()


if __name__ == "__main__":
    run()
