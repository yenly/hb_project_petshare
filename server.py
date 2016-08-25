"""PetShare - Find your furry BFF!"""

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Seeker, Owner, Pet, Connection
from model import connect_to_db, db

import dictalchemy

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "NinjaSkillz531"


@app.route('/')
def index():
    """Homepage."""

    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    """Handles user login."""

    user_email = request.form.get('email')
    user_password = request.form.get('password')

    user = User.query.filter(User.email == user_email).first()
    session['user_id'] = user.user_id

    # TO DO: build out pasword testing logic

    msg = "Welcome back", user.first_name

    flash(msg)

    return redirect('/member')


@app.route('/member')
def member():
    """Member dashboard."""

    user_id = session['user_id']

    user = User.query.get(user_id)

    user_type = []
    user_pet = ""

    #if user is owner
    if len(user.owner) != 0:
        #add user type as owner on user_type dict
        user_type.append('owner')
        #get owner_id and add to user_type dict
        for owner in user.owner:
            user_type.append(owner.owner_id)
            for pet in owner.pets:
                user_pet = pet
    #else if user is seeker
    elif len(user.seeker) != 0:
        #add user type as seeker on user_type dict
        user_type.append('seeker')
        #get seeker_id and add to user_type dict
        for seeker in user.seeker:
            user_type.append(seeker.seeker_id)

    #call get_connections passing user type
    request_list = get_connections(user_type)

    return render_template("member.html", user=user, pet=user_pet, request_list=request_list)


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

    pet_photos = pet.photos

    return render_template("pet_profile.html", pet=pet, owner=owner, pet_photos=pet_photos)


@app.route('/search')
def search():
    """Search for pet and return list of pet profiles."""
    search_term = request.args.get("search_term")
    print "Search function: ", search_term
    if search_term.isdigit():
        users = User.query.filter(User.zipcode == str(search_term)).all()
        for user in users:
            for owner in user.owner:
                search_results = owner.pets
    else:
        search_results = Pet.query.filter(Pet.animal_type == search_term).all()

    pets_dict = {}

    for counter, value in enumerate(search_results, 1):
        pet_info = dictalchemy.utils.asdict(value)
        pets_dict['results' + str(counter)] = pet_info

    return jsonify(pets_dict)


@app.route('/display_cats')
def display_cats():
    """Query db for all cats in user area and return list of profiles.

    Returns cats profiles in json."""

    search_term = "cat"
    search_results = Pet.query.filter(Pet.animal_type == search_term).all()

    cats_dict = {}

    for counter, value in enumerate(search_results, 1):
        pet_info = dictalchemy.utils.asdict(value)
        cats_dict['results' + str(counter)] = pet_info

    return jsonify(cats_dict)


@app.route('/display_dogs')
def display_dogs():
    """Query db for all dogs in user area and return list of profiles.

    Returns dog profiles in json.
    """

    # TO DO: use zipcode to filter search results

    search_term = "dog"
    search_results = Pet.query.filter(Pet.animal_type == search_term).all()

    dog_dict = {}

    for counter, value in enumerate(search_results, 1):
        pet_info = dictalchemy.utils.asdict(value)
        dog_dict['doggie' + str(counter)] = pet_info

    return jsonify(dog_dict)


@app.route('/pet_search')
def pet_search():
    """Dynamic search using angularjs."""

    return render_template("search.html")


@app.route('/connect', methods=['POST'])
def send_connection_request():
    """Connect pet seeker to pet owner.

    Stores connection request info in db.
    """

    seeker_id = session['user_id']

    seeker = Seeker.query.filter(Seeker.user_id == seeker_id).first()

    seeker_id = seeker.seeker_id

    pet_id = request.form.get("pet_id")
    owner_id = request.form.get("owner_id")

    QUERY = """INSERT INTO connections (pet_id, owner_id, seeker_id, connection_status)
               VALUES (:pet_id, :owner_id, :seeker_id, :connection_status)"""
    db.cursor = db.session.execute(QUERY, {'pet_id': pet_id,
                                           'owner_id': owner_id,
                                           'seeker_id': seeker_id,
                                           'connection_status': 'Interested'})
    db.session.commit()

    flash('Successfully created connection request.')

    return jsonify({'connect': 'success'})


def get_connections(user_info):
    """Returns a list of connection request for a user

        >>> connect_to_db(app)
        >>> get_connections(['owner', 3])
        [<Connection request_id=8 pet_id=4 owner_id=3 seeker_id=1>, <Connection request_id=16 pet_id=4 owner_id=3 seeker_id=6>]

    """

    user_type, _id = user_info

    if user_type == 'owner':
        #query for request with owner_id == _id
        request_list = Connection.query.filter(Connection.owner_id == _id).all()
    elif user_type == 'seeker':
        #query for request with seeker_id == _id
        request_list = Connection.query.filter(Connection.seeker_id == _id).all()

    return request_list


@app.route('/change_connect_status', methods=['POST'])
def change_connect_status():
    """Update status on connection request."""

    connect_status_dict = {}

    for item in request.form:
        request_info = item.split("_")
        connect_status_dict[request_info[-1]] = request.form.get(item)

    for connect_request in connect_status_dict:
        request_id = connect_request
        connection_status = connect_status_dict[connect_request]

        QUERY = """UPDATE connections SET connection_status = :connection_status
                WHERE request_id = :request_id"""

        db.cursor = db.session.execute(QUERY, {'request_id': request_id,
                                               'connection_status': connection_status})
    db.session.commit()

    return "Connections table updated. Woohoo!"


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")