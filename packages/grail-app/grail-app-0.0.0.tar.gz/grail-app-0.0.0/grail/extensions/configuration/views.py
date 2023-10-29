from .base import (
    ConfigFileSession,
    ConfigViewBase,
    ConfigInterface,
    CurrentAppConfigSession,
)
from .validators import ValueMustBe, MustBeAlphaNum
from flask_appbuilder import action, AppBuilder
import flask
from pathlib import Path

instance_config_session = ConfigFileSession(
    lambda: Path(flask.current_app.instance_path) / "config.py"
)


class InstanceConfigView(ConfigViewBase):
    list_title = "Instance Config"
    datamodel = ConfigInterface(instance_config_session)

    hidden_keys = []
    validators_columns = {
        "value": [
            # ValueMustBe('ROLE',lambda: flask.current_app.config.get('AVAILABLE_ROLES')),
            # ValueMustBe('APP_THEME',lambda: flask.current_app.config.get('AVAILABLE_THEMES')),
            # ValueMustBe('REMOTE_CREDITS_ENABLED',['True','False']),
            # MustBeAlphaNum('HOSTNAME'),
        ],
    }

    def post_update(self, item):
        flask.current_app.config.from_pyfile(self.datamodel.session.filepath)
        return super().post_update(item)

    def post_edit_redirect(self):
        return flask.redirect(flask.url_for(".list"))


class AppConfigView(ConfigViewBase):
    list_title = "App Config"
    datamodel = ConfigInterface(CurrentAppConfigSession())
    base_permissions = ["can_list"]

    @action(
        "override",
        text="Override",
        confirmation="Override configs?",
        icon="fa-pencil",
        multiple=True,
        single=True,
    )
    def override(self, items):
        if not isinstance(items, list):
            items = [items]

        flask.current_app.logger.debug(f"Overriding items: {items}")
        for i in items:
            InstanceConfigView.datamodel.edit(i)

        return flask.redirect(flask.url_for("InstanceConfigView.list"))


def init_app(app):
    appbuilder: AppBuilder = app.extensions.get("appbuilder")
    if not appbuilder:
        return
    appbuilder.add_view(
        InstanceConfigView, "Settings", icon="fa-home", category="Developer"
    )
    appbuilder.add_view(
        AppConfigView, "Configuration ", icon="fa-circle", category="Developer"
    )
