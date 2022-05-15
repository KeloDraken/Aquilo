import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

HTML_BUILD_OUTPUT_DIR = str(Path(__file__).resolve().parent.parent)
HTML_FILE = HTML_BUILD_OUTPUT_DIR + os.sep + "build" + os.sep + "index.html"


def serve():
    print("Server listening on port http://localhost:8080...")
    httpd = HTTPServer(("localhost", 8080), Server)
    httpd.serve_forever()


class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.path = HTML_FILE

        try:
            file_to_open = open(self.path).read()
        except FileNotFoundError:
            pass
        self.send_response(200)
        self.end_headers()

        try:
            self.wfile.write(bytes(file_to_open, "utf-8"))
        except UnboundLocalError:
            pass
