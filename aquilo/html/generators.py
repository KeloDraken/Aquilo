import os
from pathlib import Path

from aquilo.browser.elements import Element

HTML_BUILD_OUTPUT_DIR = str(Path(__file__).resolve().parent.parent)


def build_html(title: str, element_tree: str) -> None:
    html: str = f"""
<!DOCTYPE html><html lang="en"><head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head><body>{element_tree}</body></html>
        """

    with open(HTML_BUILD_OUTPUT_DIR + os.sep + "build" + os.sep + "index.html", "w+") as file:
        file.write(html)


def get_element_tree(root: tuple[Element]) -> str:
    element_tree = ["<div>"]

    for tag in root:
        element_tree.append(tag())
    element_tree.append("</div>")

    return "".join(element_tree)


def destroy_html():
    with open(HTML_BUILD_OUTPUT_DIR + os.sep + "build" + os.sep + "index.html", "w+") as file:
        file.write("")
