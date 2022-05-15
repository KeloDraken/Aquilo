import os
from pathlib import Path
from wsgiref.simple_server import make_server

HTML_BUILD_OUTPUT_DIR = str(Path(__file__).resolve().parent.parent)
HTML_FILE = HTML_BUILD_OUTPUT_DIR + os.sep + "build" + os.sep + "index.html"


def wsgi_app(environment, response):
    status = "200 OK"
    headers = [("Content-Type", "text/html; charset=utf-8")]
    response(status, headers)

    with open(HTML_FILE, "r") as file:
        html = file.readlines()

    b = bytes("\n".join(html), 'utf-8')
    return [b]


def serve(path: str):
    with make_server("", 8000, wsgi_app) as server:
        print("Server listening on port http://localhost:8000...")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.shutdown()
            return
