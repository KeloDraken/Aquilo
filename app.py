from aquilo import Aquilo, div, h1, h2, p, StyleSheet
from aquilo.html.generators import build_html
from aquilo.http import urlpatterns

app = Aquilo(description="Made with python")


@app.route()
def home():
    styles = StyleSheet.create({})
    text_styles = StyleSheet.create({})

    root = div(
        styles,
        h1(text_styles, "Hello"),
        h2(text_styles, "This was written in python"),
        p(text_styles, "because why not!!!"),
    )()

    return build_html("Hi", root)


@app.route()
def about():
    styles = StyleSheet.create({})
    text_styles = StyleSheet.create({})

    root = div(
        styles,
        h1(text_styles, "this is the about page")
    )()

    return build_html("about", root)


urlpatterns([
    (r'^$', home),
    (r'about/?$', about),
])

if __name__ == "__main__":
    app.run()
