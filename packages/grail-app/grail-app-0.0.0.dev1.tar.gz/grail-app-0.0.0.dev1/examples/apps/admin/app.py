from grail.extensions import settings
import flask

app = flask.Flask(__name__, instance_relative_config=True)
settings.init_app(app)
