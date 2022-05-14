import os
from pathlib import Path
from typing import Any

from aquilo.browser.elements import Element
from aquilo.server import server

HTML_BUILD_OUTPUT_DIR = str(Path(__file__).resolve().parent)


def build_html(title: str, tags: list[str]):
    body: str = "\n\t".join(tags)
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
    {body}
</body>
</html>
        """

    with open(HTML_BUILD_OUTPUT_DIR + os.sep + "build" + os.sep + "index.html", "w+") as file:
        file.write(html)


class Aquilo:
    def __init__(self, title: str, description: str):
        self.title: str = title
        self.description: str = description
        self.pages: dict[str, Any] = {}
        self.elements: list[Element] = []

    def route(self, path: str):
        def wrapper(function):
            function_name_with_dashes = function.__name__.replace("_", "-").lower()
            self.pages[function_name_with_dashes] = {"path": path, "function": function}
            return function

        return wrapper

    def register(self, element: list[Element]):
        self.elements = element

    def run(self):
        for i in self.pages:
            self.pages[i]["function"]()

        tags: list[str] = []

        for element in self.elements:
            tag = element()
            tags.append(tag)

        build_html(self.title, tags)
        server.serve()
