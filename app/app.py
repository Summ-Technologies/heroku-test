from flask import Flask

app = Flask(__name__)


@app.route("/hb")
def hb():
    return "App is alive"
