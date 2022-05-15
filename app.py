from aquilo import Aquilo
from aquilo.browser.elements.typography import h1, h2, p

app = Aquilo(title="Hello, world", description="Made with python")


@app.route("/")
def home():
    h1_styles = {
        "font-size": "100px",
        "color": "pink"
    }

    element = [
        h1("Hello, world", ["h1_styles"]),
        h2("made with python"),
        p("because why not")
    ]

    app.register_elements(element)
    app.register_styles("h1_styles", [h1_styles])


if __name__ == "__main__":
    app.run()
