from aquilo import Aquilo, h1, a, build
from aquilo.ui import Column, Container, Row

app = Aquilo(debug=True)


@app.page()
def home():
    root = Row(
        [
            Column(h1("This is the home page")),
            Column(
                [
                    a(text="go to about page", href="/about/"),
                    a(text="go to contact page", href="/contact/"),
                ],
            ),
        ]
    )()

    return build(root, title="This is the page title")


@app.page()
def about():
    root = Container(h1(text="this is the about page"))()
    return build(root, title="This is the about page")


@app.page()
def contact():
    root = Container(a("home", "/home/"))()
    return build(root, title="Contact Us")


if __name__ == "__main__":
    app.run()
