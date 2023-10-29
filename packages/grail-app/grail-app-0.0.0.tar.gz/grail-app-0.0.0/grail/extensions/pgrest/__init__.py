import flask
from typing import Any, Literal, Optional, Union
from werkzeug.local import LocalProxy
from pypgrest import Postgrest as PostgrestBase
from pydantic import BaseModel, Field

POSTGREST_URI = "http://127.0.0.1:3000"


class Postgrest(PostgrestBase):
    def count(self, *, resource, params=None, headers=None, **kwargs):
        """Fetch selected records from PostgREST. See documentation for horizontal
        and vertical filtering at http://postgrest.org/.
        Args:
            resource (str): Required. The postgrest's endpoint's table or view name to
                query.
            headers (dict): Custom PostgREST headers which will be passed to the
                request. Defaults to None.
            params (dict): PostgREST-compliant request parameters. Defaults to None.
        Returns:
            List: A list of dicts of data returned from the host
        """
        params = {} if not params else params

        method = "head"
        headers = self._get_request_headers(headers)
        self._make_request(
            resource=resource, method=method, headers=headers, params=params
        )
        range, count = self.res.headers["Content-Range"].split("/")
        return count


class PostgrestRequest(BaseModel):
    resource: str
    select: str = "*"
    order: Optional[str] = None
    limit: int = 100
    filters: dict[str, str] = {}
    headers: dict[str, str] = {}
    alias: str = "items"
    pagination: bool = False
    count: Union[Literal["exact"], Literal["estimated"], Literal["planned"], None] = None
    db: str


def request(pgrest_request: dict[str, Any]) -> dict[str, Any]:
    request_args = create_select_request(pgrest_request)
    db = pgrest_request["db"]
    uri = flask.current_app.config["POSTGREST_URI"][db]
    pgrest = Postgrest(uri)
    if "count" in pgrest_request:
        return pgrest.count(**request_args)
    else:
        return pgrest.select(**request_args)


def create_select_request(pgrest_request: dict[str, Any]) -> dict[str, Any]:
    """Convert a PostgrestRequest to a dict suitable for passing to Postgrest.select"""

    request_args: PostgrestRequest = PostgrestRequest(**pgrest_request)
    resource: str = request_args.resource
    params: dict[str, Any] = request_args.filters
    if request_args.select:
        params["select"] = request_args.select
    if request_args.order:
        params["order"] = request_args.order
    if request_args.limit:
        params["limit"] = request_args.limit
    if request_args.count:
        request_args.headers["Prefer"] = f"count={request_args.count}"

    args = {
        "resource": resource,
        "params": params,
        "pagination": request_args.pagination,
        "headers": request_args.headers,
    }
    return args


dbapi = flask.Blueprint("dbapi", __name__, url_prefix="/dbapi")


def init_app(app: flask.Flask) -> None:
    app.register_blueprint(dbapi)

    api_url = app.config.setdefault("POSTGREST_URI", POSTGREST_URI)
