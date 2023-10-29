import flask

from .cli import cli
from .lib import ADR_PATH, ADR_TEMPLATE, ADR_VIEWER_TEMPLATE_DIR


def init_app(app: flask.Flask) -> None:
    app.config.setdefault("ADR_PATH", ADR_PATH)
    app.config.setdefault("ADR_TEMPLATE", ADR_TEMPLATE)
    app.config.setdefault("ADR_VIEWER_TEMPLATE_DIR", ADR_VIEWER_TEMPLATE_DIR)

    app.cli.add_command(cli)
