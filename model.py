"""Models and database functions for PetShare project."""

from flask_sqlalchemy import flask_sqlalchemy

db = SQLAlchemy()


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