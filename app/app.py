import os

from flask import Flask

app = Flask(__name__)


@app.route("/hb")
def hb():
    test_envvar = os.environ.get("TEST_ENVVAR")
    return f"App is alive, number 2, {test_envvar}"
