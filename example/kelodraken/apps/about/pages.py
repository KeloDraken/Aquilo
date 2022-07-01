from src.aquilo import div, h1, build


def page_about():
    root = div(h1(text="this is the about page"))
    return build(root, title="This is the about page")
