from test.models import User
from test import app

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
    return f"{self.username}"

@app.route("/login", methods=["GET", "POST"])
def login():
    return "string for now"
 

