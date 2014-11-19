from __future__ import absolute_import, print_function
import os.path
import logging
from logging import FileHandler, Formatter
from flask import Flask

_app = None
def app():
    assert _app != None
    return _app

def create(debug):
    create_app(debug)

def destroy():
    global _app
    _app = None

def create_app(debug):
    global _app
    # create our flask app
    static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'cocos'))
    _app = Flask(__name__, static_folder=static_folder)
    _app.config['DEBUG'] = debug

    # setup our flask app
    add_logging()
    register_blueprints()
    register_filters()

def add_logging():
    file_handler = FileHandler('python.log', mode='w')
    file_handler.setLevel(logging.ERROR)
    formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    app().logger.addHandler(file_handler)

def register_blueprints():
    from . import urls
    urls.register_blueprints(app())

def register_filters():
    from . import filters
    filters.register_filters(app())

def run(port=5000):
    debug = app().debug
    app().run(debug=debug, use_debugger=debug, use_reloader=debug, host='0.0.0.0', port=port)
