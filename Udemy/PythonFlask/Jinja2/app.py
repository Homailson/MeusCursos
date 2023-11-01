from flask import Flask, render_template


app = Flask(__name__)


@app.route("/data-structures/")
def render_data_structures():

    movies = [
        "Leon the Professional",
        "The Usual Suspects",
        "A beautiful Mind"
    ]

    return render_template("data_structures.html", movies=movies)
