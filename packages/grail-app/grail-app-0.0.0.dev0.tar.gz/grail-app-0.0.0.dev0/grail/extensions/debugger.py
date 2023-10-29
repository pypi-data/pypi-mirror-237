import flask
from werkzeug.debug import DebuggedApplication


def init_app(app: flask.Flask):
    app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
