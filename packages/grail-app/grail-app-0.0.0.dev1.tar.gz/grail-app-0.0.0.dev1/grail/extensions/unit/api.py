
import dataclasses
from typing import Optional
import flask
import subprocess, sys, json
from .controller import get_controller
from pathlib import Path

@dataclasses.dataclass
class UnitApplication:
    type:str="python"
    user:Optional[str]=None
    path:list[str] = dataclasses.field(default_factory=list) 
    module:str="app"
    environment:dict[str,str]= dataclasses.field(default_factory=dict)
    processes:int=1
    threads:int=1
    working_directory:Optional[str]=None
    callable:str='app'
    stderr:Optional[str]=None
    stdout:Optional[str]=None
    prefix:Optional[str]=None
    home:Optional[str]=None
    

@dataclasses.dataclass
class FlaskAppFile:
    name: str
    content: str

@dataclasses.dataclass
class FlaskApp:
    name: str
    files: list[FlaskAppFile] = dataclasses.field(default_factory=list)
    user: Optional[str] = None


def get_dirname(flaskapp:FlaskApp)->str: 
    return f"{flaskapp.name}"

def get_appdir(flaskapp:FlaskApp)->Path:
    path =  Path(flask.current_app.config['APPS_DIR'])
    return path / get_dirname(flaskapp)

def get_venvdir(flaskapp:FlaskApp)->Path:
    path = Path(flask.current_app.config['VENV_DIR'])
    return path / get_dirname(flaskapp)

def write_app_files(flaskapp:FlaskApp,)->Path:
    appdir = get_appdir(flaskapp)
    if not appdir.exists():
        appdir.mkdir(parents=True, exist_ok=True)

    # Create the flask app files
    for file in flaskapp.files:
        (appdir / file.name).write_text(file.content)
    
    return appdir

def create_logdir(flaskapp:FlaskApp)->Path:
    app_log_dir = Path(flask.current_app.config['APPS_LOGS_DIR']) / get_dirname(flaskapp)
    if not app_log_dir.exists():
        app_log_dir.mkdir(parents=True, exist_ok=True)
    return app_log_dir

def create_venv(flaskapp:FlaskApp)->Path:
    path =  Path(flask.current_app.config['VENV_DIR'])
    venv_dir = path / get_dirname(flaskapp)
    executable = flask.current_app.config['UNIT_PYTHON_BIN']
    if not venv_dir.exists():
        venv_dir.parent.mkdir(parents=True, exist_ok=True)
        subprocess.call([executable, "-m", "venv", venv_dir])

    return venv_dir

def install_global_requirements(flaskapp:FlaskApp)->Path:
       # Install the default requirements

    venv_dir = get_venvdir(flaskapp)
    py_exe = str(venv_dir / "bin" / "python")

    subprocess.call(
            [
                py_exe,
                "-m",
                "pip",
                "install",
                "--upgrade", "pip",
            ]
    )
    pyproject = Path(flask.current_app.root_path).parent / "pyproject.toml"
    setup_py = Path(flask.current_app.root_path).parent / "setup.py"
    if pyproject.exists() or setup_py.exists():
        subprocess.call(
                [
                    py_exe,
                    "-m",
                    "pip",
                    "install",
                    "-e",
                    str(pyproject.parent),
                ]
            )
        flask.current_app.logger.info(f"Installed {pyproject.parent} into {venv_dir}")
    return pyproject.parent

def install_flask_requirements(flaskapp:FlaskApp)->Optional[Path]:

    venv_dir = get_venvdir(flaskapp)
    py_exe = str(venv_dir / "bin" / "python")
 
    requirements_file = get_appdir(flaskapp) / "requirements.txt"
    if requirements_file.exists():
        subprocess.call(
            [
                py_exe,
                "-m",
                "pip",
                "install",
                "-r",
                str(requirements_file),
            ]
        )
        return requirements_file
    return None

def setup_routing(appname:str,prefix:Optional[str])->str:
    # Get all the existing routes
    resp = get_controller().get("/config/routes")
    if not resp.ok:
        return f"Error while getting routes: {resp.text}"
    routes_array = resp.json()
    if 'main' in routes_array:
        routes_array = routes_array['main']

    # Update the route or add it if it doesn't exist
    new_route_uri = f"{prefix.rstrip('/')}/*" if prefix else None

    # Remove any existing routes for this app or with the same uri
    new_routes = []
    for route in routes_array:
        app = route["action"].get("pass",'').removeprefix("applications/")
        if app == appname:
            continue
        route_uri = route["match"]["uri"]
        if route_uri == new_route_uri:
            continue
        new_routes.append(route)
    
    # Add the new route to the beginning of the routes
    if new_route_uri:
        new_routes += [
            {
                "action": {"pass": f"applications/{appname}"},
                "match": {"uri": new_route_uri},
            }
        ]
    routes_array = new_routes
    # Order routes to ensure the most specific routes are first
    routes_array = list(reversed(sorted(routes_array, key=lambda x: len(x["match"]["uri"]))))

    routes_obj = {"main": routes_array}
    route_data = json.dumps(routes_obj)
    resp = get_controller().put("/config/routes/", data=route_data)
    if not resp.ok:
        return f"Error while updating route: {resp.text}: {route_data}"
    
    return ""

def get_unit_app(flaskapp:FlaskApp,prefix:str)->UnitApplication:
    appname = get_dirname(flaskapp)
    appdir = get_appdir(flaskapp)
    app_py = appdir / "app.py"
    if not app_py.exists():
        raise RuntimeError(f"app.py not found at {app_py}")

    venvdir = get_venvdir(flaskapp)
    if not venvdir.exists():
        raise RuntimeError(f"virtual env not found at {venvdir}")

    app_log_dir = Path(flask.current_app.config['APPS_LOGS_DIR']) / appname
    unit_app =UnitApplication(
        user=flaskapp.user,
        path=[str(appdir)],
        working_directory=str(appdir),
        stderr=str(app_log_dir /"stderr.log"),
        stdout=str(app_log_dir /"stdout.log"),
        prefix=prefix,
        home=str(venvdir),
    )
    return unit_app

def shutdown_application(name:str)->str:
    
    error = setup_routing(name,None)
    if error:
        return error
    
    resp = get_controller().delete(
        f"/config/applications/{name}"
    )

    if not resp.ok:
        return (f"Error while shutting down app {name}: {resp.text}")
    
    return ''

def launch_application(flaskapp:FlaskApp,prefix:str)->str:

    # Create a new flask app using the contents of the flaskapp columns
    unit_app = get_unit_app(flaskapp,prefix=prefix)
    appname = get_dirname(flaskapp)

    data = json.dumps(dataclasses.asdict(unit_app))
    resp = get_controller().put(
        f"/config/applications/{appname}", data=data
    )
    if not resp.ok:
        return (f"Error while launching app: {resp.text}: {data}")

    return ''

def setup_listener()->str:
    port = flask.current_app.config['APPS_PORT']
    listener_obj = {f"*:{port}": {"pass": "routes/main"}}
    listener_data = json.dumps(listener_obj)
    resp = get_controller().put("/config/listeners/", data=listener_data)
    if not resp.ok:
        return f"Error while updating listeners: {resp.text}: {listener_data}"
    return ''

def launch(flaskapp: FlaskApp,prefix:str)->dict[str,str]:
    """Launch a FlaskApp using Unit."""

    error = launch_application(flaskapp,prefix=prefix)
    if error:
        return {'error':error}

    error = setup_routing(flaskapp.name,prefix=prefix)
    if error:
        return {'error':error}

    error = setup_listener()
    if error:
        return {'error':error}
    
    launched_path = prefix.rstrip('/') + "/"
    launched_host = '0.0.0.0'
    launched_port = flask.current_app.config['APPS_PORT']
    launched_protocol = 'http'
    launched_url = f"{launched_protocol}://{launched_host}:{launched_port}{launched_path}"
    return {'url':launched_url}




def init_app(app:flask.Flask)->None:
    app.config.setdefault('APPS_DIR',Path(app.instance_path) / "apps")
    app.config.setdefault('APPS_LOGS_DIR',Path(app.instance_path) / "logs")
    app.config.setdefault('VENV_DIR',Path(app.instance_path) / "venvs")
    app.config.setdefault('APPS_PORT',8080)
    app.config.setdefault('UNIT_PYTHON_BIN',sys.executable)
