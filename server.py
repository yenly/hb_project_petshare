"""PetShare - Find your furry BFF!"""

from flask import Flask, render_template, request, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Seeker, Owner, Pet, Connection
from model import connect_to_db, db

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

    user = User.query.get(1)

    pet_owner = user.owners

    for owner in pet_owner:
        for pet in owner.pets:
            user_pet = pet
    print user_pet

    return render_template("member.html", user=user, pet=user_pet)


@app.route('/user/<int:id>')
def user_profile(id):
    """Display user profile."""

    user = User.query.get(id)

    return render_template("profile.html", user=user)


@app.route('/pet_profile/<int:id>')
def pet_profile(id):
    """Display pet profile."""

    pet = Pet.query.get(id)

    owner = pet.owner.user
    print owner

    pet_photos = pet.photos

    return render_template("pet_profile.html", pet=pet, owner=owner, pet_photos=pet_photos)


@app.route('/search', methods=['GET'])
def search():
    """Search for pet and return list of pet profiles."""
    search_term = request.args.get("search_term")
    pets = Pet.query.filter(Pet.animal_type == search_term).all()
    print pets

    # return redirect(url_for('/search_results'), pets=pets)
    return render_template("search_results.html", pets=pets)


@app.route('/search_results')
def display_search_results():
    """Display search results."""

    pass


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")