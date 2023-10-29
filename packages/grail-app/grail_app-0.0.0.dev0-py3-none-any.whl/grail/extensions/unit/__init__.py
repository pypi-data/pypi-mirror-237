"""
This module contains the Unit extension for Flask.

Nginx Unit is a dynamic web application server, designed to run applications
written in several different languages. Unit is lightweight, polyglot, and
blazingly fast.

This extension provides a simple interface to the Unit API for managing
applications and configuration.

For more information, see the `Unit documentation`
<https://unit.nginx.org/>_.

"""
import flask
import click, os
from .controller import Controller, get_controller
from . import api
from    pathlib import Path
from typing import Optional

UNIT_ROUTES_PREFIX = "/unit"
UNIT_EXTENSION_NAME = "unit"



bp = flask.Blueprint("unit", __name__, static_folder=None, template_folder=None)
"""The Flask blueprint for the Unit extension."""

bp.cli.help = "Manage NginX Unit applications and configuration"


@bp.route("/restart/<app_name>")
def restart_app(app_name):
    return get_controller().restart_app(app_name).json()


@bp.route("/reload")
def reload():
    filename = flask.current_app.config["UNIT_CONFIG_FILE"]
    with open(filename, "rb") as f:
        return get_controller().put("config", data=f).json()


@bp.route("/<path:path>")
@bp.route("/")
def get(path=""):
    return get_controller().get(path).json()


@bp.route("/log/access")
def access_log():
    filename = flask.current_app.config["UNIT_ACCESS_LOG"]
    with open(filename, "r") as f:
        return f.read()


@bp.cli.command("reload")
def cli_reload():
    """Reload the entire configuration from file"""
    filename = flask.current_app.config["UNIT_CONFIG_FILE"]
    with open(filename, "rb") as f:
        click.echo(get_controller().put("config", data=f).json())


@bp.cli.command("get")
@click.argument("path", default="")
def cli_get(path):
    """Get the configuration by path"""
    click.echo(get_controller().get(path).json())


@bp.cli.command("restart")
@click.argument("app_name")
def cli_restart(app_name):
    """Restart a app by name"""
    click.echo(get_controller().restart_app(app_name).json())

@bp.cli.command('shutdown')
@click.argument("app_name")
def cli_shutdown(app_name:str) -> None:
    """Shutdown an app by name"""
    error = api.shutdown_application(app_name)
    if error:
        click.echo(error)
    else:
        click.echo(f"Shutdown app {app_name}")
@bp.cli.command("launch")
@click.argument("app_name")
@click.option("--route", default=None, help="Route to use for the app")
@click.option("--user", default=None, help="linux user to run the app as")
def cli_launch(app_name:str,route:Optional[str]=None,user:Optional[str]=None)->None:
    """Launch an app by name"""
    
    app = api.FlaskApp(
        name=app_name,
        user=user or os.getlogin()
    )

    result = api.launch(app,prefix=route or f"/{app_name}")
    
    if 'url' in result:
        click.echo(f"Launched app at {result['url']}")
        import webbrowser
        webbrowser.open(result['url'])
    else:
        click.echo(f"Failed to launch app {app_name}: {result}")

@bp.cli.command("install")
@click.argument("app_name")
@click.option("--requirements", default=None, help="Files to include in the app")
@click.option("--include", default=False, help="pip install to include in the app")
def cli_install(app_name:str,requirements:Optional[Path]=None,include=False)->None:
    """Install an app by name"""

    files: list[api.FlaskAppFile]   = []
    requirements = Path(requirements) if requirements else None
    if requirements and requirements.exists():
        files.append(api.FlaskAppFile(name='requirements.txt',content=requirements.read_text()))

    app = api.FlaskApp(
        name=app_name,
        files=files
    )
    envpath = api.create_venv(app)
    if envpath:
        click.echo(f"Using venv at {envpath}")

    written_files = api.write_app_files(app)
    if files:
        click.echo(f"Wrote files to {files}")

    if include:
        installed_dir = api.install_global_requirements(app)
        click.echo(f"Installed global requirements from {installed_dir}")

    reqfile = api.install_flask_requirements(app)
    if reqfile:
        click.echo(f"Installed requirements from {reqfile}")
    
    logpath = api.create_logdir(app)
    if logpath:
        click.echo(f"Created logdir at {logpath}")


def init_app(app: flask.Flask) -> None:
    """
    Initialize the Unit extension. Creates a new :class:`Controller`
    and registers the :class:`flask.Blueprint` with the Flask application.
    """

    enabled = app.debug

    # app.logger.info(f"Unit extension {'enabled' if enabled else 'disabled'}")
    if not enabled:
        return

    unit_route = app.config.setdefault("UNIT_ROUTES_PREFIX", UNIT_ROUTES_PREFIX)
    unit_extension = app.config.setdefault("UNIT_EXTENSION_NAME", UNIT_EXTENSION_NAME)
    config_file = app.config.setdefault(
        "UNIT_CONFIG_FILE", f"{app.root_path}/.unit/config/config.json"
    )
    access_log = app.config.setdefault(
        "UNIT_ACCESS_LOG", f"{app.root_path}/.unit/log/access.log"
    )
    unit_log = app.config.setdefault("UNIT_LOG", f"{app.root_path}/.unit/log/unit.log")

    # app.logger.info(f"Unit config file: {config_file} access log: {access_log} unit log: {unit_log}")

    app.extensions[unit_extension] = Controller(config_file=config_file)

    app.register_blueprint(bp, url_prefix=unit_route)

    api.init_app(app)