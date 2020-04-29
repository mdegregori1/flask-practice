from test.models import User
from test import app, db, bcrypt
import json
from flask import request, jsonify, Flask, make_response
from flask_login import login_user
import jwt
import datetime

app.config['SECRET_KEY'] = 'd6b5e117f8fc98bd1e97831d0bea530c'

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
    auth = request.authorization
    user = User.query.filter_by(username=req["username"]).first()
    # user = User(username=form.username.data, password=hashed_password)
    if user:
        return make_response("Username already exists. Try again.", 400)
    
    entered_password_1 = req["password1"]
    entered_password_2 = req["password2"]
    if entered_password_1 == entered_password_2:
        new_user = User(username = req["username"],password = bcrypt.generate_password_hash(entered_password_1))
        db.session.add(new_user)
        db.session.commit()
        token = jwt.encode({'id': new_user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, app.config['SECRET_KEY'])
        return jsonify({'token' : token.decode("ascii")})
        
    else:
        return make_response("Sorry, passwords must match", 400)
    # hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    # db.session.add(user)
    # db.session.commit()


@app.route("/login", methods=["GET", "POST"])
def login():
    req = request.json
    auth = request.authorization
    user = User.query.filter_by(username=req["username"]).first()
    if user and bcrypt.check_password_hash(user.password, req["password"]):
        token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, app.config['SECRET_KEY'])
        return jsonify({'token' : token.decode("ascii")})
        # print(f"{user} logged in!")
    else:
        return make_response("Sorry, invalid credentials", 401)
 
