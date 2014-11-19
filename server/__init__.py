from __future__ import absolute_import, print_function
from . import flask

def run(debug, port=5000):
    flask.create(debug)
    flask.run(port)
    flask.destroy()
