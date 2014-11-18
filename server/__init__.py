from __future__ import absolute_import, print_function
from . import flask

def run(debug):
    flask.create(debug)
    flask.run()
    flask.destroy()
