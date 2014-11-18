from __future__ import absolute_import, print_function
import os
from flask import Blueprint
from flask.views import MethodView
from ..flask import app

blueprint = Blueprint('cocos', __name__)

class CocosFileView(MethodView):
    def __init__(self, *args, **kwargs):
        if 'file' in kwargs:
            self._file = kwargs.pop('file')
        super(CocosFileView, self).__init__(*args, **kwargs)

    def get(self, *args, **kwargs):
        return app().send_static_file(self._file)

class CocosPathView(MethodView):
    def __init__(self, *args, **kwargs):
        if 'path' in kwargs:
            self._path = kwargs.pop('path')
        super(CocosPathView, self).__init__(*args, **kwargs)

    def get(self, path, *args, **kwargs):
        return app().send_static_file(os.path.join(self._path, path))


blueprint.add_url_rule('/', view_func=CocosFileView.as_view('index.html', file='index.html'))
blueprint.add_url_rule('/project.json', view_func=CocosFileView.as_view('project.json', file='project.json'))
blueprint.add_url_rule('/res/<path:path>', view_func=CocosPathView.as_view('res', path='res'))

if app().debug:
    blueprint.add_url_rule('/frameworks/<path:path>', view_func=CocosPathView.as_view('frameworks', path='frameworks'))
    blueprint.add_url_rule('/src/<path:path>', view_func=CocosPathView.as_view('src', path='src'))
    blueprint.add_url_rule('/main.js', view_func=CocosFileView.as_view('main.js', file='main.js'))
else:
    blueprint.add_url_rule('/game.min.js', view_func=CocosFileView.as_view('game.min.js', file='game.min.js'))
