import flask
from flask.cli import AppGroup
from typing import Any
import click

EXTENSION_NAME = "gpt"


def get_current_ai() -> Any:
    app = flask.current_app
    ai = app.extensions[EXTENSION_NAME]
    return ai


def get_or_create_ai() -> Any:
    from . import coder

    if EXTENSION_NAME not in flask.current_app.extensions:
        flask.current_app.extensions[EXTENSION_NAME] = coder.create_ai(
            flask.current_app.config["OPENAI_API_KEY"]
        )

    ai = get_current_ai()
    return ai


ai_cli = AppGroup("ai", help="AI commands.")


@ai_cli.command("ask")  # type: ignore
@click.argument("prompt")
def ask_ai(prompt: str) -> None:
    """Ask the AI a question."""
    ai = get_or_create_ai()
    response = ai.ask(prompt)  # type: ignore
    click.echo(f"{prompt}\n{response}")


def init_app(app: flask.Flask) -> None:
    api_key = app.config.get("OPENAI_API_KEY")
    if not api_key:
        return
    app.cli.add_command(ai_cli)
