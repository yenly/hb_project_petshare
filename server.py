"""PetShare - Find your furry BFF!"""

from flask import Flask, render_template, request, redirect, flash, session, jsonify
from flask_mail import Mail, Message
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Seeker, Owner, Pet, Connection
from model import connect_to_db, db

import dictalchemy
import os

from twilio.rest import TwilioRestClient

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_DEFAULT_SENDER'] = 'thepetshare@gmail.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# for twilio
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = TwilioRestClient(account_sid, auth_token)

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
    session['user_city'] = user.city

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

    print user_type
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


@app.route('/display_cats')
def display_cats():
    """Query db for all cats in user area and return list of profiles.

    Returns cats profiles in json."""

    # TO DO: change hard code zipcode to take from user session
    user_city = session['user_city']
    print user_city

    cats_dict = find_pets('cat', user_city)
    print cats_dict

    return jsonify(cats_dict)


@app.route('/display_dogs')
def display_dogs():
    """Query db for all dogs in user area and return list of profiles.

    Returns dog profiles in json.
    """

    # TO DO: use zipcode to filter search results, need bigger sample data
    # user_zipcode = session['user_zipcode']
    user_city = session['user_city']
    print user_city

    dog_dict = find_pets('dog', user_city)
    print dog_dict

    return jsonify(dog_dict)


def find_pets(ani_type, location):
    """Query db for pets based on animal type and location.

    Return dictionary of pets.

        >>> find_pets('cat', '94121')
        {'cat1': {'name': u'Hobbes', 'color': u'orange white stripes', 'gender': u'M', 'age': 3, 'breed': u'tabby', 'owner_id': 6, 'character_details': u'Precocious, mischievous, and adventurous. ', 'is_available': True, 'health_details': u'null', 'image_url': u'https://somethingokay.files.wordpress.com/2012/11/hobbes-from-calvin-and-hobbes-7.gif', 'pet_id': 6, 'animal_type': u'cat', 'size': u'14lbs'}}
    """

    search_results = Pet.query.filter(Pet.animal_type == ani_type).all()
    pets_dict = {}

    for counter, pet in enumerate(search_results, 1):
        if pet.owner.user.city == location:
            pet_info = dictalchemy.utils.asdict(pet)
            pet_info['zipcode'] = pet.owner.user.zipcode
            pet_info['city'] = pet.owner.user.city
            pets_dict[ani_type + str(counter)] = pet_info

    return pets_dict


@app.route('/pet_search')
def pet_search():
    """Dynamic search using angularjs."""

    return render_template("search.html")


@app.route('/search_map')
def search_map():
    """Display search results as markers on google map."""

    return render_template("search_map.html")


@app.route('/connect', methods=['POST'])
def send_connection_request():
    """Connect pet seeker to pet owner.

    Stores connection request info in db.
    """

    user_id = session['user_id']

    seeker = Seeker.query.filter(Seeker.user_id == user_id).first()

    seeker_id = seeker.seeker_id

    pet_id = request.form.get("pet_id")
    owner_id = request.form.get("owner_id")
    connect_message = request.form.get("connect_message")

    print pet_id, owner_id, connect_message

    QUERY = """INSERT INTO connections (pet_id, owner_id, seeker_id, connection_status)
               VALUES (:pet_id, :owner_id, :seeker_id, :connection_status)"""
    db.cursor = db.session.execute(QUERY, {'pet_id': pet_id,
                                           'owner_id': owner_id,
                                           'seeker_id': seeker_id,
                                           'connection_status': 'Interested'})
    db.session.commit()

    connection = Connection.query.filter(Connection.pet_id == pet_id).first()
    request_id = connection.request_id
    print connect_message, request_id

    QUERY = """INSERT INTO connect_messages (request_id, user_id, message)
               VALUES (:request_id, :user_id, :message)"""

    db.cursor = db.session.execute(QUERY, {'request_id': request_id,
                                           'user_id': user_id,
                                           'message': connect_message})

    db.session.commit()

    pet = Pet.query.filter(Pet.pet_id == pet_id).first()

    seeker_name = seeker.user.first_name + " " + seeker.user.last_name

    send_email_notification(seeker_name, pet.name, pet.owner.user.email)
    send_txt(pet.name)

    return jsonify({'connect': 'success'})


def send_email_notification(seeker_name, pet_name, owner_email):
    """Send pet owner email notification of connection request by seeker."""

    # hardcode owner_email for demo purposes
    owner_email = "ymmisc@gmail.com"

    msg = Message('Request to Connect', recipients=[owner_email])
    msg.body = "%s would like to connect with your pet, %s! Log in to find out more." % (seeker_name, pet_name)
    mail.send(msg)

    return True


def send_txt(pet_name):
    """Send text notification using Twilio."""

    txt_msg = "PetShare: Connection request for %s received! Log in your account to find out more." % (pet_name)

    message = client.messages.create(body=txt_msg,
                                     to="+14155316383",  # Hardcode for demo
                                     from_="+14156108596")

    return True


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

    app.run(host='0.0.0.0')
