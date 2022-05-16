from typing import Any
from wsgiref.simple_server import make_server

_URLPATTERNS: list[tuple[str, Any]] = list()


def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found'.encode()]


def urlpatterns(patterns: list[tuple[str, Any]]):
    global _URLPATTERNS
    _URLPATTERNS = patterns


def get_patterns():
    return _URLPATTERNS


def serve(application: Any):
    with make_server("", 8000, application) as server:
        print("Server listening on port http://localhost:8000...")
        try:
            import webbrowser
            webbrowser.open("http://localhost:8000/")
            server.serve_forever()
        except KeyboardInterrupt:
            server.shutdown()
            return
