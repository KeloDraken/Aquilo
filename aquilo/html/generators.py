from aquilo.browser.elements import Element


def get_element_tree(root: tuple[Element]):
    element_tree = ["<div>"]

    for tag in root:
        element_tree.append(tag())
    element_tree.append("</div>")

    return "\n".join(element_tree)
