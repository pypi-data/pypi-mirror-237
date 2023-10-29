from typing import Any, Generator
import pytest
import flask
import flask.testing


@pytest.fixture()
def app() -> Generator[flask.Flask, None, None]:
    from grail.app import (
        create_app,
    )  # Do not import at top level, otherwise all sqla models will be registered always

    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app: flask.Flask) -> flask.testing.FlaskClient:
    return app.test_client()


@pytest.fixture()
def runner(app: flask.Flask) -> flask.testing.FlaskCliRunner:
    return app.test_cli_runner()
