from grail.codegen.fab_app import FlaskApp, ExtensionsList, Module
from pathlib import Path

ext_yaml = Path(__file__).parent.parent / "extensions.yaml"
extensions = ExtensionsList.from_yaml(ext_yaml.read_text())

module_yamls = [
    Path(__file__).parent.parent / "Module" / f"{m}.yaml"
    for m in ["blog", "departments", "lowcode"]
]

modules = {m.name: m for m in [Module.from_yaml(f.read_text()) for f in module_yamls]}

lowcode = FlaskApp(
    name="lowcode",
    modules=[modules["lowcode"]],
    extensions=extensions.items,
)
blog = FlaskApp(
    name="blog",
    modules=[modules["blog"]],
    extensions=extensions.items,
)
departments = FlaskApp(
    name="departments",
    modules=[modules["departments"]],
    extensions=extensions.items,
)
