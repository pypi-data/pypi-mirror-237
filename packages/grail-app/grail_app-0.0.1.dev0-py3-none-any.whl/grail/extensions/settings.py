import dynaconf
import flask
import os

def init_app(app:flask.Flask) -> None:
    # Dynaconf checks FLASK_ENV to determine which section of settings to use.
    # If FLASK_ENV is not set it uses ENV_FOR_DYNACONF which default to 'development'.
    # We want to default to 'production' so set FLASK_ENV (a.k.a app.config['ENV'])
    os.environ.setdefault('FLASK_ENV', 'production')
    with app.app_context():
        dynaconf.FlaskDynaconf(
            app,
            SETTINGS_FILE=[
                f"{app.root_path}/settings.yaml",
                f"{app.instance_path}/config.py",
            ],
            extensions_list="EXTENSIONS",  
        )
    extensions = [e.removesuffix(':init_app').removeprefix(f'{__package__}.') for e in app.config.get("EXTENSIONS", [])]
    app.logger.info(f"App initialized with FLASK_ENV='{app.config['ENV']}' with FLASK_DEBUG={app.config['DEBUG']} and extensions {extensions}")
  
