from flask_appbuilder import ModelView, expose, has_access
import inspect
from flask_appbuilder.models import decorators

import flask, pathlib
from flask_appbuilder.models.generic import (
    GenericModel,
    GenericSession,
    GenericColumn,
    interface,
)

from werkzeug.routing import Rule


class EndpointModel(GenericModel):
    name = GenericColumn(str, primary_key=True)
    rules = GenericColumn(str)
    function = GenericColumn(str)
    code = GenericColumn(str)
    doc = GenericColumn(str)


class TemplateModel(GenericModel):
    name = GenericColumn(str, primary_key=True)
    owner = GenericColumn(str)
    path = GenericColumn(str)
    content = GenericColumn(str)

    @decorators.renders("location")
    def location(self):
        # will render this columns as link to vscode
        path = pathlib.Path(self.path) / pathlib.Path(self.name)
        return flask.Markup(f'<a href="vscode://file{path}">{path}')


class AppSession(GenericSession):
    def __init__(self, model_class, app: flask.Flask = None):
        super().__init__()
        self._app = app
        if not self._app:
            self._app = lambda: flask.current_app._get_current_object()
        self.model_class = model_class
        self.query_class = model_class.__name__

    @property
    def app(self) -> flask.Flask:
        return self._app() if callable(self._app) else self._app


class EndpointSession(AppSession):
    @property
    def rules(self):
        return self.app.url_map._rules_by_endpoint

    def all(self):
        self.delete_all(self.model_class())
        for endpoint in self.rules.keys():
            self.add_object(endpoint)
        return super().all()

    def get(self, endpoint):
        self.delete_all(self.model_class())
        self.add_object(endpoint)
        return super().get(pk=endpoint)

    def add_object(self, endpoint):
        rules = self.rules[endpoint]
        model = self._endpoint_to_obj(endpoint, rules)
        self.add(model)

    def _rule_to_str(self, r: Rule):
        return str(r) + " " + str(list(r.methods))

    def _endpoint_to_obj(self, endpoint, rules):
        rules = ",".join(self._rule_to_str(r) for r in rules)
        function = self.app.view_functions[endpoint]
        module_function = function.__module__ + ":" + function.__name__
        code = inspect.getsource(function)
        doc = function.__doc__
        return EndpointModel(
            name=endpoint, rules=rules, function=module_function, code=code, doc=doc
        )


class TemplateSession(AppSession):
    def all(self):
        self._load()
        return super().all()

    def get(self, endpoint):
        self._load()
        return super().get(pk=endpoint)

    def list_all(self, blueprints=None, prefix=True):
        """
        Return all app templates.
        Blueprint templates will be returned for blueprints listed in the 'blueprints' array,
            or all if 'blueprints' is True.

        If 'prefix' is True, only return templates in the app's root_path.
        If 'prefix' is a string, only return templates that start with the value
        """
        from jinja2.loaders import ChoiceLoader, FileSystemLoader
        import os

        file_loaders = []

        loader = self.app.jinja_loader

        if isinstance(loader, ChoiceLoader):
            for l in loader.loaders:
                if isinstance(l, FileSystemLoader):
                    file_loaders.append(l)

        elif isinstance(loader, FileSystemLoader):
            file_loaders.append(loader)

        for l in file_loaders:
            for t in l.list_templates():
                yield (
                    t,
                    self.app.name,
                    os.path.join(self.app.root_path, self.app.template_folder),
                )

        if blueprints is None:
            return

        if isinstance(blueprints, list):
            blueprints = [self.app.blueprints[bp] for bp in blueprints]

        if isinstance(blueprints, bool) and blueprints == True:
            blueprints = self.app.iter_blueprints()

        if prefix == True:
            prefix = self.app.root_path

        for bp in blueprints:
            loader = bp.jinja_loader
            if loader and isinstance(loader, FileSystemLoader):
                for t in loader.list_templates():
                    if self.get_path(t).startswith(prefix):
                        yield (
                            t,
                            bp.name,
                            os.path.join(bp.root_path, bp.template_folder),
                        )

    def _load(self):
        self.delete_all(self.model_class())
        for template, owner, path in self.list_all(blueprints=True):
            content = (pathlib.Path(path) / template).read_text()
            self.add(
                TemplateModel(name=template, owner=owner, path=path, content=content)
            )

    def get_path(self, template_context_or_name):
        """Get the filepath of a template by name or 'self' if in a template"""
        from jinja2.runtime import TemplateReference

        name = template_context_or_name
        if isinstance(template_context_or_name, TemplateReference):
            name = template_context_or_name._TemplateReference__context.name
        try:
            path = self.app.jinja_env.get_template(name).filename
        except Exception as e:
            print(f"Failed getting tmamplate path for {name}: {e}")
            return None
        return path


class AppInterface(interface.GenericInterface):
    def __init__(self, model_class, session=None):
        if not session:
            session = AppSession(model_class=model_class)
        super().__init__(model_class, session)


class EndpointsView(ModelView):
    list_title = "Endpoints"
    show_title = "Ednpoint Details"
    datamodel = AppInterface(EndpointModel, session=EndpointSession(EndpointModel))
    base_permissions = ["can_list", "can_show"]
    list_columns = ["name", "rules", "function"]
    show_columns = list_columns + ["code", "doc"]
    base_order = ("name", "asc")
    page_size = 1000

    formatters_columns = {"code": lambda c: flask.Markup(f"<pre>{c}</pre>")}

    links = [
        dict(
            url=lambda name: flask.url_for(".show", pk=name),
            title="View",
            icon="fa fa-search",
            description="See Details",
        )
    ]


class TemplatesView(ModelView):
    list_title = "Templates"
    show_title = "Template Details"
    datamodel = AppInterface(TemplateModel, session=TemplateSession(TemplateModel))
    base_permissions = ["can_list", "can_show"]
    list_columns = [
        "name",
        "location",
        "owner",
    ]
    show_columns = list_columns + ["content"]
    page_size = 1000
    base_order = ("name", "asc")

    @expose("/show/<path:pk>", methods=["GET"])
    @has_access
    def show(self, pk):
        return super().show(pk=pk)

    links = [
        dict(
            url=lambda name: flask.url_for(".show", pk=name),
            title="View",
            icon="fa fa-search",
            description="See Details",
        )
    ]


def init_app(app):
    appbuilder = app.extensions.get("appbuilder")
    if appbuilder:
        appbuilder.add_view(
            EndpointsView, "Endpoints", icon="fa-arrow-right", category="Developer"
        )
        appbuilder.add_view(
            TemplatesView, "Templates", icon="fa-film", category="Developer"
        )
