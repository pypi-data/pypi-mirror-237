import flask
from flask.cli import ScriptInfo
from werkzeug.local import LocalProxy
from typing import Type

AppImportPath = str

current_gateway = LocalProxy(lambda: flask.current_app.extensions["gateway"])


def load_app_from_spec(appspec: AppImportPath) -> flask.Flask:
    script_info = ScriptInfo(app_import_path=appspec)

    flask_app = script_info.load_app()

    return flask_app


class RuntimeDispatcherMiddleware:
    """Combine multiple applications as a single WSGI application.
    Requests are dispatched to an application based on the path it is
    mounted under.

    :param app: The WSGI application to dispatch to if the request
        doesn't match a mounted path.
    :param mounts: Maps path prefixes to applications for dispatching.
    """

    def __init__(self, app: flask.Flask, mounts=None, before_request=None):
        self.wsgi_app = app.wsgi_app
        app.wsgi_app = self
        self.flask_app = app
        self.mounts: dict[str, AppImportPath] = mounts or {}
        self.instances: dict[str, flask.Flask] = {}
        self._before_request_func = before_request or (lambda: None)
        app.extensions["gateway"] = self
        app.context_processor(lambda: {"gateway": self})

    def url(self, path: str = "") -> str:
        return flask.request.script_root + path

    def current_prefix(self, environ):
        script: str = environ.get("PATH_INFO", "")
        path_info: str = ""

        while "/" in script:
            if script in self.mounts:
                import_path = self.mounts[script]
                app = self.instances.get(script)
                if not app or app.config.get("NEED_RESTART"):
                    app = load_app_from_spec(import_path)
                    self.instances[script] = app
                break

            script, last_item = script.rsplit("/", 1)
            path_info = "/%s%s" % (last_item, path_info)
        else:
            import_path = self.mounts.get(script, "")
            if import_path:
                app = self.instances.get(import_path)
                if not app:
                    app = load_app_from_spec(import_path)
                    self.instances[script] = app
            else:
                app = self.wsgi_app

        return script, path_info, app

    def __call__(self, environ, start_response):
        # if not self.flask_app.got_first_request:
        #     return self.wsgi_app(environ=environ,start_response=start_response)

        prefix, path, app = self.current_prefix(environ=environ)
        original_script_name = environ.get("SCRIPT_NAME", "")
        environ["SCRIPT_NAME"] = original_script_name + prefix
        environ["PATH_INFO"] = path

        with self.flask_app.request_context(environ):
            try:
                app = self._before_request_func() or app
            except Exception as e:
                # Handle error as if it came from original flask app
                app = self.flask_app.handle_exception(e)

        response = app(environ, start_response)

        return response


def init_app(app: flask.Flask) -> None:
    setattr(app, "gateway", RuntimeDispatcherMiddleware(app))
