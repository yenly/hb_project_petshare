from model import User, Seeker, Owner, Pet, Pet_Photo, Connection, Connect_Messages
from model import connect_to_db, db

from server import app
from datetime import datetime
import csv


def load_users_csv():
    """Load users in from csv file."""

    print "Loading users from csv file..."

    User.query.delete()

    with open('seed_data/users.csv') as user_csvfile:
        readUsers = csv.reader(user_csvfile, delimiter=',')
        for row in readUsers:
            last_name = row[0]
            first_name = row[1]
            email = row[2]
            password = hash(row[3])
            phone_number = row[4]
            birthdate = row[5]
            occupation = row[6]
            address = row[7]
            city = row[8]
            state = row[9]
            zipcode = row[10]
            image_url = row[11]

            user = User(last_name=last_name,
                        first_name=first_name,
                        email=email,
                        password=password,
                        phone_number=phone_number,
                        birthdate=birthdate,
                        occupation=occupation,
                        address=address,
                        city=city,
                        state=state,
                        zipcode=zipcode,
                        image_url=image_url)

            db.session.add(user)

    db.session.commit()


def load_owners():
    """Load pet owners into database."""

    print "Loading owners..."

    Owner.query.delete()

    owners = [1, 2, 3, 4, 5, 6, 7, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

    # add user_ids from owners list to db table
    for user in owners:
        user_id = user
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


def load_pets_csv():
    """Load pets into database from csv file."""

    print "Loading pets..."

    Pet.query.delete()

    with open('seed_data/pets.csv') as pet_csvfile:
        readPets = csv.reader(pet_csvfile, delimiter=',')
        for row in readPets:
            name = row[0]
            age = row[1]
            gender = row[2]
            size = row[3]
            color = row[4]
            breed = row[5]
            animal_type = row[6]
            owner_id = row[7]
            is_available = row[8]
            character_details = row[9]
            health_details = row[10]
            image_url = row[11]

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
                      image_url=image_url)

            db.session.add(pet)

    db.session.commit()


def load_connections():
    """Load sample connection."""

    print "Loading connections..."

    Connection.query.delete()

    connect = Connection(pet_id=1,
                         owner_id=1,
                         seeker_id=4,
                         connection_status='Interested')

    connect2 = Connection(pet_id=1,
                          owner_id=1,
                          seeker_id=2,
                          connection_status='Interested')

    db.session.add(connect)
    db.session.add(connect2)

    db.session.commit()


def load_messages():
    """Load messages for connections."""

    print "Loading sample message..."

    Connect_Messages.query.delete()

    message = Connect_Messages(request_id=1,
                               user_id=9,
                               message='Your dog sounds badass!')

    db.session.add(message)
    db.session.commit()


def load_pet_photos_csv():
    """Load photos from csv file."""

    print "Loading pet photos..."

    Pet_Photo.query.delete()

    with open('seed_data/pet_photos.csv') as pet_photo_csvfile:
        readPhotos = csv.reader(pet_photo_csvfile, delimiter=',')
        for row in readPhotos:
            pet_id = row[0]
            image_url = row[1]
            caption = row[2]

            pet_photo = Pet_Photo(pet_id=pet_id,
                                  image_url=image_url,
                                  caption=caption)

            db.session.add(pet_photo)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()
    load_users_csv()
    load_owners()
    load_seekers()
    load_pets_csv()
    load_connections()
    load_messages()
    load_pet_photos_csv()
