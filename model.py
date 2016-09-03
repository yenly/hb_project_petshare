"""Models and database functions for PetShare project."""

from flask_sqlalchemy import SQLAlchemy
import dictalchemy

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
    health_details = db.Column(db.String(300))
    image_url = db.Column(db.String(200))

    owner = db.relationship('Owner', backref='pets')

    def __repr__(self):
        """Provide Pet info."""

        return "<Pet pet_id=%s name=%s animal_type=%s owner_id=%s>" % (self.pet_id,
                                                                       self.name,
                                                                       self.animal_type,
                                                                       self.owner_id)


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
    request_at = db.Column(db.DateTime, server_default=db.func.now())
    connection_status = db.Column(db.String, nullable=True)

    pet = db.relationship('Pet', backref='connections')
    owner = db.relationship('Owner', backref='connections')
    seeker = db.relationship('Seeker', backref='connections')

    def __repr__(self):
        """Provide info on connection."""

        return "<Connection request_id=%s pet_id=%s owner_id=%s seeker_id=%s>" % (self.request_id,
                                                                                  self.pet_id,
                                                                                  self.owner_id,
                                                                                  self.seeker_id)


class Connect_Messages(db.Model):
    """Messages between pet seeker and pet owner regarding connection request."""

    __tablename__ = "connect_messages"

    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('connections.request_id'))
    message_at = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    message = db.Column(db.String(400))

    connection = db.relationship('Connection', backref='messages')
    user = db.relationship('User', backref='messages')

    def __repr__(self):
        """Provide info on connection messages."""

        return "<Connect_Msg message_id=%s request_id=%s user_id=%s>" % (self.message_id,
                                                                         self.request_id,
                                                                         self.user_id)


dictalchemy.utils.make_class_dictable(User)
dictalchemy.utils.make_class_dictable(Owner)
dictalchemy.utils.make_class_dictable(Seeker)
dictalchemy.utils.make_class_dictable(Pet)
dictalchemy.utils.make_class_dictable(Pet_Photo)
dictalchemy.utils.make_class_dictable(Connection)
dictalchemy.utils.make_class_dictable(Connect_Messages)


# Helper functions
def connect_to_db(app, db_uri="postgresql:///petshare"):
    """Connect to the database to our Flask app.

    Default db_uri is our petshare db. if testing, pass in testdb url
    """

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def test_data():
    """Create example data to test databse."""

    test_user1 = User(last_name='Brown',
                      first_name='Charlie',
                      email='charlie@gmail.com',
                      password='abc123',
                      birthdate='1996-07-11',
                      phone_number='415-555-555',
                      occupation='cartoon character',
                      address='123 Abc At',
                      city='San Francisco',
                      state='CA',
                      zipcode='94121',
                      image_url='http://emilypfreeman.com/wp-content/uploads/2015/11/easteregg11-2-1c.jpg')

    test_user2 = User(last_name='Pelt',
                      first_name='Linus',
                      email='linus@gmail.com',
                      password='abc123',
                      birthdate='1996-08-11',
                      phone_number='415-555-555',
                      occupation='cartoon character',
                      address='123 Def At',
                      city='San Francisco',
                      state='CA',
                      zipcode='94121',
                      image_url='https://eatingfastfood.files.wordpress.com/2011/07/linus.jpg')

    db.session.add(test_user1)
    db.session.add(test_user2)

    # add users to use for next tables
    db.session.commit()

    charlie = Owner(user_id=1)
    linus = Seeker(user_id=2)

    # add owner and seeker to use for next tables
    db.session.add(charlie)
    db.session.add(linus)
    db.session.commit()

    snoopy = Pet(name='Snoopy',
                 age=4,
                 gender='M',
                 size='48lbs',
                 color='white with black spots',
                 breed='beagle',
                 animal_type='dog',
                 owner_id=1,
                 is_available=True,
                 character_details='Snoopy is a loyal, innocent, imaginative and good-natured talking beagle who is prone to imagining fantasy lives',
                 health_details='Snoopy can be selfish and/or lazy at times',
                 image_url='https://pbs.twimg.com/profile_images/2256335229/snoopy-happy_400x400.gif')

    heathcliff = Pet(name='HeathCliff',
                     age=7,
                     gender='M',
                     size='18lbs',
                     color='orange',
                     breed='tabby',
                     animal_type='cat',
                     owner_id=1,
                     is_available=True,
                     character_details='Heathcliff is a street cat who loves to fight anyone but will not fight girls, He will also lie, cheat and steal to get himself some food, but beneath it all, he is a good guy.',
                     health_details='Super active.',
                     image_url='https://i1.ytimg.com/sh/rFSGy6sxOv8/showposter.jpg?')

    db.session.add(snoopy)
    db.session.add(heathcliff)
    # add pet to use for next table
    db.session.commit()

    photo1 = Pet_Photo(pet_id=1,
                       image_url='https://s-media-cache-ak0.pinimg.com/564x/e1/b5/f5/e1b5f57f63e00a02b852ac6051f31741.jpg',
                       caption='Group hug with my human BFF and little buddy woodstock')

    photo2 = Pet_Photo(pet_id=1,
                       image_url='http://www.picgifs.com/clip-art/cartoons/christmas-snoopy/clip-art-christmas-snoopy-938072.jpg',
                       caption='I love Christmas time!')

    db.session.add(photo1)
    db.session.add(photo2)

    connect = Connection(pet_id=1,
                         owner_id=1,
                         seeker_id=1,
                         connection_status='Interested')

    db.session.add(connect)
    db.session.commit()


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."
