from blog import app
from flask import render_template


@app.route("/")
@app.route("/home")
def homepage():
    return render_template("index.html", title="home page")


@app.route("/design")
def design():
    return render_template("design.html", title="Design Page")


@app.route("/health")
def health():
    return render_template("health.html", title="health page")


@app.route("/opinion")
def opinion():
    return render_template("opinion.html", title="Opinion Page")


@app.route("/travel")
def travel():
    return render_template("travel.html", title="Travel Page")


@app.route("/technology")
def tech():
    return render_template("technology.html", title="Tech Page")


# routes for Gossips
@app.route("/travel/day_one")
def first_day():
    return render_template("Gossips/Day_one.html")


@app.route("/travel/world")
def world_post():
    return "This page is unavailable "


@app.route("/travel/design")
def design_post():
    return "This page is unavailable "


# routes for Recent Posts
@app.route("/travel/example")
def example_post():
    return "This page is unavailable "


@app.route("/travel/another")
def another_post():
    return "This page is unavailable "


@app.route("/travel/longer")
def longer_post():
    return "This page is unavailable "


# routes for Archives
@app.route("/jan-2024")
def archive_jan():
    return "January archive page"


@app.route("/feb-2024")
def archive_feb():
    return "february archive page"


@app.route("/mar-2024")
def archive_mar():
    return "march archive page"


@app.route("/april-2024")
def archive_april():
    return "april archive page"


@app.route("/may-2024")
def archive_may():
    return "may archive page"


@app.route("/june-2024")
def archive_june():
    return "June archive page"


@app.route("/july-2024")
def archive_july():
    return "July archive page"


@app.route("/august-2024")
def archive_august():
    return "august archive page"


@app.route("/sept-2024")
def archive_sept():
    return "september archive page"


@app.route("/oct-2024")
def archive_oct():
    return "october archive page"


@app.route("/nov-2024")
def archive_nov():
    return "november archive page"


@app.route("/dec-2024")
def archive_dec():
    return "december archive page"




