from typing import Any

from aquilo.browser.elements.containers import div
from aquilo.html.generators import build_html, destroy_html
from aquilo.server import serve


class Aquilo:
    def __init__(self, title: str, description: str):
        self.element_tree = None
        self.title: str = title
        self.description: str = description
        self.pages: dict[str, Any] = {}
        self.root: div = None
        self.styles: list[str] = []

    def route(self, path: str):
        def wrapper(function):
            function_name_with_dashes = function.__name__.replace("_", "-").lower()
            self.pages[function_name_with_dashes] = {"path": path, "function": function}
            return function

        return wrapper

    def register_root(self, root: div):
        if not isinstance(root, div):
            raise TypeError("root must be a div")
        self.root = root

    def run(self):
        for page in self.pages:
            self.pages[page]["function"]()

        if self.root is None:
            print("Root element not found")
        else:
            self.element_tree: str = self.root()
            build_html(self.title, self.element_tree)
            serve()
            destroy_html()

    def register_styles(self, class_name: str, styles: list[dict[str, str]]):
        sl = []
        for style in styles:
            for i, style_class in enumerate(style):
                sl.append(f"{style_class}: {style[style_class]};")
            self.styles.append(f".{class_name}" + " {\n" + "\n".join(sl) + "\n}")
