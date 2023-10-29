from . import config, model, view


def init_app(app):
    config.init_app(app)
    model.init_app(app)
    view.init_app(app)
