from typing import Any, Literal
from typing import Optional
from typing import Sequence, ForwardRef
from .base import Base, Generator
from .application import Model, Action, BREADPage, Application

from pydantic import validator, Field
from jinja2 import Template
from .filesystem import FilesystemModel, FilesystemFormatter
from flask import Flask

import textwrap

# --------BACKEND---------------
#   Flask AppBuilder App MetaModel
# ------------------------------


class SQLAColumn(Base):
    datatype: Any
    default: Any | None = None
    foreign_key: str | tuple[str, str] | None = None
    nullable: bool = False


class SQLARelationship(Base):
    target: str | tuple[str, str]
    backref: str | None = None


class M2M(SQLARelationship):
    kind: Literal["Kind.many_to_many"] = "Kind.many_to_many"
    secondary: str


class O2M(SQLARelationship):
    kind: Literal["Kind.one_to_many"] = "Kind.one_to_many"
    viewonly: bool = False


class O2O(SQLARelationship):
    kind: Literal["Kind.one_to_one"] = "Kind.one_to_one"


class M2O(SQLARelationship):
    kind: Literal["Kind.many_to_one"] = "Kind.many_to_one"


from typing import Union, Annotated

Relationship = Annotated[Union[M2M, O2M, M2O, O2O], Field(discriminator="kind")]


class SQLAModel(Base):
    tablename: str
    columns: list[SQLAColumn]
    relationships: Sequence[Relationship] = []
    mixins: list[str] = [
        "....extensions.appbuilder.Base",
    ]

    @validator("columns")
    def check_columns(cls, value: list[SQLAColumn]) -> list[SQLAColumn]:
        # if len(value) == 0:
        #    raise ValueError("There must be at least 1 column")
        return value


class FABView(Base):
    class FABAction(Base):
        name: str
        title: str
        icon: str = ""
        multiple: bool = True
        single: bool = True
        confirmation: str = ""

    name: str
    model: SQLAModel
    mixins: list[str] = ["ModelView"]
    list_columns: list[str] = []
    show_columns: list[str] = []
    edit_columns: list[str] = []
    add_columns: list[str] = []
    related_views: list[str] = []
    actions: list[FABAction] = []


class FABPermission(Base):
    pass


class Module(Base):
    models: list[SQLAModel] = []
    views: list[FABView] = []
    permissions: list[FABPermission] = []
    actions: list[Action] = []


class Extension(Base):
    requirements: list[str] = []
    config: dict[str, Any] = {}


class ExtensionsList(Base):
    items: list[Extension] = []


class FlaskApp(Base):
    modules: list[Module]
    extensions: list[Extension]
    config: dict[str, Any] = {}


# --------------------------------------


class SQLAModelColumnGenerator(Generator[Sequence[Model], dict[str, list[SQLAColumn]]]):
    def generate(self, inp: Sequence[Model]) -> dict[str, list[SQLAColumn]]:
        cols: dict[str, list[SQLAColumn]] = {}
        for model in inp:
            for attr in model.attributes:
                sm = SQLAColumn(
                    name=attr.name, datatype=attr.datatype, default=attr.default
                )

                if model.name not in cols:
                    cols[model.name] = []
                cols[model.name].append(sm)
            for rel in model.relationships:
                sm = SQLAColumn(
                    name=rel.name, datatype=attr.datatype, default=attr.default
                )

                if model.name not in cols:
                    cols[model.name] = []
                cols[model.name].append(sm)

        return cols


class SQLAModelGenerator(Generator[Sequence[Model], list[SQLAModel]]):
    mixins: list[str] = ["SQLAModel", "AuditMixin"]
    column_gen: SQLAModelColumnGenerator = SQLAModelColumnGenerator()

    def generate(self, inp: Sequence[Model]) -> list[SQLAModel]:
        sqla_models: list[SQLAModel] = []
        for model in inp:
            columns: dict[str, list[SQLAColumn]] = self.column_gen(inp)
            sm = SQLAModel(
                name=model.name,
                tablename=model.name.lower(),
                columns=columns[model.name],
            )

            sqla_models.append(sm)
        return sqla_models


class Bread2FABViewGenerator(Generator[BREADPage, FABView]):
    model: SQLAModel

    def generate(self, inp: BREADPage) -> FABView:
        view = FABView(
            name=inp.name,
            model=self.model,
        )
        return view


class FABViewGenerator(Generator[Application, list[FABView]]):
    def generate(self, inp: Application) -> list[FABView]:
        views: list[FABView] = []

        models: dict[str, SQLAModel] = {
            m.name: m for m in SQLAModelGenerator()(inp.datamodel.models)
        }

        for page in inp.pagemodel.pages:
            if isinstance(page, BREADPage):
                p: FABView = Bread2FABViewGenerator(model=models[page.model])(
                    page,
                )
                views.append(p)
            else:
                raise NotImplementedError
        return views


class ModulesGenerator(Generator[Application, list[Module]]):
    models: dict[str, list[str]]
    views: dict[str, list[str]]
    actions: dict[str, list[str]]
    models_gen: SQLAModelGenerator
    views_gen: FABViewGenerator

    def generate(self, inp: Application) -> list[Module]:
        module_names: set[str] = set(
            list(self.models.keys())
            + list(self.views.keys())
            + list(self.actions.keys())
        )
        modules: list[Module] = []
        for name in module_names:
            models: list[Model] = [
                m for m in inp.datamodel.models if m.name in self.models.get(name, [])
            ]

            module = Module(
                name=name,
                models=self.models_gen(models),
                actions=[],
                views=self.views_gen(inp),
            )

            modules.append(module)
        return modules


class FABGenerator(Generator[Application, FlaskApp]):
    modules: ModulesGenerator

    def generate(self, inp: Application) -> FlaskApp:
        return FlaskApp(
            name=inp.name,
            modules=self.modules(inp),
            extensions=[],
            config={},
        )


# ------------------------------------
# Code Generators (Model to Code)
# ------------------------------------


class SQLAColumnCodeGenerator(Generator[SQLAColumn, str]):
    template: str = """
        Column({{typemap[column.datatype]}}
            {%-if column.default%},default={{column.default}}){%endif-%}
            {%-if column.foreign_key%},ForeignKey('{{column.foreign_key}}'){%endif-%}
            ,nullable={{column.nullable}},)
        """

    typemap: dict[str, str] = {
        "string": "String",
        "integer": "Integer",
        "datetime": "DateTime",
        "boolean": "Boolean",
        "duration": "Interval",
        "text": "Text",
        "number": "Numeric",
        "json": "JSON",
    }

    def generate(self, inp: SQLAColumn) -> str:
        return Template(textwrap.dedent(self.template).lstrip()).render(
            column=inp, typemap=self.typemap
        )


class SQLARelationshipCodeGenerator(Generator[SQLAModel, dict[str, str]]):
    template: str = """relationship('{{relationship.target}}', {{extra_args}})"""

    def generate(self, inp: SQLAModel) -> dict[str, str]:
        rels: dict[str, str] = {}
        for rel in inp.relationships:
            extra_args: dict[str, str] = (
                {"backref": f"'{rel.backref}'"} if rel.backref else {}
            )
            match rel:
                case O2M(viewonly=True):
                    extra_args["viewonly"] = "True"
                case O2M():
                    extra_args["uselist"] = "True"
                case O2O():
                    extra_args["uselist"] = "False"
                case M2M():
                    extra_args["secondary"] = f"'{rel.secondary}'"
                case M2O():
                    pass
                case _:
                    raise ValueError(f"Invalid Relationshpi Type: {rel}")

            result = Template(textwrap.dedent(self.template).lstrip()).render(
                relationship=rel,
                extra_args=", ".join([f"{k}={v}" for k, v in extra_args.items()]),
            )
            rels[rel.name] = result

        return rels


class SQLAModelCodeGenerator(Generator[list[SQLAModel], list[FilesystemModel]]):
    column_gen: SQLAColumnCodeGenerator = SQLAColumnCodeGenerator()
    rel_gen: SQLARelationshipCodeGenerator = SQLARelationshipCodeGenerator()

    template: str = """
        {%for imp in imports%}
        {{imp}}
        {%endfor%}

        # Generated by SQLAModelCodeGenerator from {{model.name}}
        class {{model.name}}({%for m in model.mixins%}{{m.split('.')[-1]}}{%if not loop.last%},{%endif%}{%endfor%}):
            {%if model.description%}''' {{model.description}} '''{%endif%}

            __tablename__: str = "{{model.tablename}}"
            
            id = Column(Integer, primary_key=True)
            {%for name, defn in columns.items()%}
            {{name}} = {{defn}}
            {%if defn.description%}''' {{defn.description}} '''{%endif%}
            {%endfor%}
            {%for name, defn in relationships.items()%}
            {{name}} = {{defn}}
            {%if defn.description%}''' {{defn.description}} '''{%endif%}
            {%endfor%}

            def __repr__(self):
                return self.name
        """

    init_models_template: str = textwrap.dedent(
        """
        {%for m in models %}
        from .{{m.name|lower}} import {{m.name}}
        {%endfor %}
        import flask
        def init_app(app:flask.Flask):
            pass
        """
    ).lstrip()

    def imports(self, models: list[SQLAModel]) -> list[str]:
        all_imports: list[str] = []
        for model in models:
            imports: list[str] = (
                ["sqlalchemy.Column", "sqlalchemy.Integer"]
                + [
                    f"sqlalchemy.{self.column_gen.typemap[col.datatype]}"
                    for col in model.columns
                ]
                + model.mixins
            ) + (
                ["sqlalchemy.orm.relationship", "sqlalchemy.ForeignKey"]
                if model.relationships
                else []
            )
            import_strings: list[str] = [
                f"from {'.'.join(i.split('.')[:-1])} import {i.split('.')[-1]}"
                for i in imports
            ]
            all_imports += import_strings

        return all_imports

    def generate(self, inp: list[SQLAModel]) -> list[FilesystemModel]:
        files: list[FilesystemModel] = []
        for model in inp:
            columns: dict[str, str] = {
                c.name: self.column_gen(c) for c in model.columns
            }
            relationships: dict[str, str] = self.rel_gen(model)

            content: str = Template(textwrap.dedent(self.template)).render(
                model=model,
                columns=columns,
                relationships=relationships,
                imports=self.imports([model]),
            )
            files.append(
                FilesystemModel(
                    name=model.name + " SQLAModel",
                    path=f"{model.name.lower()}.py",
                    content=content,
                )
            )
        files.append(
            FilesystemModel(
                name=f"Initialize SQLAModel: {[m.name for m in inp]}",
                path="__init__.py",
                content=Template(textwrap.dedent(self.init_models_template)).render(
                    models=inp
                ),
            )
        )
        # TODO: Add relationships
        # TODO: Render template
        return files


class FABViewCodeGenerator(Generator[list[FABView], list[FilesystemModel]]):
    template: str = """
        from flask_appbuilder import ModelView
        from flask_appbuilder.models.sqla.interface import SQLAInterface
        from ..models import {{view.model.name|lower}}
        {%if view.actions%}
        from flask_appbuilder import action
        import flask
        {%endif%}

        {%for r in view.related_views%}
        from .{{r}} import {{r}}View
        {%endfor%}

        # Generated by FABViewCodeGenerator from {{view.model.name}}
        class {{view.name}}View({{view.mixins|join(',')}}):
            {%if view.description%}''' {{view.description}} '''{%endif%}
            datamodel = SQLAInterface({{view.model.name|lower}}.{{view.model.name}})
            list_columns = [{%for c in view.list_columns%}"{{c}}",{%endfor%}]
            show_columns = [{%for c in view.show_columns%}"{{c}}",{%endfor%}]
            edit_columns = [{%for c in view.edit_columns%}"{{c}}",{%endfor%}]
            add_columns =   [{%for c in view.add_columns%}"{{c}}",{%endfor%}]
            related_views = [{%for v in view.related_views%}{{v}}View,{%endfor%}]


            {% for action in view.actions %}
            @action("{{action.name}}", "{{action.title}}", "{{action.confirmation}}", "{{action.icon}}", multiple={{action.multiple}}, single={{action.single}})
            def {{action.name}}(self, item: {{view.model.name|lower}}.{{view.model.name}}):
                # Your action code here
                return flask.current_app.extensions['actions']['{{action.name}}'](item)
            {% endfor %}
        """

    init_views_template: str = """
        {%for view in views%}
        from .{{view.name}} import {{view.name}}View
        {%endfor%}
        import flask
        def init_app(app:flask.Flask):
            appbuilder = app.extensions.get("appbuilder")
            if not appbuilder:
                return
            {%for v in views%}
            appbuilder.add_view({{v.name}}View, "{{v.name}}", icon="{{v.icon}}", category="{{v.category}}")
            {%endfor%}
        """

    def gen_view(self, v: FABView) -> str:
        return Template(textwrap.dedent(self.template)).render(view=v)

    def generate(self, inp: list[FABView]) -> list[FilesystemModel]:
        files: list[FilesystemModel] = []
        for v in inp:
            files.append(
                FilesystemModel(
                    name=v.name + " FABView",
                    path=f"{v.name}.py",
                    content=self.gen_view(v),
                )
            )
        files.append(
            FilesystemModel(
                name="Initialize Views",
                path="__init__.py",
                content=Template(textwrap.dedent(self.init_views_template)).render(
                    views=inp,
                ),
            )
        )
        return files


class ActionCodeGenerator(Generator[list[Action], list[FilesystemModel]]):
    template: str = """
        def {{action.name}}(self, item):
        """

    def generate(self, inp: list[Action]) -> list[FilesystemModel]:
        return [
            # FilesystemModel(
            #     name="Action File",
            #     path="actions.py",
            #     content="\n".join([self.template.format(a) for a in inp]),
            # )
        ]


class FlaskCodeGenerator(Generator[FlaskApp, list[FilesystemModel]]):
    sqla_codegen: SQLAModelCodeGenerator = SQLAModelCodeGenerator()
    fab_view_codegen: FABViewCodeGenerator = FABViewCodeGenerator()
    action_codegen: ActionCodeGenerator = ActionCodeGenerator()
    load_modules_template: str = textwrap.dedent(
        """
        import flask
        from . import {%for module in app.modules%}{{module.name}}{%if not loop.last%},{%endif%}{%endfor%}

        def init_app(app: flask.Flask) -> None:
        {%for module in app.modules%}
            {{module.name}}.init_app(app)
        {%endfor%}
    """
    ).lstrip()

    def render_modules(self, app: FlaskApp) -> str:
        return Template(self.load_modules_template).render(app=app)

    load_extensions_template: str = textwrap.dedent(
        """
        import flask
        from . import {%for extension in app.extensions%}{{extension.name}}{%if not loop.last%},{%endif%}{%endfor%}

        def init_app(app: flask.Flask) -> None:
        {%for extension in app.extensions%}
            {{extension.name}}.init_app(app)
        {%endfor%}
        """
    ).lstrip()

    def render_extensions(self, app: FlaskApp) -> str:
        return Template(self.load_extensions_template).render(app=app)

    init_module_template: str = textwrap.dedent(
        """
    import flask 

    from . import models, views

    def init_app(app:flask.Flask) -> None:
        ''' Initialize the {{module.name}} module. '''

        models.init_app(app)
        views.init_app(app)
    """
    ).lstrip()

    def render_init_module(self, module: Module) -> str:
        return Template(self.init_module_template).render(module=module)

    module_prefix: str = "modules/"
    extension_prefix: str = "extensions/"

    source_files: list[FilesystemModel] = Field(
        title="Source Directory",
        description="""
        Which directory to use for source files. 
        These files will be rendered into the build dir
        TODO: Allow S3, GCS, FTP, etc. as build directories.
        """,
        example=[
            FilesystemModel(
                name="app_py",
                path="myapp/app.py",
                content="""
                    import flask
                    app = flask.Flask(__name__)
                    """,
            ),
            FilesystemModel(
                name="config_py",
                path="myapp/config.py",
                content="""
                    SECRET_KEY='abcdfadsf'
                    """,
            ),
        ],
        default=[
            FilesystemModel(
                name="app_py",
                path="app.py",
                content=textwrap.dedent(
                    """
                    import flask
                    app = flask.Flask(__name__)
                    """
                ).lstrip(),
            ),
            FilesystemModel(
                name="config_py",
                path="config.py",
                content=textwrap.dedent(
                    """
                    SECRET_KEY='abcdfadsf'
                    """
                ).lstrip(),
            ),
        ],
    )

    def generate(self, inp: FlaskApp) -> list[FilesystemModel]:
        modules_files: list[FilesystemModel] = []
        for module in inp.modules:
            sqla_model_files: list[FilesystemModel] = [
                FilesystemModel(
                    name=f.name,
                    content=f.content,
                    path=self.module_prefix + module.name + "/models/" + f.path,
                )
                for f in self.sqla_codegen(module.models)
            ]
            fab_view_files: list[FilesystemModel] = [
                FilesystemModel(
                    name=f.name,
                    content=f.content,
                    path=self.module_prefix + module.name + "/views/" + f.path,
                )
                for f in self.fab_view_codegen(module.views)
            ]
            action_files: list[FilesystemModel] = self.action_codegen(module.actions)
            modules_files += sqla_model_files + fab_view_files + action_files
            modules_files.append(
                FilesystemModel(
                    path=self.module_prefix + module.name + "/__init__.py",
                    name=f"Initialize {module.name} Module",
                    content=self.render_init_module(module),
                )
            )
        modules_files.append(
            FilesystemModel(
                path=self.module_prefix + "__init__.py",
                name=f"Initialize Modules: {[m.name for m in inp.modules]}",
                content=self.render_modules(inp),
            ),
        )
        extensions_files: list[FilesystemModel] = [
            FilesystemModel(
                path=self.extension_prefix + "__init__.py",
                name=f"Initialize Extensions: {[m.name for m in inp.extensions]}",
                content=self.render_extensions(inp),
            ),
        ]

        modules_files.append(
            FilesystemModel(
                path="__init__.py",
                name=f"Initialize App: {inp.name}",
                content=f"'''Initialize App: {inp.name}'''",
            )
        )
        return modules_files + extensions_files + self.source_files
