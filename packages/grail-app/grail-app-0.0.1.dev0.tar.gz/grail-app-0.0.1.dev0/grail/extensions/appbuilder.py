from flask_appbuilder import AppBuilder
import flask


def init_app(app: flask.Flask) -> None:
    db = app.extensions["sqlalchemy"].db
    AppBuilder(app, db.session)
