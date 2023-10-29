import os,sys
import flask
from connexion import FlaskApp
from grail.extensions import settings
import pathlib

HERE = pathlib.Path(__file__).parent
SPEC_DIR = HERE / 'spec'

capp = FlaskApp(__name__, specification_dir=str(SPEC_DIR)) 

app:flask.Flask = capp.app # type: ignore

settings.init_app(app)

spec_files = (f for f in SPEC_DIR.iterdir() if f.is_file() and f.suffix in ['.yml','.yaml'])

for f in spec_files:
    spec = f.stem
    spec_file = SPEC_DIR / f"{spec}.yaml"
    capp.add_api(str(spec_file),base_path=f"/{spec}")


@app.route("/")
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()