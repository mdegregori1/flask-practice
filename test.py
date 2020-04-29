from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# secret key
app.config['SECRET_KEY'] = 'd6b5e117f8fc98bd1e97831d0bea530c'

# initiate sqllite db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# pass app into sql db
db = SQLAlchemy(app)

# user
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    # posts = db.relationship('Post', backref="author", lazy=True)
    
    def __repr__(self):
        return f"User('{self.id}', {self.username})"


@app.route("/")
def hello():
    return "<h1>Home Page Test!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page!</h1>"

# add registration route
# methods allow for get and post to route
@app.route("/register", methods=["GET", "POST"])
def register():
    return f"{self.username}"

@app.route("/login", methods=["GET", "POST"])
def login():
    return "string for now"
 


#debugger on
if __name__ == '__main__':
    app.run(debug=True)

