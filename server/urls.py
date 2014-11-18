from __future__ import absolute_import, print_function
from . import views

def register_blueprints(app):
    app.register_blueprint(views.cocos.blueprint)
