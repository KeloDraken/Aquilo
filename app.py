from aquilo import Aquilo, div, h1, h2, p, StyleSheet, a
from aquilo.html.generators import build_html
from aquilo.http import urlpatterns

app = Aquilo()


@app.route()
def home():
    styles = StyleSheet.create({})
    text_styles = StyleSheet.create({})

    root = div(
        styles,
        h1(styles=text_styles, text="Hello"),
        h2(styles=text_styles, text="This was written in python"),
        p(styles=text_styles, text="because why not!!!"),
        a(styles=text_styles, text="go to about page", href="/about/")
    )()

    return build_html(root, title="This is the page title")


@app.route()
def about():
    styles = StyleSheet.create({})
    text_styles = StyleSheet.create({})

    root = div(
        styles,
        h1(styles=text_styles, text="this is the about page")
    )()

    return build_html(root, title="This is the about page")


urlpatterns([
    (r'^$', home),
    (r'about/?$', about),
])

if __name__ == "__main__":
    app.run()
