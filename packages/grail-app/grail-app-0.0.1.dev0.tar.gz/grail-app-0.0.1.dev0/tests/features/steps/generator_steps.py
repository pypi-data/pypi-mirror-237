# type: ignore
from behave import given, when, then
from pyrsistent import b
from grail.codegen.fab_app import (
    FlaskApp,
    Extension,
    SQLAModel,
    Module,
)
from grail.codegen.filesystem import FileDumper
import flask
from operator import itemgetter
from grail.objects.flask_app import MODULES, EXTENSIONS, SQLA_MODELS
from grail import generate_app

from behave import register_type, given
import parse


# -- TYPE CONVERTER: For a simple, positive integer number.
@parse.with_pattern(r"\D+")
def parse_extensions(text) -> list[Extension]:
    names: list[str] = text.split(",")
    extensions: list[Extension] = []
    try:
        extensions = list(itemgetter(*names)(EXTENSIONS))
    except KeyError as e:
        pass  # raise KeyError(f"Extensions must be one of {list(EXTENSIONS.keys())}: {e}")
    return extensions


@parse.with_pattern(r"\D+")
def parse_modules(text) -> list[Module]:
    names: list[str] = text.split(",")
    modules: list[Module] = []
    try:
        modules = list(itemgetter(*names)(MODULES))
    except KeyError as e:
        pass  # raise KeyError(f"Modules must be one of {list(MODULES.keys())}: {e}")
    return modules


@parse.with_pattern(r"\D+")
def parse_models(text) -> list[SQLAModel]:
    names: list[str] = text.split(",")
    models: list[SQLAModel] = []
    try:
        models = list(itemgetter(*names)(SQLA_MODELS))
    except KeyError as e:
        pass  # raise KeyError(f"SQLAModels must be one of {list(SQLA_MODELS.keys())}: {e}")
    return models


# -- REGISTER TYPE-CONVERTER: With behave
register_type(Modules=parse_modules)
register_type(Extensions=parse_extensions)
register_type(Models=parse_models)


@given(
    'a new FlaskApp spec "{name}" with modules {modules:Modules} and extensions {extensions:Extensions}'
)
def step_given_a_flask_spec(
    context, name: str, modules: list[str], extensions: list[str] = []
) -> None:
    context.app_model = FlaskApp(name=name, modules=modules, extensions=extensions)


@when("I generate the flask app")
def step_generate_the_app(context) -> None:
    try:
        compiler = FileDumper(build_dir=context.temp_dir)
        app = (generate_app.generator >> compiler >> generate_app.load_app)(
            context.app_model
        )
        context.app_instance = app
        context.model_is_valid = True

    except ValueError as e:
        print(e)
        context.model_is_valid = False
        raise
    except Exception as e:
        print(e)
        context.model_is_valid = False
        raise
    assert context.model_is_valid, "FlaskApp model is not valid"


@then("The app should have extensions {extensions:Extensions}")
def step_then_the_should_have_extensions(context, extensions) -> None:
    app: flask.Flask = context.app_instance
    for e in extensions:
        assert e.name in app.extensions, f"App does not have extension {e.name}"


@then("The app should have models {models:Models}")
def step_then_the_should_have_models(context, models) -> None:
    app: flask.Flask = context.app_instance

    # for m in models:
    #    assert m.name in app.extensions["sqlamodels"], f"App does not have module {m}"


@then("The app should have modules {modules:Modules}")
def step_then_the_should_have_modules(context, modules) -> None:
    app: flask.Flask = context.app_instance
    # for m in modules:
    #    assert m in app.blueprints, f"App does not have module {m}"
