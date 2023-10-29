"""
This module contains methods used by the cogapp template engine.
"""
from typing import Any
import jinja2
import json

environment = jinja2.Environment()


def define(g: dict[str, Any]) -> None:
    cog = g["cog"]
    schema = g["schema"]
    exec(cog.previous, g)
    cog.out(cog.previous if cog.inFile == cog.outFile else "")
    g["schema"] = json.load(open(schema))


def readme(schema: str | None = None) -> str:
    """
    return the readme
    """

    return f"""
    # This is the readme for {schema or 'this project'}
    """


def render(model: dict[Any, Any], template: str) -> str:
    """
    render a template given a schema
    """

    return environment.from_string(template).render(**model)
