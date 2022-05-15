from aquilo import Aquilo
from aquilo.browser.elements.containers import div
from aquilo.browser.elements.typography import h1, h2, p

app = Aquilo(title="Hello, world", description="Made with python")


@app.route("/")
def home():
    element = div(
        div(
            div(
                h1("Hello, world"),
                h2("made with python"),
                p("because why not"),
            )
        ),
        div(
            div(
                h1("Hello, world"),
                h2("made with python"),
                p("because why not"),
            )
        )
    )

    app.register_root(element)


if __name__ == "__main__":
    app.run()
