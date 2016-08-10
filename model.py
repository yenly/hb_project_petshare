"""Models and database functions for PetShare project."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User of PetShare website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    birthdate = db.Column(db.DateTime, nullable=False)
    occupation = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zipcode = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        """Provide basic info on user."""

        return "<User user_id=%s last_name=%s first_name=%s email=%s>" % (self.user_id,
                                                                          self.last_name,
                                                                          self.first_name,
                                                                          self.email)


class Pet_Owner(User):
    """Inherits User class. Define user type to be pet owner."""

    __tablename__ = "pet_owners"

    owner_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __repr__(self):
        """Provide help info on pet owner"""

        return "<Owner owner_id=%s user_id=%s>" % (self.owner_id, self.user_id)


class Pet_Seeker(User):
    """Inherits User class. Define user type to be pet seeker."""

    __tablename__ = "pet_seekers"

    seeker_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    household_size = db.Column(db.Integer, nullable=True)
    children = db.Column(db.Integer, nullable=True)
    pet_experience = db.Column(db.String(10), nullable=True)

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
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    size = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    breed = db.Column(db.String(50), nullable=False)
    animal_type = db.Column(db.String(3), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('pet_owners.owner_id'))
    is_available = db.Column(db.Boolean, nullable=False, default=True)
    character_details = db.Column(db.String(300), nullable=False)
    health_details = db.Column(db.String(100), nullable=True)

    owner = db.relationship('Owner', backref='pets')

    def __repr__(self):
        """Provide Pet info."""

        return "<Pet pet_id=%s name=%s animal_type=%s owner_id=%s>" % (self.pet_id,
                                                                       self.name,
                                                                       self.animal_type,
                                                                       self.owner_id)


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


class Connection(db.Model):
    """Keeps track of connection request between pet seeker and owner."""

    __tablename__ = "connections"

    request_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.pet_id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('pet_owners.owner_id'))
    seeker_id = db.Column(db.Integer, db.ForeignKey('pet_seekers.seeker_id'))
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
