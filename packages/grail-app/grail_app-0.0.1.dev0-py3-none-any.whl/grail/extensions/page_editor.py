import flask
from pathlib import Path
from flask.typing import ResponseReturnValue
import flask_flatpages
from . import pages
from . import jinja_editor

page_editor = flask.Blueprint("page_editor", __name__)


def page_filepath(page: flask_flatpages.Page) -> Path:
    page_file = Path(pages.flatpages.root) / f"{page.path}.html"
    return page_file


@page_editor.route("/", methods=["GET"])
@page_editor.route("/<path:path>", methods=["GET"])
def editor(path: str = "index") -> str:
    page = pages.flatpages.get_or_404(path)
    filepath = page_filepath(page)
    template = jinja_editor.Template(
        name=path, content=filepath.read_text(), filename=str(filepath)
    )
    return flask.render_template("jinja_editor.html", template=template)


@page_editor.route("/preview", methods=["POST"])
def preview() -> ResponseReturnValue:
    template: jinja_editor.Template = jinja_editor.Template(**flask.request.json or {})
    original_page = pages.flatpages.get_or_404(template.name)

    page = pages.flatpages._parse(
        template.content, original_page.path, rel_path=pages.flatpages.root
    )

    template.content = page.html_renderer(page)
    extends = page.meta.get("template", "")
    template.content = jinja_editor.render_as_content(template, extends=extends)
    return flask.jsonify(template.__dict__)


@page_editor.route("/save", methods=["POST"])
def save() -> str:
    template = jinja_editor.Template(**flask.request.json or {})
    page = pages.flatpages.get_or_404(template.name)
    page_file: Path = page_filepath(page)
    page_file.write_text(template.content)
    return "OK"


def init_app(app: flask.Flask) -> None:
    app.register_blueprint(page_editor, url_prefix="/page_editor")
