import os
import re
from pathlib import Path
from wsgiref.simple_server import make_server

HTML_BUILD_OUTPUT_DIR = str(Path(__file__).resolve().parent.parent)
HTML_FILE = HTML_BUILD_OUTPUT_DIR + os.sep + "build" + os.sep + "index.html"


#
#
# # def _application(environment, response):
# #     status = "200 OK"
# #     headers = [("Content-Type", "text/html; charset=utf-8")]
# #     response(status, headers)
# #
# #     with open(HTML_FILE, "r") as file:
# #         html = file.readlines()
# #
# #     b = bytes("\n".join(html), 'utf-8')
# #     return [b]
# #
# #
# # def serve():
# #     with make_server("", 8000, _application) as server:
# #         print("Server listening on port http://localhost:8000...")
# #         try:
# #             import webbrowser
# #             webbrowser.open("http://localhost:8000/")
# #             server.serve_forever()
# #         except KeyboardInterrupt:
# #             server.shutdown()
# #             return
# #
# #


def index(environ, response):
    """This function will be mounted on "/" and display a link
    to the hello world page."""
    status = "200 OK"
    headers = [("Content-Type", "text/html; charset=utf-8")]
    response(status, headers)

    return ['''Hello World Application
               This is the Hello World application:

`<a href="/hello">continue </a>`_

'''.encode()]


def hello(environ, start_response):
    """Like the example above, but it uses the name specified in the
URL."""
    # get the name from the url if it was specified there.
    args = environ['app.urls']
    if args:
        subject = args[0]
    else:
        subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['hello there'.encode()]


def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found'.encode()]


def application(environ, start_response):
    """
    The main WSGI application. Dispatch the current request to
    the functions from above and store the regular expression
    captures in the WSGI environment as  `myapp.url_args` so that
    the functions from above can access the url placeholders.

    If nothing matches call the `not_found` function.
    """
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
        match = re.search(regex, path)
        if match is not None:
            environ['app.urls'] = match.groups()
            return callback(environ, start_response)
    return not_found(environ, start_response)


def serve():
    with make_server("", 8000, application) as server:
        print("Server listening on port http://localhost:8000...")
        try:
            import webbrowser
            webbrowser.open("http://localhost:8000/")
            server.serve_forever()
        except KeyboardInterrupt:
            server.shutdown()
            return
