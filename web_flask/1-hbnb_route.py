#!/usr/bin/python3

"""
A script to start a simple flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """ Display 'hello HBNB!' when accessinn the route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """ Display HBNB when accessimg route """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
