import os
from pathlib import Path
from typing import Any

from aquilo.browser.elements.containers import div
from aquilo.server.server import serve

HTML_BUILD_OUTPUT_DIR = str(Path(__file__).resolve().parent)


def build_html(title: str, element_tree: str):
    html: str = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>
    {element_tree}
</body>
</html>
        """

    with open(HTML_BUILD_OUTPUT_DIR + os.sep + "build" + os.sep + "index.html", "w+") as file:
        file.write(html)


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
        self.root = root

    def run(self):
        for page in self.pages:
            self.pages[page]["function"]()

        if self.root is None:
            print("Root element found")
            print("Document needs to have at least one element")
        else:
            self.element_tree: str = self.root()
            build_html(self.title, self.element_tree)
            serve()

    def register_styles(self, class_name: str, styles: list[dict[str, str]]):
        sl = []
        for style in styles:
            for i, style_class in enumerate(style):
                sl.append(f"{style_class}: {style[style_class]};")
            self.styles.append(f".{class_name}" + " {\n" + "\n".join(sl) + "\n}")
