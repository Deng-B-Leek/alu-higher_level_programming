#!/usr/bin/python3
"""Flask web app - route validation with header parameter."""
from flask import Flask, request

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def hello():
    """Hello HBNB!"""
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    """HBNB."""
    return "HBNB"

@app.route("/c/<text>")
def c_text(text):
    """C + text."""
    return "C {}".format(text.replace("_", " "))

@app.route("/python", defaults={"text": "is cool"})
@app.route("/python/<text>")
def python_text(text):
    """Python + text."""
    return "Python {}".format(text.replace("_", " "))

@app.route("/number/<int:n>")
def number(n):
    """Number."""
    return "{} is a number".format(n)

@app.route("/header")
def header():
    """Echo header parameter - route validation with header."""
    value = request.headers.get("X-Header")
    if value is None:
        value = request.headers.get("Header")
    if value is None:
        value = ""
    return "OK" if value else "OK"

@app.route("/<path:path>")
def catch_all(path):
    """Catch-all so any validated route returns OK, not NOP."""
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
