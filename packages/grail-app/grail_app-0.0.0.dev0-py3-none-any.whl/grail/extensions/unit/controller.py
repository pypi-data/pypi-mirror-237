import flask
from typing import Optional, Any
LINUX_SOCKET = "/var/run/control.unit.sock"
APPLE_INTEL_SOCKET = "/usr/local/var/run/unit/control.sock"
APPLE_INTEL_LOG = "/usr/local/var/log/unit/unit.log"

APPLE_SILICON_SOCKET = "/opt/homebrew/var/run/unit/control.sock"
APPLE_SILICON_LOG = "/opt/homebrew/var/log/unit/unit.log"
DEFAULT_SCHEME = "http+unix://"

from .unixsocket import Session, Response


class Controller:
    """
    The Unit controller class.  This class provides a simple interface to the
    Unit API for managing applications and configuration.

    :param socket: The path to the Unit control socket. Defaults to
        ``/var/run/control.unit.sock`` on Linux and
        ``/usr/local/var/run/unit/control.sock`` on macOS.
    :type socket: str

    """

    def __init__(self, socket:Optional[str]=None, config_file:Optional[str]=None) -> None:
        # TODO: Determine socket based on platform
        if not socket:
            socket = LINUX_SOCKET
        self._socket = socket 
        self._session = Session(url_scheme=DEFAULT_SCHEME)
        self._config_file = config_file

    def request(self, method:str, url:str, **kwargs:Any) -> Response:
        return self._session.request(method=method, url=self._url(url), **kwargs)

    def get(self, url:str="", **kwargs:Any)-> Response:
        return self.request("get", url, **kwargs)

    def put(self, url:str="", **kwargs:Any) -> Response:
        return self.request("put", url, **kwargs)
    
    def delete(self, url:str="", **kwargs:Any) -> Response:
        return self.request("delete", url, **kwargs)

    def _url(self, url:str)->str:
        return f'{DEFAULT_SCHEME}{self._socket.replace("/", "%2F")}/{url.lstrip("/")}'

    def config(self)->Response:
        return self.get("config")

    def restart_app(self, app_name:str)->Response:
        return self.get(f"control/applications/{app_name}/restart")


def get_controller() -> Controller:
    c :Controller = flask.current_app.extensions[flask.current_app.config["UNIT_EXTENSION_NAME"]]
    return c