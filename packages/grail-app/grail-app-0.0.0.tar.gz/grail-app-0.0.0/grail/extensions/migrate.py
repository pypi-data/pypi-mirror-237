import pathlib
import flask
from flask_migrate import Migrate


def init_app(app: flask.Flask):
    db = app.extensions["sqlalchemy"].db
    migrationdir = pathlib.Path(app.root_path) / "migrations"
    Migrate(app, db, directory=str(migrationdir))
