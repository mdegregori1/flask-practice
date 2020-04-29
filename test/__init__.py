# where we initilize the application - Think app.js
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
# secret key
app.config['SECRET_KEY'] = 'd6b5e117f8fc98bd1e97831d0bea530c'
# initiate sqllite db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# pass app into sql db
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from test import routes