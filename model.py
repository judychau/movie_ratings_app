"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
class User(db.Model):
    """User of rating website"""

    __tablename__="users"


    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        """ This will give us useful information when we print the user_id, instead of printing the space where it is stored ... like <__main__.User object at 0x7f1aa026a310>... it will print out what we ask it to in the function body defined below... """

        return "<User user_id=%s email=%s password=%s age=%s zipcode=%s >" % (self.user_id,self.email, self.password, self.age, self.zipcode)

class Movie(db.Model):

    __tablename__="movies"

    movie_id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    released_at = db.Column(db.DateTime)
    imdb_url = db.Column(db.String)

class Rating(db.Model):

    __tablename__="ratings"

    rating_id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    score = db.Column(db.Integer)


# Model definitions

# Delete this line and put your User/Movie/Ratings model classes here.


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ratings.db'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."

