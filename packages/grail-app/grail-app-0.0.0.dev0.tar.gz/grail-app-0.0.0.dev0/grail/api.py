import flask
from grail.codegen.fab_app import (
    FlaskCodeGenerator,
    SQLAModelCodeGenerator,
)
from grail.codegen.filesystem import (
    FileLoader,
    FileDumper,
    FilesystemFormatter,
)
from grail.modules import lowcode

from grail.codegen import fab_app
import pathlib
from typing import Any


import pathlib


from grail.codegen.base import Function
from flask.cli import ScriptInfo
import flask, pathlib


def load_app_from_path(app_path: pathlib.Path) -> flask.Flask:
    info = ScriptInfo(app_import_path=f"{app_path / 'app.py'}:create_app()")
    fapp: flask.Flask = info.load_app()
    return fapp


FILES = [
    "config.py",
    "app.py",
    "extensions/sqlalchemy.py",
    "extensions/appbuilder.py",
    "extensions/gateway.py",
    # "extensions/gpt.py",
]

file_loader = FileLoader(base_path=str(pathlib.Path(__file__).parent))
sqla_codegen = SQLAModelCodeGenerator()
flask_codegen = FlaskCodeGenerator(
    sqla_codegen=sqla_codegen, source_files=file_loader(FILES)
)
formatter = FilesystemFormatter()
generator = flask_codegen >> formatter


load_app = Function(func=load_app_from_path)


def inderpret_app(app: fab_app.FlaskApp, build_path: pathlib.Path) -> flask.Flask:
    compiler = FileDumper(build_dir=str(build_path))
    return (generator >> compiler >> load_app)(app)


def create_app(specpath: pathlib.Path, build_path: pathlib.Path) -> flask.Flask:
    app_model = fab_app.FlaskApp.from_yaml(specpath.read_text())
    print(f"loaded {app_model.name} from {specpath}")

    build_path.mkdir(parents=True, exist_ok=True)
    app: flask.Flask = inderpret_app(app_model, build_path=build_path)
    print(f"Loaded app {app.name} from {app.root_path}")
    return app


def launch_app(app: Any, gateway: Any) -> None:
    prefix = f"/apps/{app.name}"
    flask_app = fab_app.FlaskApp.from_orm(app)

    app_dir = pathlib.Path("/tmp/launched_apps") / app.name
    app_dir.mkdir(parents=True, exist_ok=True)
    compiler = generator >> FileDumper(build_dir=str(app_dir))

    app_path = compiler(flask_app)
    app_uri = str(app_path / "app.py") + ":create_app()"
    gateway.mounts[prefix] = app_uri
    import sys

    if prefix in gateway.instances:
        del gateway.instances[prefix]

    # remove modules created previously by this app, so that they are re-imported
    # when the new app starts
    if app.name in sys.modules:
        del sys.modules[app.name]
        for m in filter(lambda x: x.startswith(app.name + "."), sys.modules.keys()):
            del sys.modules[m]


def to_model(app: fab_app.FlaskApp) -> lowcode.models.App:
    extension_objects: list[lowcode.models.Extension] = [
        lowcode.models.Extension(
            name=e.name,
            description=e.description,
        )
        for e in app.extensions
    ]
    module_objects: dict[str, lowcode.models.Module] = {}
    for module in app.modules:
        model_objects: dict[str, lowcode.models.SQLAModel] = {
            model.name: lowcode.models.SQLAModel(
                name=model.name,
                tablename=model.tablename,
                description=model.description,
                columns=[
                    lowcode.models.SQLAColumn(
                        name=column.name,
                        description=column.description,
                        datatype=column.datatype,
                    )
                    for column in model.columns
                ],
            )
            for model in module.models
        }

        module_objects[module.name] = lowcode.models.Module(
            name=module.name,
            description=module.json(),
            models=list(model_objects.values()),
            views=[
                lowcode.models.FABView(
                    name=view.name,
                    description=view.description,
                    model=model_objects[view.model.name],
                )
                for view in module.views
            ],
        )

    app_model = lowcode.models.App(
        name=app.name,
        description=app.description,
        extensions=extension_objects,
        modules=list(module_objects.values()),
    )

    return app_model


if __name__ == "__main__":
    import sys
    from pathlib import Path

    if len(sys.argv) < 2:
        print("Usage: python -m grail.generate_app <src_path> <gen_dir> ...")
        sys.exit(1)

    create_app(Path(sys.argv[1]), Path(sys.argv[2]))
