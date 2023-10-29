"""Functions handling API endpoints."""
import flask
from open_alchemy import models
import pathlib
import subprocess, sys, json
from grail.extensions.unit import get_controller as controller, model

APPS_DIR = pathlib.Path("/apps")
VENV_DIR = pathlib.Path("/venv")
FlaskApp = models.FlaskApp


def upload_files(id):
    flaskapp = FlaskApp.query.filter_by(id=id).first_or_404()

    file_models = {
        f.filename: models.FlaskAppFile(name=f.filename, content=f.read().decode("utf-8"))
        for f in flask.request.files.getlist("files")
    }
    app_files = {f.name: f for f in flaskapp.files}
    for name,file in file_models.items():
        found_file = app_files.get(name)
        if found_file:
            found_file.content = file.content
        else:
            flaskapp.files.append(file)
    flask.current_app.extensions["sqlalchemy"].db.session.commit()

    return {}, 200


def upload(id):
    flaskapp = FlaskApp.query.filter_by(id=id).first_or_404()

    files = {
        "app_py": flask.request.files.get("app_py"),
        "requirements_txt": flask.request.files.get("requirements_txt"),
        "settings_yaml": flask.request.files.get("settings_yaml"),
    }
    changed = False
    for name, file in files.items():
        if file:
            text = file.read().decode("utf-8")
            setattr(flaskapp, name, text)
            changed = True
    if changed:
        flask.current_app.extensions["sqlalchemy"].db.session.commit()

    return {}, 200


def launch(id):
    """Launch a FlaskApp from the database."""
    flaskapp = FlaskApp.query.filter_by(id=id).first_or_404()
    dirname = f"{flaskapp.id}-{flaskapp.name}"
    appdir = APPS_DIR / dirname
    if not appdir.exists():
        appdir.mkdir(parents=True, exist_ok=True)

    # Create the flask app files
    for file in flaskapp.files:
        (appdir / file.name).write_text(file.content)

    # Create a new virtual environment if it doesn't exist
    venv_dir = VENV_DIR / dirname
    if not venv_dir.exists():
        venv_dir.parent.mkdir(parents=True, exist_ok=True)
        subprocess.call([sys.executable, "-m", "venv", venv_dir])
    
    # Install the default requirements
    subprocess.call(
            [
                str(venv_dir / "bin" / "python"),
                "-m",
                "pip",
                "install",
                "--upgrade pip",
            ]
    )
    pyproject = (flask.current_app.root_path).parent / "pyproject.toml"
    if pyproject.exists():
        subprocess.call(
                [
                    str(venv_dir / "bin" / "python"),
                    "-m",
                    "pip",
                    "install",
                    "-e",
                    str(pyproject.parent),
                ]
            )
        flask.current_app.logger.info(f"Installed {pyproject.parent} into {venv_dir}")
    # Install the requirements.txt
    requirements_file = appdir / "requirements.txt"
    if requirements_file.exists():
        subprocess.call(
            [
                str(venv_dir / "bin" / "python"),
                "-m",
                "pip",
                "install",
                "-r",
                str(requirements_file),
            ]
        )

    # Create a new flask app using the contents of the flaskapp columns
    app_py = appdir / "app.py"
    if not app_py.exists():
        flask.abort(401, f"app.py not found for {dirname}")

    url_prefix = flaskapp.route or f"/{dirname}"

    unit_app = model.ConfigApplicationPython(
        type="python",
        user="root",
        group="root",
        path=[str(appdir), "/app"], #type: ignore
        module="app",
        environment={},
        limits=None,
        processes=1,
        threads=1,
        working_directory=str(appdir),
        callable="app",
        stderr=None,
        stdout=None,
        prefix=url_prefix,
        home=str(venv_dir),
        isolation=None,
        protocol=None,
        targets=None,
        thread_stack_size=16384 * 4,
    )
    data = unit_app.json(exclude_defaults=True, exclude_unset=True, exclude_none=True)
    resp = controller().put(
        f"/config/applications/{flaskapp.id}-{flaskapp.name}", data=data
    )
    if not resp.ok:
        return f"Error while launching app: {resp.text}: {data}", 500

    # Get all the existing routes
    resp = controller().get("/config/routes/main")
    if not resp.ok:
        return f"Error while getting routes: {resp.text}", 500
    routes_array = resp.json()

    # Update the route or add it if it doesn't exist
    new_route_uri = f"{url_prefix}/*"
    exists = False
    for route in routes_array:
        route_uri = route["match"]["uri"]
        if route_uri == new_route_uri:
            route["action"]["pass"] = f"applications/{dirname}"
            exists = True
            break
    if not exists:
        routes_array.append(
            {
                "action": {"pass": f"applications/{dirname}"},
                "match": {"uri": new_route_uri},
            }
        )
    routes_obj = {"main": routes_array}
    route_data = json.dumps(routes_obj)
    resp = controller().put("/config/routes/", data=route_data)
    if not resp.ok:
        return f"Error while updating route: {resp.text}: {route_data}", 500
    
    # Update the flaskapp route in the database
    if url_prefix != flaskapp.route:
        flaskapp.route = url_prefix
        flask.current_app.extensions["sqlalchemy"].db.session.commit()

    return {'url':(url_prefix + "/")}


def load():
    """Load all flask apps from the provided path into the database"""
    filepath = pathlib.Path("/apps")
    apps = []
    for appdir in filepath.iterdir():
        app_py_path: pathlib.Path = appdir / "app.py"
        requirements_txt_path = appdir / "requirements.txt"
        settings_yaml_path = appdir / "settings.yaml"
        app_py = (
            app_py_path.read_text() if app_py_path.exists() else "# Add flask app here"
        )
        requirements_txt = (
            requirements_txt_path.read_text()
            if requirements_txt_path.exists()
            else "flask==2.0.2"
        )
        settings_yaml = (
            settings_yaml_path.read_text()
            if settings_yaml_path.exists()
            else "default:"
        )

        flaskapp = FlaskApp(
            name=appdir.name,
            app_py=app_py,
            requirements_txt=requirements_txt,
            settings_yaml=settings_yaml,
        )
        flask.current_app.extensions["sqlalchemy"].db.session.add(flaskapp)
        apps.append(flaskapp)

    flask.current_app.extensions["sqlalchemy"].db.session.commit()
    flaskapp_dicts = map(lambda flaskapp: flaskapp.to_dict(), apps)
    return list(flaskapp_dicts)


def search():
    """Get all flaskapps from the flask.current_app.extensions['sqlalchemy']."""
    flaskapps = FlaskApp.query.all()
    flaskapp_dicts = map(lambda flaskapp: flaskapp.to_dict(), flaskapps)
    return list(flaskapp_dicts)


def post(body):
    """Save an flaskapp to the flask.current_app.extensions['sqlalchemy']."""
    if FlaskApp.query.filter_by(id=body["id"]).first() is not None:
        return ("FlaskApp already exists.", 400)
    flaskapp = FlaskApp.from_dict(**body)
    flask.current_app.extensions["sqlalchemy"].db.session.add(flaskapp)
    flask.current_app.extensions["sqlalchemy"].db.session.commit()


def get(id):
    """Get an flaskapp from the flask.current_app.extensions['sqlalchemy']."""
    return FlaskApp.query.filter_by(id=id).first_or_404().to_dict()


def patch(body, id):
    """Update an flaskapp in the dayabase."""
    flaskapp = FlaskApp.query.filter_by(id=id).first()
    if flaskapp is None:
        return ("FlaskApp not found.", 404)
    flaskapp.name = body["name"]
    flaskapp.division = body["division"]
    flaskapp.salary = body["salary"]
    flask.current_app.extensions["sqlalchemy"].db.session.commit()
    return 200


def delete(id):
    """Delete an flaskapp from the flask.current_app.extensions['sqlalchemy']."""
    result = FlaskApp.query.filter_by(id=id).delete()
    if not result:
        return ("FlaskApp not found.", 404)
    flask.current_app.extensions["sqlalchemy"].db.session.commit()
    return 200
