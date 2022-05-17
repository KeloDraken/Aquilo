from aquilo import Aquilo, h1, h2, p, a, build
from aquilo.ui import Column, Container, Row

app = Aquilo()


@app.page()
def home():
    root = Row(
        Column(
            h1(text="Hello"),
            h2(text="This was written in python"),
            p(text="because why not!!!"),
        ),
        Column(
            a(text="go to about page", href="/about/"),
            a(text="go to contact page", href="/contact/"),
        )
    )()

    return build(root, title="This is the page title")


@app.page()
def about():
    root = Container(
        h1(text="this is the about page")
    )()

    return build(root, title="This is the about page")


@app.page()
def contact():
    root = Container(a("home", "/home/"))()
    return build(root, title="Contact Us")


if __name__ == "__main__":
    app.run()
