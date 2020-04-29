from test.models import User
from test import app, db, bcrypt
import json
from flask import request, jsonify


@app.route("/")
def hello():
    return "<h1>Home Page Test :) !</h1>"

@app.route("/about")
def about():
    return "<h1>About Page :) !</h1>"

# add registration route
# methods allow for get and post to route
@app.route("/register", methods=["GET", "POST"])
def register():
    req = request.json
    user = User.query.filter_by(username=req["username"]).first()
    # user = User(username=form.username.data, password=hashed_password)
    if user:
        return "Username already exists"
    
    entered_password_1 = req["password1"]
    entered_password_2 = req["password2"]
    if entered_password_1 == entered_password_2:
        new_user = User(username = req["username"],password = bcrypt.generate_password_hash(entered_password_1))
        db.session.add(new_user)
        db.session.commit()
        return f"Created {new_user}"
    else:
        return "Passwords don't match. Try again."
    # hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    # db.session.add(user)
    # db.session.commit()


@app.route("/login", methods=["GET", "POST"])
def login():
    return "string for now"
 
