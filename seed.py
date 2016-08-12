from model import User, Seeker, Owner, Pet, Pet_Photo, Connection
from model import connect_to_db, db

from server import app
from datetime import datetime

def load_users():
    """Load users into database """

    print "Loading users..."

    User.query.delete()

    for row in open("seed_data/user.data"):
        row = row.rstrip()
        last_name, first_name, email, password, birthdate, phone, occupation, address, city, state, zipcode, image = row.split("|")

        user = User(last_name=last_name,
                    first_name=first_name,
                    email=email,
                    password=password,
                    birthdate=birthdate,
                    phone_number=phone,
                    occupation=occupation,
                    address=address,
                    city=city,
                    state=state,
                    zipcode=zipcode,
                    image_url=image)
        db.session.add(user)
    db.session.commit()


def load_owners():
    """Load pet owners into database."""

    print "Loading owners..."

    Owner.query.delete()

    # Auto making first 5 users pet owners for testing
    for i in range(6):
        user_id = i + 1
        owner = Owner(user_id=user_id)
        db.session.add(owner)

    db.session.commit()


def load_seekers():
    """Load pet seekers into database."""

    print "Loading seekers..."

    Seeker.query.delete()

    for row in open("seed_data/seeker.data"):
        row = row.rstrip()
        user_id, household_size, children, pet_experience = row.split("|")

        seeker = Seeker(user_id=user_id,
                        household_size=household_size,
                        children=children,
                        pet_experience=pet_experience)
        db.session.add(seeker)

    db.session.commit()


def load_pets():
    """Load pets into database."""

    print "Loading pets..."

    Pet.query.delete()

    for row in open("seed_data/pet.data"):
        row = row.rstrip()
        name, age, gender, size, color, breed, animal_type, owner_id, is_available, character_details, health_details, image = row.split("|")

        pet = Pet(name=name,
                  age=age,
                  gender=gender,
                  size=size,
                  color=color,
                  breed=breed,
                  animal_type=animal_type,
                  owner_id=owner_id,
                  is_available=is_available,
                  character_details=character_details,
                  health_details=health_details,
                  image_url=image)

        db.session.add(pet)

    db.session.commit()


def load_connections():
    """Load sample connection."""

    print "Loading one connection..."

    Connection.query.delete()

    connect = Connection(pet_id=1,
                         owner_id=1,
                         seeker_id=4,
                         connection_status='Interested')

    connect2 = Connection(pet_id=1,
                          owner_id=1,
                          seeker_id=5,
                          connection_status='Interested')

    db.session.add(connect)
    db.session.add(connect2)

    db.session.commit()

def load_pet_photos():
    """Load sample photos for pets to test db."""

    print "Loading pet photos..."

    Pet_Photo.query.delete()

    ghost = Pet_Photo(pet_id=1,
                      image_url='https://howlingforjustice.files.wordpress.com/2012/06/ghost-with-jon-snow-got1.png?w=400',
                      caption='My human BFF and I ready for battle.')

    ghost2 = Pet_Photo(pet_id=1,
                       image_url='https://cdn.cloudpix.co/images/jon-snow/jon-snow-on-the-iron-throne-with-ghost-game-of-thrones-and-ghost-34478429f2e282ab1f7d85393f0d2ede-large-388205.jpg',
                       caption='My human BFF and I on the iron throne.')

    grey_wind = Pet_Photo(pet_id=5,
                          image_url='https://s-media-cache-ak0.pinimg.com/564x/82/33/02/8233028427798cc7bd701c70a6a02317.jpg',
                          caption='When I was a wee pup with my human BFF.')

    hobbes = Pet_Photo(pet_id=6,
                       image_url='http://img0007o.psstatic.com/115008713_calvin-and-hobbes-pajama-dancing-canvas-print-44-ebay.jpg',
                       caption='Dancing with my little buddy.')

    hobbes2 = Pet_Photo(pet_id=6,
                        image_url='http://images4.fanpop.com/image/photos/23700000/Calvin-Hobbes-calvin-and-hobbes-23762777-1280-800.jpg',
                        caption='We got moves!')

    hobbes3 = Pet_Photo(pet_id=6,
                        image_url='http://i.onionstatic.com/avclub/5449/21/16x9/960.jpg',
                        caption='Exploring with my little buddy.')

    db.session.add(ghost)
    db.session.add(ghost2)
    db.session.add(grey_wind)
    db.session.add(hobbes)
    db.session.add(hobbes2)
    db.session.add(hobbes3)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()
    load_users()
    load_owners()
    load_seekers()
    load_pets()
    load_connections()
    load_pet_photos()
