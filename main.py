from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

caesar_form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form action="/" id="caesar-form" method="post">
            <label for="rot">Rotate by:</label>
                 <input id="rot" type="text" name="rot" value="0"/>
            </br>
            <label for="text">Text:
                 <textarea id="text" name="text" form="caesar-form"></textarea>
            </label>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return caesar_form

@app.route("/", methods =['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']

    rot = int(rot)
    text = str(text)

    rot_text = rotate_string(text, rot)

    return '<h1>' + rot_text + '</h1>'

app.run()