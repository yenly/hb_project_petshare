from model import User, Seeker, Owner, Pet, Connection
from model import connect_to_db, db

from server import app
from datetime import datetime

def load_users():
    """Load users into database """

    print "Loading users..."

    User.query.delete()

    for row in open("seed_data/user.data"):
        row = row.rstrip()
        last_name, first_name, email, password, birthdate, phone, occupation, address, city, state, zipcode = row.split("|")

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
                    zipcode=zipcode)
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
        name, age, gender, size, color, breed, animal_type, owner_id, is_available, character_details, health_details = row.split("|")

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
                  health_details=health_details)

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


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()
    load_users()
    load_owners()
    load_seekers()
    load_pets()
    load_connections()
