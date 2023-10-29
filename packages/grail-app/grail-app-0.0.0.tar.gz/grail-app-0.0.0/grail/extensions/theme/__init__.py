import flask
from flask.typing import ResponseReturnValue
from pathlib import Path
from . import cli

HERE = Path(__file__).parent

BASE_TEMPLATE = "base.html"
DEFAULT_THEME = "demo1"

demo = flask.Blueprint("demo", __name__)


@demo.get("/<path:filename>")
def page(filename: str) -> ResponseReturnValue:
    dirname: Path = flask.current_app.config["DEMO_FOLDER"]
    return flask.send_from_directory(str(dirname), filename)


@demo.get("/static/<path:filename>")
def asset(filename: str) -> ResponseReturnValue:
    dirname: Path = (
        Path(flask.current_app.config["DEMO_FOLDER"])
        / flask.current_app.config["THEME"]
        / "dist"
    )
    return flask.send_from_directory(str(dirname), filename)


def init_app(app: flask.Flask) -> None:
    theme_name = app.config.setdefault("THEME", DEFAULT_THEME)
    theme = flask.Blueprint(
        "theme",
        __name__,
        url_prefix="/theme",
        template_folder=HERE / "themes" / theme_name,
        static_folder=HERE / "static" / theme_name,
        static_url_path="/theme/static",
    )

    app.config.setdefault("BASE_TEMPLATE", BASE_TEMPLATE)
    app.config.setdefault("DEMO_FOLDER", Path(app.root_path) / "demo")

    theme.cli.help = "Commands for managing new themes"
    theme.cli.add_command(cli.create_theme)

    app.register_blueprint(theme)
    app.register_blueprint(demo, url_prefix="/demo")

    init_icons(app)


def init_icons(app: flask.Flask) -> None:
    """Add icons to blueprints template context. Icons are stored in the theme's media folder.
    The icons can be used in templates like this:
    {%include 'duotune/general/gen025.svg'%}

    Args:
        app (flask.Flask): _description_
    """
    icons_folder = (
        Path(app.config["DEMO_FOLDER"])
        / app.config["THEME"]
        / "dist"
        / "assets"
        / "media"
        / "icons"
    )
    icons = flask.Blueprint("icons", __name__, template_folder=icons_folder)
    app.register_blueprint(icons)
