import re
from typing import Any, Callable

from aquilo.browser.elements.containers import div
from aquilo.html.generators import destroy_html
from aquilo.http import serve, get_patterns


class Aquilo:
    def __init__(self, description: str):
        self.element_tree = None
        self.description: str = description
        self.page: dict[str, Any] = {}
        self.root = None
        self.styles: list[str] = []

    def route(self):
        def wrapper(function: Callable):
            function_name_with_dashes: str = function.__name__.replace("_", "-").lower()
            self.page[function_name_with_dashes] = {"function": function}
            return function

        return wrapper

    def register_root(self, root: div):
        if not isinstance(root, div):
            raise TypeError("root must be a div")
        self.root: div = root

    def _application(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])

        html: str = "Not found"
        path: str = environ.get('PATH_INFO', '').lstrip('/')

        for regex, callback in get_patterns():
            match = re.search(regex, path)

            if match is not None:
                environ['app.urls'] = match.groups()

                if path == "":
                    home_page = list(self.page.keys())[0]
                    html = self.page[home_page]["function"]()
                else:
                    p = path.replace("/", " ").strip()

                    for i in list(self.page.keys()):
                        if p == i:
                            html = self.page[i]["function"]()
                            break

        return [html.encode()]

    def run(self):
        serve(self._application)
        destroy_html()

    def register_styles(self, class_name: str, styles: list[dict[str, str]]):
        sl = []
        for style in styles:
            for i, style_class in enumerate(style):
                sl.append(f"{style_class}: {style[style_class]};")
            self.styles.append(f".{class_name}" + " {\n" + "\n".join(sl) + "\n}")
