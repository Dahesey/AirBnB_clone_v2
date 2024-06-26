#!/usr/bin/python3
"""
A script to strt a simple flask web application
"""

from flask import Flask
from flask import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """ Display below text when route is accessed """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """ Display below text when route is accessed """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Display C followed by text when route is accessed """
    return "C " + escape(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
