"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    flash("That's the WRONG login!")
    return render_template("homepage.html")

@app.route("/users")
def user_list():
    """Show list of users."""

    user = User.query.all()
    return render_template("user_list.html", users-users)


@app.route("/register")
def register():
    return render_template("/register.html")



@app.route("/registeruser", methods=['POST']) 
def registeruser():                             #define the form action from register.html
    email = request.form.get("email")           #get these from the register.html form inputs
    password = request.form.get("password")
    age = request.form.get("age")
    zipcode = request.form.get("zipcode")

    user = User(email=email, password=password, age=age, zipcode=zipcode)   #add inputs to the User table in DB

    db.session.add(user)    #add the user to the session
    db.session.commit()     

    return redirect("/")


@app.route("/login") 
def login():
    return render_template("login.html")


@app.route("/processlogin", methods=['POST'])
def processlogin():
    email_input = request.form.get("email") 
    password = request.form.get("password")

    # find user by email and compare email and password
    # query for user by email
    login_user = User.query.filter_by(email=email_input).first()
    # print login_user
    # print login_user.email
    # print login_user.password

    #compare email and password to the query result
    if password = login_user.password:
        print login_user.password

        #if true add user to FLASK session, look up in shopping cart how to add things to the Flask session



    #if false redirect user to login
    else:
        return redirect("/login")

    # password != login_user.password ... this is what else means, but we dont have to type it because  the pw either equals something or not) 



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()