from flask_appbuilder import ModelView, expose, has_access
import inspect

import flask, sys
from flask_appbuilder.models.generic import (
    GenericModel,
    GenericSession,
    GenericColumn,
    interface,
)
from flask_appbuilder.models import decorators

import blinker


class SignalModel(GenericModel):
    name = GenericColumn(str, primary_key=True)
    receivers = GenericColumn(str)
    doc = GenericColumn(str)

    @classmethod
    def from_signal(self, signal: blinker.Signal):
        doc = (
            signal.__doc__
            if signal.__doc__ != "A named generic notification emitter."
            else ""
        )
        funcs = (r() for r in signal.receivers.values())
        receivers = (f"{f.__module__}:{f.__name__}" for f in funcs)
        model = SignalModel(name=signal.name, receivers=",".join(receivers), doc=doc)
        return model

    @property
    def targets(self):
        for l in self.receivers.split(","):
            if not l:
                continue
            module_name, func_name = l.split(":")
            module = sys.modules[module_name]
            func = module.__dict__[func_name]
            yield func

    @decorators.renders("locations")
    def locations(self):
        # will render this columns as bold on ListWidget
        locations = []
        for func in self.targets:
            path = f"{func.__code__.co_filename}:{func.__code__.co_firstlineno}"
            code = inspect.getsource(func)
            link = f'<a href="vscode://file{path}">{func.__module__}:{func.__name__}</a><div><pre>{code}</pre></div>'
            locations.append(link)
        return flask.Markup("</br>".join(locations))


class SignalSession(GenericSession):
    def __init__(self, namespace: blinker.Namespace = None):
        super().__init__()
        self.namespace: blinker.Namespace = namespace
        if not self.namespace:
            self.namespace = blinker.signal.__self__
        self.query_class = "SignalModel"

    def all(self):
        self.delete_all(SignalModel())
        for name in self.namespace.keys():
            self.add_object(name)
        return super().all()

    def get(self, pk):
        self.delete_all(SignalModel())
        self.add_object(pk)
        return super().get(pk=pk)

    def add_object(self, name):
        model = self._signal_to_obj(name)
        self.add(model)

    def _signal_to_obj(self, name):
        signal = self.namespace.get(name)
        if not signal:
            return None

        return SignalModel.from_signal(signal)


class SignalInterface(interface.GenericInterface):
    def __init__(self, session=None):
        if not session:
            session = SignalSession(blinker.signal.__self__)
        super().__init__(SignalModel, session)


class SignalsView(ModelView):
    list_title = "Signals"
    datamodel = SignalInterface()
    base_permissions = ["can_list", "can_show"]
    list_columns = ["name", "locations", "doc"]
    show_columns = list_columns

    links = [
        dict(
            url=lambda name: flask.url_for(".show", pk=name),
            title="View",
            icon="fa fa-search",
            description="See Details",
        )
    ]

    # @has_access
    @expose("/json")
    def json(self):
        all_json = {}
        for s in self.datamodel.session.all()[1]:
            all_json[s.name] = s.receivers.split(",") if s.receivers else []
        return flask.jsonify(all_json)


def init_app(app):
    appbuilder = app.extensions.get("appbuilder")
    if appbuilder:
        appbuilder.add_view(
            SignalsView, "Signals", icon="fa-level-up", category="Developer"
        )
