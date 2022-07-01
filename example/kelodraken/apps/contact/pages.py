from src.aquilo import div, build, a


def page_contact():
    root = div(a("home", "/home/"))
    return build(root, title="Contact Us")
