"""PetShare - Find your furry BFF!"""

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "NinjaSkillz531"


@app.route('/')
def index():
    """Homepage."""

    return render_template("index.html")


@app.route('/login')
def login():
    """User login."""

    return render_template("member.html")


@app.route('/profile')
def profile():
    """User profile."""

    return render_template("profile.html")


@app.route('/pet_profile')
def pet_profile():
    """Pet profile."""

    return render_template("pet_profile.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")