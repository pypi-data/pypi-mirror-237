from flask_executor import Executor
from flask_shell2http import Shell2HTTP
import flask


def init_app(app):
    executor = Executor(app)
    shell2http = Shell2HTTP(app=app, executor=executor, base_url_prefix="/commands/")

    for cmd in ["pgadmin", "editor", "api", "git"]:
        shell2http.register_command(
            endpoint=cmd, command_name=f"/venv/{cmd}/bin/python", decorators=[]
        )

    @app.route("/install/<appname>")
    def install_app(appname):
        data = {
            "args": ["-m", "pip", "install", "-r", f"/apps/{appname}/requirements.txt"],
            "timeout": 60,
            "force_unique_key": False,
        }
        client = flask.current_app.test_client()
        resp = client.post(f"/commands/{appname}", json=data).get_json()

        resp["result_url"] = resp["result_url"].replace(
            "http://localhost/", flask.request.url_root
        )

        return flask.jsonify(resp)
