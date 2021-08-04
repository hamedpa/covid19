from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<p>Hello, World!</p><img class="logo" src="../_static/flask-icon.png" alt="Logo">'


if __name__ == "__main__":
    app.run()

