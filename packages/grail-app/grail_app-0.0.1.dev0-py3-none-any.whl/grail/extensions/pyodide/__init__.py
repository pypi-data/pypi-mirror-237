import flask

bp = flask.Blueprint("pyodide", __name__, template_folder="templates")


@bp.route("/cli/")
def render_pyodide() -> str:
    return flask.render_template("pyodide-cli.html")


def init_app(app: flask.Flask) -> None:
    app.register_blueprint(bp, url_prefix="/python")
