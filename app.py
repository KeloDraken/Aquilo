from aquilo import Aquilo, div, h1, h2, p, StyleSheet

app = Aquilo(title="Hello, world", description="Made with python")


@app.route("/")
def home():
    styles = StyleSheet.create({})
    text_styles = StyleSheet.create({})

    root = div(
        styles,
        h1(text_styles, "Hello"),
        h2(text_styles, "This was written in python"),
        p(text_styles, "because why not!!!"),
    )
    app.register_root(root)


if __name__ == "__main__":
    app.run()
