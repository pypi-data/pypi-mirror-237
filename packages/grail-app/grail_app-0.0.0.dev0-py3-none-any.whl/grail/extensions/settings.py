import dynaconf


def init_app(app) -> None:
    with app.app_context():
        dynaconf.FlaskDynaconf(
            app,
            SETTINGS_FILE=[
                "/app/settings.yaml",
                f"{app.root_path}/settings.yaml",
                f"{app.instance_path}/config.py",
            ],
            extensions_list="EXTENSIONS",  # type: ignore
        )
