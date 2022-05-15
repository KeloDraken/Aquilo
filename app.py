from aquilo import Aquilo, div, h1, h2, p, StyleSheet

app = Aquilo(title="Hello, world", description="Made with python")


@app.route("/")
def home():
    styles = StyleSheet.create({})

    root = div(
        styles,
        h1("Hello"),
        h2("This was written in python"),
        p("because why not!!!"),
    )
    app.register_root(root)


if __name__ == "__main__":
    app.run()
