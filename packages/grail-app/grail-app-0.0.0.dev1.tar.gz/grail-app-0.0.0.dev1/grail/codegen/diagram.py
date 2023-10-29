# type: ignore
import erdantic as erd
from grail.codegen.application import Application
from grail.codegen.fab_app import FlaskAppInterpreter, FlaskApp
from IPython.display import Image
import tempfile
import webbrowser
import sys
import importlib


def draw(cls: type | str) -> Image:
    if isinstance(cls, str):
        module_name, class_name = cls.rsplit(".", 1)
        module = importlib.import_module(module_name)
        cls = getattr(module, class_name)

    with tempfile.NamedTemporaryFile(suffix=".png") as f:
        erd.draw(cls, out=f.name)
        webbrowser.open(f"file://{f.name}")
        i = Image(filename=f.name)
    return i


if __name__ == "__main__":
    cls = sys.argv[1]
    draw(cls)
