from typing import Any, Callable

from aquilo.browser.elements.containers import div
from aquilo.html import get_404
from aquilo.http import serve, get_patterns, urlpatterns


class Aquilo:
    def __init__(
        self,
        host: str = None,
        ip: str = "127.0.0.1",
        port: int = 8000,
        debug: bool = True,
    ):
        self.host = host
        self.ip = ip
        self.port = port
        self.element_tree = None
        self._pages: dict[str, Any] = {}
        self.root = None
        self.styles: list[str] = []
        self._patterns = []
        self.debug: bool = debug

    def page(self):
        def wrapper(function: Callable):
            function_name_with_dashes: str = function.__name__.replace("_", "-").lower()
            self._pages[function_name_with_dashes] = {"function": function}
            pattern = ("{}".format(function_name_with_dashes + "/"), function)
            self._patterns.append(pattern)
            return function

        return wrapper

    def register_root(self, root: div):
        if not isinstance(root, div):
            raise TypeError("root must be a div")
        self.root: div = root

    def _application(self, environ, start_response):
        start_response("200 OK", [("Content-Type", "text/html")])

        path: str = environ.get("PATH_INFO", "").lstrip("/")

        if not path.endswith("/"):
            path = path + "/"

        pages = list(self._pages.keys())

        if path == "/" or path == "":
            html = self._pages[pages[0]]["function"]().encode()
            return [html]

        for pattern in get_patterns():
            page = path.replace("/", " ").strip()

            if page in pages:
                html = self._pages[page]["function"]().encode()
                return [html]

        return [get_404()]

    def run(self):
        urlpatterns(self._patterns)
        serve(self.host, self.ip, self.port, self._application, self.debug)

    def register_styles(self, class_name: str, styles: list[dict[str, str]]):
        sl = []
        for style in styles:
            for i, style_class in enumerate(style):
                sl.append(f"{style_class}: {style[style_class]};")
            self.styles.append(f".{class_name}" + " {\n" + "\n".join(sl) + "\n}")

    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        return self._application(*args)
