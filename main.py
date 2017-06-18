from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
 

def index():
    form = FlaskForm()
    return "Hello World"

app.run()