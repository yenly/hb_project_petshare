"""Models and database functions for PetShare project."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User of PetShare website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    last_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))
    phone_number = db.Column(db.String(12))
    birthdate = db.Column(db.DateTime)
    occupation = db.Column(db.String(50))
    address = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.String(15))
    image_url = db.Column(db.String(200))

    def __repr__(self):
        """Provide basic info on user."""

        return "<User user_id=%s last_name=%s first_name=%s email=%s>" % (self.user_id,
                                                                          self.last_name,
                                                                          self.first_name,
                                                                          self.email)


class Owner(db.Model):
    """Inherits User class. Define user type to be pet owner."""

    __tablename__ = "owners"

    owner_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    user = db.relationship('User', backref='owner')

    def __repr__(self):
        """Provide help info on pet owner"""

        return "<Owner owner_id=%s user_id=%s>" % (self.owner_id, self.user_id)


class Seeker(db.Model):
    """Inherits User class. Define user type to be pet seeker."""

    __tablename__ = "seekers"

    seeker_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    household_size = db.Column(db.Integer, nullable=True)
    children = db.Column(db.Integer, nullable=True)
    pet_experience = db.Column(db.String(10), nullable=True)

    user = db.relationship('User', backref='seeker')

    def __repr__(self):
        """Provide help info on pet seeker"""

        return "<Seeker seeker_id=%s user_id=%s>" % (self.seeker_id, self.user_id)


# class User_Social_Media(db.Model):
#     """User's social media links."""

#     __tablename__ = "user_social_medias"

#     sm_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
#     social_media_type = db.Column(db.String(20), nullable=False)
#     url = db.Column(db.String(50), nullable=False)

#     def __repr__(self):
#         """Provide user's social media links"""

#         return "<USM user_id=%s social_media_type=%s url=%s>" % (self.user_id,
#                                                                  self.social_media_type,
#                                                                  self.url)


class Pet(db.Model):
    """Pet for sharing by owner."""

    __tablename__ = "pets"

    pet_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(1))
    size = db.Column(db.String(10))
    color = db.Column(db.String(50))
    breed = db.Column(db.String(50))
    animal_type = db.Column(db.String(3))
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.owner_id'))
    is_available = db.Column(db.Boolean)
    character_details = db.Column(db.String(300))
    health_details = db.Column(db.String(100))
    image_url = db.Column(db.String(200))

    owner = db.relationship('Owner', backref='pets')

    def __repr__(self):
        """Provide Pet info."""

        return "<Pet pet_id=%s name=%s animal_type=%s owner_id=%s>" % (self.pet_id,
                                                                       self.name,
                                                                       self.animal_type,
                                                                       self.owner_id)

    # def __dict__(self):
    #     """Converts class object to dictionary."""

    #     pet_dict = {}

        


# class Pet_Available_Time(db.Model):
#     """When Pets are avaiable for connection."""

#     __tablename__ = "pet_available_times"

#     timeslot_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     pet_id = db.Column(db.Integer, db.ForeignKey('pets.pet_id'))
#     owner_id = db.Column(db.Integer, db.ForeignKey('pet_owners.owner_id'))
#     available_start_at = db.Column(db.DateTime, nullable=False)
#     available_end_at = db.Column(db.DateTime, nullable=False)

#     def __repr__(self):
#         """Provide time available range for pet and owner."""

#         return "<Pet_Available pet_id=%s available_start_at=%s available_end_at=%s>" % (self.pet_id,
#                                                                                         self.available_start_at,
#                                                                                         self.available_end_at)

class Pet_Photo(db.Model):
    """Pet photos for pet profile."""

    __tablename__ = "pet_photos"

    photo_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.pet_id'))
    image_url = db.Column(db.String(200))
    caption = db.Column(db.String(100))

    pet = db.relationship('Pet', backref='photos')

    def __repr__(self):
        """Provide info on photo"""

        return "<Photo pet_id=%s image_url=%s>" % (self.pet_id, self.image_url)


class Connection(db.Model):
    """Keeps track of connection request between pet seeker and owner."""

    __tablename__ = "connections"

    request_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.pet_id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.owner_id'))
    seeker_id = db.Column(db.Integer, db.ForeignKey('seekers.seeker_id'))
    connection_status = db.Column(db.String, nullable=True)

    def __repr__(self):
        """Provide info on connection."""

        return "<Connection request_id=%s pet_id=%s owner_id=%s seeker_id=%s>" % (self.request_id,
                                                                                  self.pet_id,
                                                                                  self.owner_id,
                                                                                  self.seeker_id)


# Helper functions
def connect_to_db(app):
    """Connect to the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petshare'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."
