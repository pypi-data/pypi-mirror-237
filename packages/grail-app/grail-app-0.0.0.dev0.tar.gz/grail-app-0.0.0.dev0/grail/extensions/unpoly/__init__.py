import flask
from unpoly import Unpoly
from typing import Mapping, cast, Optional
import json
from unpoly.adapter import BaseAdapter

# The following code is run in a middleware, once per request
UP_METHOD_COOKIE = "_up_method"


class FlaskAdaptor(BaseAdapter):
    """
    Provides the entrypoint for other frameworks to use this library.

    Implements common functionality that is not often overriden as well
    as framework specific hooks.
    """

    def __init__(self, request: flask.Request) -> None:
        super().__init__()
        self.request: flask.Request = request

    def request_headers(self) -> Mapping[str, str]:
        """Reads the request headers from the current request.

        Needs to be implemented."""
        return self.request.headers

    def request_params(self) -> Mapping[str, str]:
        """Reads the GET params from the current request.

        Needs to be implemented."""
        return self.request.args

    def redirect_uri(self, response: flask.Response) ->Optional[str]:
        """Returns the redirect target of a response or None if the response
        is not a redirection (ie if it's status code is not in the range 300-400).

        Needs to be implemented."""
        return (
            cast(Mapping[str, str], response.headers).get("Location")
            if 300 <= response.status_code < 400  # noqa: PLR2004
            else None
        )

    def set_redirect_uri(self, response: flask.Response, uri: str) -> None:
        """Set a new redirect target for the current response. This is used to
        pass unpoly parameters via GET params through redirects.

        Needs to be implemented."""
        response.headers["Location"] = uri

    def set_headers(self, response: flask.Response, headers: Mapping[str, str]) -> None:
        """Set headers like `X-Up-Location` on the current response.

        Needs to be implemented."""
        for k, v in headers.items():
            response.headers[k] = v

    def set_cookie(self, response: flask.Response, needs_cookie: bool = False) -> None:
        """Set or delete the `_up_method <https://unpoly.com/_up_method>`_ cookie.

        The implementation should set the cookie if `needs_cookie` is `True` and
        otherwise remove it if set.

        Needs to be implemented."""
        if needs_cookie:
            response.set_cookie(UP_METHOD_COOKIE, self.method)
        elif UP_METHOD_COOKIE in self.request.cookies:
            response.delete_cookie(UP_METHOD_COOKIE)

    @property
    def method(self) -> str:
        """Exposes the current request's method (GET/POST etc)

        Needs to be implemented."""
        return cast(str, self.request.method)

    @property
    def location(self) -> str:
        """Exposes the current request's location (path including query params)

        Needs to be implemented."""
        return self.request.full_path

    def deserialize_data(self, data: str) -> object:
        """Deserializes data passed in by Unpoly.

        By default it simply reads it as JSON, but can be overriden if custom
        decoders are needed.
        """
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            return None

    def serialize_data(self, data: object) -> str:
        """Serializes the data for passing it to Unpoly.

        By default it simply serializes it as JSON, but can be overriden if custom
        encoders are needed.
        """
        return json.dumps(data, separators=(",", ":"), ensure_ascii=True)


def before_request():
    adapter = FlaskAdaptor(flask.request)
    # Attach `Unpoly` to the request, so views can easily acces it
    flask.g.up = Unpoly(adapter)

    # Actually execute the view and get the response object
    @flask.after_this_request
    def finalize(response):
        # Tell `Unpoly` to set the relevant `X-Up-*` headers
        flask.g.up.finalize_response(response)
        return response


bp = flask.Blueprint(
    "unpoly",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/unpoly/static",
)


def init_app(app: flask.Flask):
    app.register_blueprint(bp)

    app.before_request(before_request)
