from aquilo import Aquilo
from aquilo.browser.elements.typography import h1, h2, p

app = Aquilo("KeloDraken", "The web framework for pythoneers")


@app.route("/")
def hello():
    elements = [
        h1("Welcome to Aquilo"),
        h2("The web framework for pythoneers"),
        p("This was generated using python")
    ]
    app.register(elements)


if __name__ == "__main__":
    app.run()
