# # """Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db


# # here we are importing information from our model.py file. we are importing the tables that we created. The tables are created by the classes USER, MOVIE, and RATING. We also import the connect_to_db function and the db funtion to import our connection and the actual database.
# # a method is a function inside a class
# # when we run through a class we create an instance 

from server import app

from datetime import datetime


def load_users():
    """Load users from u.user into database."""
    text = open('seed_data/u.user')
    allusers = text.read().split()

    for row in allusers:
        row = row.rstrip()
        user_id, age, gender, occupation, zipcode =row.split("|") 
        user = User(user_id = user_id, age=age, zipcode=zipcode)
        # we say user here as the first word ... user =... because user is each row that we are assigning
      

        # if we dont have the fields or the information from the raw data files u.user, then we dont have information to put into the datatable for email and password. "None" in python equals "null" in SQL. We dont need SQL. since we arent using the gender or the occupation, later, we dont need to even populate it into the table. For now, email and password are null
        db.session.add(user)
        # we made user... now we have to use user and add it to the session which is the User table.. session. merge and session.replace (look this shit up)

    db.session.commit()

def load_movies():
    """Load movies from u.item into database."""

    text = open('seed_data/u.item')
  
    for line in text:
        line.rstrip()
        row = line.split("|")
        movie_id= row[0]
        titleyear = row[1]
        title = titleyear[:-7]
        stringdate = row[2]
        if stringdate is None:
            released_at = datetime.strptime(stringdate, "%d-%b-%Y")
        else: 
            released_at = datetime.now()
        imdb_url = row[3]

        movie = Movie(movie_id = movie_id, title = title, released_at = released_at, imdb_url= imdb_url)
        db.session.add(movie)

    db.session.commit()
     



# def load_ratings():
#     """Load ratings from u.data into database."""

#     text = open('seed_data/u.data')
#     allratings = text.read().split()

#     for row in allratings:
#         row = row.rstrip()
#         user_id, movie_id, score, timestamp



if __name__ == "__main__":
    connect_to_db(app)

    load_users()
    load_movies()
# #     load_ratings()
