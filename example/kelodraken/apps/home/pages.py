from src.aquilo import div, h1, build, a


def page_home():
    root = div(
        [
            div(h1("This is the home page")),
            div(
                [
                    a(text="go to about page", href="/about/about"),
                    a(text="go to contact page", href="/contact/contact"),
                ],
            ),
        ]
    )
    return build(root, title="This is the page title")
