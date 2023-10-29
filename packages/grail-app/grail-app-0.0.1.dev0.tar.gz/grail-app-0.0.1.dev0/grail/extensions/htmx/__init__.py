import flask

import flask_htmx

htmx = flask_htmx.HTMX()

bp = flask.Blueprint(
    "htmx",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/htmx/static",
)


def init_app(app: flask.Flask) -> None:
    htmx.init_app(app)
    app.register_blueprint(bp)
