from flask_appbuilder.models.generic import (
    GenericModel,
    GenericSession,
    GenericColumn,
    interface,
)
from flask_appbuilder import ModelView
import flask
from pathlib import Path
from datetime import datetime
import os

from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from wtforms import StringField

DEFAULT_HIDDEN_KEYS = [
    "SECRET_KEY",
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "TB_SECRET_SALT",
    "TB_DEVICE_PROVISION_SECRET",
]


class ConfigModel(GenericModel):
    name = GenericColumn(str, primary_key=True)
    value = GenericColumn(str)

    def __repr__(self):
        return f"Config(name='{self.name}',value='{self.value}')"


class FileBackedSession(GenericSession):
    def __init__(self, filepath, *args, **kwargs) -> None:
        self._filepath = filepath
        super().__init__(*args, **kwargs)

    @property
    def filepath(self):
        fp = Path(self._filepath() if callable(self._filepath) else self._filepath)
        return fp

    def append(self, item):
        with open(self.filepath, "a") as f:
            f.write(item)


class ConfigSessionBase(GenericSession):
    loader = lambda s: {}

    def __init__(self, loader=None, *args, **kwargs):
        self._loader = loader or self.loader
        self._hidden = []
        super().__init__(*args, **kwargs)

    def get(self, pk):
        self._refresh()
        self.query_class = "ConfigModel"
        obj = super().get(pk)
        if not obj:
            val = flask.current_app.config.get(pk)
            obj = ConfigModel(name=pk, value=val)
        return obj

    def filter_names(self, inlist):
        self._hidden += inlist
        return self

    def all(self):
        self._refresh()
        return super().all()

    def _refresh(self):
        self.delete_all(ConfigModel())
        configs = self._load()
        for name, value in configs.items():
            if self._hidden and name in self._hidden:
                value = "**HIDDEN**"
            model = ConfigModel(name=name, value=value)
            self.add(model)

    def _load(self):
        return self._loader()


class ConfigFileSession(ConfigSessionBase, FileBackedSession):
    def __init__(self, loader=None, *args, **kwargs):
        super().__init__(loader, filepath=loader, *args, **kwargs)

    def update(self, item):
        self.append(item)
        self._refresh()

    def _load(self):
        filepath = self._loader()
        config = flask.config.Config(filepath.parent)
        config.from_pyfile(filepath, silent=True)
        return config


class CurrentAppConfigSession(ConfigSessionBase):
    loader = lambda s: flask.current_app.config


class ConfigInterface(interface.GenericInterface):
    def __init__(self, session):
        super().__init__(ConfigModel, session)

    def item_to_pystring(self, item):
        current_value = flask.current_app.config.get(item.name)
        current_type = type(current_value)
        formatter = dict(
            bool=str,
            int=int,
            float=float,
        ).get(current_type.__name__, lambda s: '"' + str(s) + '"')

        r = formatter(item.value)
        return str(r)

    def edit(self, item):
        """
        Edit (change) object
        """
        if item.name in FilterHidden.current_hidden_keys():
            self.message = (f"Cannot change {item.name}", "danger")
            return None
        user = (
            flask.current_app.extensions["appbuilder"].sm.current_user
            if flask.has_request_context()
            and "appbuilder" in flask.current_app.extensions
            else None
        )
        email = user.email if user else os.environ.get("USER", "Unknown")
        when = datetime.utcnow()
        config_to_str = (
            f"\n{item.name}=" + self.item_to_pystring(item) + f" # at {when} by {email}"
        )
        self.session.update(config_to_str)
        return {item.name: item.value}


class BS3TextFieldROWidget(BS3TextFieldWidget):
    def __call__(self, field, **kwargs):
        kwargs["readonly"] = "true"
        return super(BS3TextFieldROWidget, self).__call__(field, **kwargs)


from flask_appbuilder.models.generic.filters import BaseFilter


class FilterHidden(BaseFilter):
    """Check if name is in a list"""

    name = "Hidden"

    @staticmethod
    def current_hidden_keys():
        hidden = ConfigViewBase.hidden_keys

        try:
            method = flask.current_app.view_functions.get(
                flask.request.url_rule.endpoint, None
            )
            if method:
                hidden = hidden + method.__self__.__class__.hidden_keys
        except:
            pass
        return hidden

    def apply(self, query, _):
        return query.filter_names(self.current_hidden_keys())


class ConfigViewBase(ModelView):
    base_permissions = ["can_list", "can_edit"]
    list_columns = ["name", "value"]
    base_order = ("name", "asc")
    page_size = 1000
    edit_form_extra_fields = {
        "name": StringField("name", widget=BS3TextFieldROWidget())
    }
    hidden_keys = DEFAULT_HIDDEN_KEYS
    base_filters = [["name", FilterHidden, None]]
