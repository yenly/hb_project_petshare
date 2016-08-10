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
