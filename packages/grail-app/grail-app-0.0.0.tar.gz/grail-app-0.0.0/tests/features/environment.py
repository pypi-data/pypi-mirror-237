import os
import tempfile
import flask
from behave import fixture, use_fixture  # type: ignore [import]

# grail is the sample application we want to test
from grail.app import create_app


@fixture
def flaskr_client(context, *args, **kwargs):  # type: ignore [no-untyped-def]
    app: flask.Flask = create_app()
    context.db, app.config["DATABASE"] = tempfile.mkstemp()
    app.testing = True
    context.client = app.test_client()

    yield context.client
    # -- CLEANUP:
    os.close(context.db)
    os.unlink(app.config["DATABASE"])


@fixture
def temp_dir(context, *args, **kwargs):  # type: ignore [no-untyped-def]
    with tempfile.TemporaryDirectory() as td:
        context.temp_dir = td
        yield context.temp_dir


def before_feature(context, feature):  # type: ignore [no-untyped-def]
    # -- HINT: Recreate a new flaskr client before each feature is executed.
    use_fixture(flaskr_client, context)
    use_fixture(temp_dir, context)

    context.create_app = create_app
    print(f"Running feature {feature}")
