import sqlite3

from aquilo import Aquilo, h1, h2, a, build
from aquilo.ui import Column, Container, Row

app = Aquilo()


def get_posts():
    # Connecting to sqlite
    conn = sqlite3.connect("db.sqlite3")

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Retrieving data
    cursor.execute("""SELECT * from afterlockdown_post""")

    # Fetching 1st row from the table
    result = cursor.fetchall()

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()

    return result


@app.page()
def home():
    results = get_posts()
    items = list()

    for i in results:
        items.append(
            Row(
                [
                    h1(text=i[1]),
                    h2(text=i[4])
                ],
            )
        )

    root = Row(
        [
            Column(
                items
            ),
            Column(
                [
                    a(text="go to about page", href="/about/"),
                    a(text="go to contact page", href="/contact/")
                ],
            ),
        ]
    )()

    return build(root, title="This is the page title")


@app.page()
def about():
    root = Container(h1(text="this is the about page"))()
    return build(root, title="This is the about page")


@app.page()
def contact():
    root = Container(a("home", "/home/"))()
    return build(root, title="Contact Us")


# if __name__ == "__main__":
app.run()
