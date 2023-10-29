from grail.codegen.fab_app import SQLAModel
from grail.objects import flask_app

from grail.codegen.filesystem import FileDumper
from grail.codegen.base import Generator
from grail.codegen.fab_app import FlaskApp, Module
from grail.api import generator, load_app
import flask, pathlib

FAB_MODELS = {
    "ViewMenu",
    "User",
    "Permission",
    "Role",
    "RegisterUser",
    "PermissionView",
}

import pytest

app_models = [flask_app.departmentsapp, flask_app.lowcodeapp]


@pytest.mark.parametrize("app_model", app_models)
def test_generate_models(tmp_path: pathlib.Path, app_model: FlaskApp) -> None:
    app_root: pathlib.Path = tmp_path / app_model.name
    app_root.mkdir(parents=True, exist_ok=True)

    compiler: Generator[FlaskApp, flask.Flask] = (
        generator >> FileDumper(build_dir=str(app_root)) >> load_app
    )

    models: list[SQLAModel] = []
    for module in app_model.modules:
        models.extend(module.models)

    app: flask.Flask = compiler(app_model)
    registered_models = set(m for m in get_registered_models(app))
    generated_models: set[str] = {m.name for m in models}
    assert registered_models == generated_models
    # assert registered_models - generated_models == FAB_MODELS
    assert app.name == f"{app_model.name}.app"
    assert app.root_path == str(app_root)  # TODO fix this, it's broken for grail app
    assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:"


def get_registered_models(app: flask.Flask) -> dict[str, "Any"]:
    Base = app.extensions["sqlalchemy"].db.Model
    models = {m.class_.__name__: m.class_ for m in Base.registry.mappers}
    return models
