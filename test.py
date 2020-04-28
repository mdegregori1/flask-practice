from flask import Flask
app = Flask(__name__)

@app.route('/home/<string:name>')
def hello_name(name):
    return f"Hello, {name}"