import sys

if False and sys.version[:4] not in ("3.11", "3.12"):
    APT_INSTALL = """
    sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev liblzma-dev
    """
    PY_INSTALL = """
    curl https://pyenv.run | bash
    pyenv install 3.12
    pyenv global 3.12.0
    """

    print("you need python 3.11 but currently have " + sys.version)
    print("Install python build dependancies: " + APT_INSTALL)
    print("Install python3.12: " + PY_INSTALL)
    exit(1)

from flask.cli import FlaskGroup
import click
from .app import create_app


@click.group(cls=FlaskGroup, create_app=create_app)
def run() -> None:
    """Management script for the application."""


if __name__ == "__main__":
    run()
