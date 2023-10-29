import flask
import yaml
from grail.extensions import settings, pgrest
import requests
import flask_flatpages


def render_page(
    text: str,
    pages: flask_flatpages.FlatPages,
    page: flask_flatpages.Page,
) -> str:
    # 1. resolve pgrest requests
    pgrest_requests = page.meta.get("pgrest", {})
    for alias, pgrest_request in pgrest_requests.items():
        response = pgrest.request(pgrest_request)
        page.meta[alias] = response
        page.meta["response"] = response

    # 2. resolve internal requests
    internal_requests = page.meta.get("requests", {})
    for alias, request in internal_requests.items():
        request_url = uri = request.get("uri") if request else None
        if not request_url:
            continue
        request_method = request.get("method", "get").lower()
        request_url = (
            flask.request.host_url + request_url.lstrip()
            if not request_url.startswith("http")
            else request_url
        )
        response = requests.request(
            request_method, request_url, json=request.get("data")
        )
        page.meta[alias] = response

    # 3. resolve model specs
    specs = page.meta.get("specs", {})
    for alias, spec in specs.items():
        spec_text = (flask.current_app.config["SPEC_DIR"] / spec).read_text()
        spec_dict = yaml.safe_load(spec_text)
        page.meta["specs"][alias] = spec_dict
    # Render template from file so that it's available in debugger
    rendered_html = flask.render_template(
        [
            f"{page.path}.html",
            f"{page.path}.py.j2",
            f"{page.path}.py.jinja2",
        ],
        current_pages=pages,
        **page.meta,
    )

    new_page = pages._parse(rendered_html, path=page.path, rel_path=pages.root)

    return new_page.body or ""


def create_app() -> flask.Flask:
    app = flask.Flask(__name__, instance_relative_config=True)
    settings.init_app(app)
    return app


def application(environ, start_response):
    app = create_app()
    return app(environ, start_response)


if __name__ == "__main__":
    create_app().run()
