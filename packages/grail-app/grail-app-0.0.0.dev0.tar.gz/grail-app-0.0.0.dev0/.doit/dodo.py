# type: ignore

import doit
import glob
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))
PACKAGE = "grail"
GEN_DIR = ROOT_DIR / "instance/generated_apps"
OBJ_DIR = ROOT_DIR / "grail"/"objects"
SCHEMA_DIR = ROOT_DIR / "grail/objects/schemas"

SCHEMAS = [
    "grail.codegen.fab_app:FlaskApp",
    "grail.codegen.application:Application",
]
MODULES = [
   # "grail.objects.Module.blog:Blog",
   # "grail.objects.Module.departments:Departments",
    "grail.objects.Module.lowcode:LowCode",
]
APPS = [
    "lowcode",
  #  "blog",
  #  "departments",
]

DOIT_CONFIG = {
    # "continue": True,
    #  "reporter": "json",
    "verbosity": 2,
    "backend": "sqlite3",
}


def to_yaml(object_path: str, path: str, *args, **kwargs):
    import importlib, pathlib, os
    os.chdir(ROOT_DIR)
    try:
        module_name, object_name = object_path.split(":")
        mod = importlib.import_module(module_name, package='grail')
        obj = getattr(mod, object_name)
        y = obj.to_yaml()
        pathlib.Path(path).write_text(y)
        print(f"Wrote {object_name} to {path}")
    except:
        print(f"Failed to write {object_name} to {path}")
        raise
    finally:
        os.chdir(doit.get_initial_workdir())
    return True


def to_yaml_schema(object_path: str, path: str, *args, **kwargs):
    import importlib, pathlib,os
    try:
        module_name, object_name = object_path.split(":")
        mod = importlib.import_module(module_name, package=None)
        obj = getattr(mod, object_name)
        y = obj.schema_yaml()
        pathlib.Path(path).write_text(y)
        print(f"Wrote {object_name} to {path}")
    except:
        print(f"Failed to write {object_name} to {path}")
        raise
    finally:
        os.chdir(doit.get_initial_workdir())
    return True


def task_schemas():
    yield {
        "name": SCHEMA_DIR,
        "actions": [f"mkdir -p {SCHEMA_DIR}"],
        "targets": [SCHEMA_DIR],
        "clean": True,
    }

    for model in SCHEMAS:
        mod_path, mod_obj = model.split(":")
        mod_yaml = SCHEMA_DIR / f"{mod_obj}.yaml"
        yield {
            "name": mod_yaml,
            "file_dep": [f"{ROOT_DIR}/grail/codegen/fab_app.py"],
            "actions": [
                (
                    to_yaml_schema,
                    [model, mod_yaml],
                    {},
                ),
            ],
            "targets": [mod_yaml],
            "clean": True,
        }


@doit.create_after(executed="schemas")
def task_datamodel():
    for schema_file in glob.glob(f"{SCHEMA_DIR}/*.yaml"):
        schema_path = Path(schema_file)
        schema_name = schema_path.stem
        schema_python = SCHEMA_DIR / f"{schema_name}.py"
        yield {
            "name": schema_python,
            "file_dep": [schema_path],
            "actions": [
                f"datamodel-codegen --input {schema_path} --output {schema_python} --input-file-type jsonschema"
            ],
            "targets": [schema_python],
            "clean": True,
        }


@doit.create_after(executed="schemas")
def task_objects():
    """Convert the objects to yaml"""
    ext_yaml = f"{OBJ_DIR}/extensions.yaml"
    ext_path = "grail.objects.extensions:extensions"
    yield {
        "name": ext_yaml,
        "file_dep": [f"{OBJ_DIR}/extensions.py"],
        "actions": [
            (
                to_yaml,
                [ext_path, ext_yaml],
                {},
            ),
        ],
        "targets": [ext_yaml],
        "clean": True,
    }

    for m in MODULES:
        _, mod_obj = m.split(":")
        mod_yaml = f"{OBJ_DIR}/Module/{mod_obj.lower()}.yaml"
        yield {
            "name": mod_yaml,
            "file_dep": [f"{OBJ_DIR}/Module/{mod_obj.lower()}.py"],
            # "actions": [f"python -m grail.objects.Module {m} {mod_yaml}"],
            "actions": [
                (
                    to_yaml,
                    [m, mod_yaml],
                    {},
                ),
            ],
            "targets": [mod_yaml],
            "clean": True,
        }
    for app in APPS:
        app_yaml = f"{OBJ_DIR}/FlaskApp/{app}.yaml"
        yield {
            "name": app_yaml,
            "file_dep": [
                ext_yaml,
                f"{OBJ_DIR}/Module/{app}.yaml",
                SCHEMA_DIR / "FlaskApp.yaml",
            ],
            "actions": [
                (
                    to_yaml,
                    [f"grail.objects.FlaskApp:{app}", app_yaml],
                    {},
                ),
            ],
            "targets": [app_yaml],
            "clean": True,
        }


from grail.codegen.fab_app import FABView, FlaskApp, SQLAModel, FilesystemModel
from pathlib import Path


def gen_sqlamodel(models: list[SQLAModel], gen_path: Path):
    from grail.codegen.fab_app import SQLAModel, SQLAModelCodeGenerator

    model_files: list[FilesystemModel] = SQLAModelCodeGenerator().generate(models)

    files_dict: dict[str, str] = {
        str(gen_path / f.path): f.content for f in model_files
    }
    generated_files.update(files_dict)
    gen_path.mkdir(parents=True, exist_ok=True)
    return files_dict


def gen_fabviews(view: FABView, path: Path):
    from grail.codegen.fab_app import FABViewCodeGenerator

    view_code: str = FABViewCodeGenerator().gen_view(view)

    Path(path).write_text(view_code)
    return view_code


loaded_apps: dict[str, FlaskApp] = {}
generated_files: dict[str, str] = {}


@doit.create_after(executed="objects")
def task_parse():
    """Parse and validate all object files"""

    def do_parse(app_yaml: Path, *args, **kwargs):
        app = FlaskApp.from_yaml(app_yaml.read_text())
        loaded_apps[app_yaml] = app
        return app.dict()

    for app_file in glob.glob(f"{OBJ_DIR}/FlaskApp/*.yaml"):
        app_yaml = Path(app_file)
        yield {
            "name": app_file,
            "file_dep": [app_yaml],
            "actions": [(do_parse, [app_yaml])],
            "clean": True,
        }


@doit.create_after(executed="models")
def task_write():
    """Write all files generated by the generate task"""

    def write_file(path, content, *args, **kwwargs):
        Path(path).write_text(content)
        print(f"MODEL: file {path}")

    for path, content in generated_files.items():
        yield {
            "name": path,
            "targets": [path],
            # "file_dep": [app_yaml],
            "actions": [(write_file, [path, content])],
            "clean": True,
        }


@doit.create_after(executed="parse")
def task_models():
    """Generate the sqlalchemy models from the model"""
    for app_yaml, app in loaded_apps.items():
        for module in app.modules:
            module_path: Path = Path(GEN_DIR) / app.name
            models_path = module_path / "models"

            yield {
                "name": models_path,
                "actions": [
                    (
                        gen_sqlamodel,
                        [],
                        {"models": module.models, "gen_path": models_path},
                    )
                ],
                "clean": True,
                "file_dep": [app_yaml],
            }


@doit.create_after(executed="models")
def task_write_models():
    """Generate the sqlalchemy models from the model"""
    for app_yaml, app in loaded_apps.items():
        for module in app.modules:
            module_path: Path = Path(GEN_DIR) / app.name 
            models_path = module_path / "models"
            yield {
                "name": models_path,
                "targets": [models_path],
                "file_dep": [app_yaml],
                "actions": [f"mkdir -p {models_path}"],
                "clean": True,
            }
            yield {
                "name": models_path / "__init__.py",
                "actions": [
                    (
                        gen_sqlamodel,
                        [],
                        {"models": module.models, "gen_path": models_path},
                    )
                ],
                "clean": True,
                "file_dep": [app_yaml],
            }


@doit.create_after(executed="parse")
def task_generate():
    """Generate the app from the model"""

    for app_yaml, app in loaded_apps.items():
        for module in app.modules:
            module_path: Path = Path(GEN_DIR) / app.name
            views_path = module_path / "views"
            yield {
                "name": views_path,
                "targets": [views_path],
                "file_dep": [app_yaml],
                "actions": [f"mkdir -p {views_path}"],
                "clean": True,
            }
            yield {
                "name": views_path / "__init__.py",
                "targets": [views_path / "__init__.py"],
                "file_dep": [app_yaml],
                "actions": [f"touch {views_path}/__init__.py"],
                "clean": True,
            }
            for view in module.views:
                view_path = views_path / f"{view.name}.py"
                yield {
                    "name": view_path,
                    "actions": [(gen_fabviews, [], {"view": view, "path": view_path})],
                    "clean": True,
                    "file_dep": [app_yaml],
                }


def _task_mypy():
    yield {
        "name": f"mypy {GEN_DIR}/{app}/",
        "actions": [
            f"mypy --warn-unused-configs --no-strict-optional --strict {GEN_DIR}/{app}/"
        ],
    }


def _task_pytest():
    """Run all the tests for the project"""
    for app in APPS:
        yield {
            "name": f"pytest {GEN_DIR}/{app}/app.py",
            "actions": ["pytest"],
            # "targets": [f"grail/objects/{app}.yaml"],
            "file_dep": [f"{GEN_DIR}/{app}/app.py"],
        }


def task_black():
    """Run black formatter on code"""
    return {
        "actions": [f"black {PACKAGE} {ROOT_DIR/'tests'}"],
    }


# def task_mypy():
#     """Run mypy type checker on code"""
#
#     return {
#         "actions": [
#             f"mypy --warn-unused-configs --no-strict-optional --strict {PACKAGE}"
#         ],
#     }
