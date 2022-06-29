from aquilo import Aquilo, h1, a, build, div

app = Aquilo(debug=True)


@app.page()
def home():
    root = div(
        [
            div(h1("This is the home page")),
            div(
                [
                    a(text="go to about page", href="/about/"),
                    a(text="go to contact page", href="/contact/"),
                ],
            ),
        ]
    )
    return build(root, title="This is the page title")


@app.page()
def about():
    root = div(h1(text="this is the about page"))
    return build(root, title="This is the about page")


@app.page()
def contact():
    root = div(a("home", "/home/"))
    return build(root, title="Contact Us")


if __name__ == "__main__":
    app.run()
