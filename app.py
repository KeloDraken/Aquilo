from aquilo import Aquilo, div
from aquilo.browser.elements.typography import h1

app = Aquilo(title="Hello, world", description="Made with python")


@app.route("/")
def home():
    root = div(
        h1("This is made with python")
    )
    app.register_root(root)


if __name__ == "__main__":
    app.run()
