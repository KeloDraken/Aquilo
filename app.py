from aquilo import Aquilo
from aquilo.browser.elements.typography import h1, h2, p

app = Aquilo("KeloDraken", "The web framework for pythoneers")


@app.route("/")
def hello():
    h1_styles = {"color": "pink"}
    ht = {"font-size": "100px"}

    elements = [
        h1("Welcome to Aquilo, by Samkelo Drakenberg", ["h1_styles", "ht"]),
        h2("The web framework for pythoneers"),
        p("This was generated using python")
    ]
    app.register_elements(elements)
    app.register_styles("h1_styles", [h1_styles, ht])


if __name__ == "__main__":
    app.run()
