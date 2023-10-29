from flask.typing import ResponseReturnValue
import flask
from pathlib import Path
import flask_flatpages


def init_routes(
    bp: flask.Blueprint, pages: flask_flatpages.FlatPages, methods: list[str] = ["GET"]
):
    @bp.route("/", methods=methods)
    @bp.route("/<path:path>/", methods=methods)
    def page(path: str = "index") -> ResponseReturnValue:
        flask.g.path = path
        page: flask_flatpages.Page | None = pages.get(path)
        if not page:
            return (
                flask.render_template(
                    "new_page.html", path=path.removesuffix(".html") + ".html"
                ),
                404,
            )
        page.meta = preprocess_frontmatter(page)

        flask.g.current_page = page
        if flask.request.headers.get("HX-Request"):
            return str(page.html_renderer(page))
        template = page.meta.get("template", flask.current_app.config["BASE_TEMPLATE"])
        response = flask.render_template(
            template, content=page.html_renderer(page), title=page.meta.get("title")
        )

        # response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        # response.headers['Pragma'] = 'no-cache'
        return response


def preprocess_frontmatter(page: flask_flatpages.Page) -> dict[str, str]:
    from io import StringIO
    import yaml

    meta_string = flask.render_template_string(page._meta)
    meta = {}
    for doc in yaml.safe_load_all(StringIO(meta_string)):
        if doc is not None:
            meta.update(doc)
    # YAML documents can be any type but we want a dict
    # eg. yaml.safe_load('') -> None
    #     yaml.safe_load('- 1\n- a') -> [1, 'a']
    if not meta:
        return {}
    if not isinstance(meta, dict):
        raise ValueError(
            "Expected a dict in metadata for '{0}', got {1}".format(
                page.path, type(meta).__name__
            )
        )

    return meta


def init_app(app: flask.Flask) -> None:
    for name, spec in app.config.get("PAGES", {}).items():
        fp = flask_flatpages.FlatPages(app=app, name=name)
        bp = flask.Blueprint(str(fp.name), __name__, template_folder=fp.root)
        path = spec.get("path", "") if spec else ""
        methods = spec.get("methods", ["GET"]) if spec else ["GET"]
        if path:
            init_routes(bp, fp, methods=methods)
        app.register_blueprint(bp, url_prefix=path)

    @app.route("/vscode/<pages>/<path:path>")
    def vscode(pages, path: str) -> ResponseReturnValue:
        flatpages_instance = flask.current_app.extensions["flatpages"][pages]
        path = path.removesuffix(".html") + ".html"
        filepath = Path(flatpages_instance.root) / path

        if not filepath.exists():
            filepath.parent.mkdir(parents=True, exist_ok=True)
            filepath.write_text(DEFAULT_PAGE_TEMPLATE)
        return flask.redirect(f"vscode://file/{filepath.absolute()}")

    @app.context_processor
    def inject_pages() -> dict:
        return flask.current_app.extensions.get("flatpages", {})


DEFAULT_PAGE_TEMPLATE = """title: New Page\n\n<h1> Hello World </h1>"""
