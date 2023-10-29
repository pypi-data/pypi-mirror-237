from . import views
from .base import ConfigModel


def init_app(app):
    views.init_app(app)
