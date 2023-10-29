from re import T
import flask
from flask.typing import ResponseReturnValue
import dataclasses
from pathlib import Path


@dataclasses.dataclass
class Template:
    name: str
    content: str
    filename: str
    uptodate: bool = True

    def __html__(self) -> str:
        return self.content


jinja_editor = flask.Blueprint(
    "jinja_editor",
    __name__,
    template_folder="templates",
    static_folder="static",
)


def template_loader(name: str) -> Template:
    loader = flask.current_app.jinja_env.loader
    content, filename, uptodate = (
        loader.get_source(flask.current_app.jinja_env, template=name)
        if loader
        else ("", "", True)
    )
    if not filename:
        flask.abort(404, f"Template named '{name}' not found")

    template = Template(
        name=name,
        content=content,
        filename=name,
        uptodate=uptodate() if callable(uptodate) else uptodate or True,
    )
    return template


def template_renderer(template: Template) -> str:
    if False:
        return render_as_block(template)
    else:
        return render_as_content(template)


def template_saver(template: Template) -> None:
    template_root: Path = Path(flask.current_app.template_folder or "")
    if not template_root.is_absolute():
        template_root = Path(flask.current_app.root_path) / template_root
    template_path = template_root.absolute() / template.filename
    if not Path(template_path).exists():
        template_path.parent.mkdir(parents=True, exist_ok=True)
        flask.current_app.logger.info(
            f"Template file '{template.filename}' created at {template_path}"
        )
    template_path.write_text(template.content)


@jinja_editor.route("/", methods=["GET"])
@jinja_editor.route("/<path:path>", methods=["GET"])
def editor(path: str = "") -> str:
    path = path or flask.current_app.config["BASE_TEMPLATE"]
    template = template_loader(path)
    return flask.render_template("jinja_editor.html", template=template)


@jinja_editor.route("/preview", methods=["POST"])
def preview() -> ResponseReturnValue:
    template: Template = Template(**flask.request.json or {})
    template.content = template_renderer(template)
    return flask.jsonify(template.__dict__)


@jinja_editor.route("/save", methods=["POST"])
def save() -> str:
    template = Template(**flask.request.json or {})
    template_saver(template)
    return "OK"


# ------------------------
def render_as_block(template: Template) -> str:
    if template.name != flask.current_app.config["BASE_TEMPLATE"]:
        return flask.render_template_string(
            """
            {%extends config.BASE_TEMPLATE%}
            {%block content%}
                {{template}}
            {%endblock content %}
            """,
            template=template,
        )
    return flask.render_template_string(template.content)


def render_as_content(template: Template, extends: str = "") -> str:
    template.content = flask.render_template_string(template.content)
    if template.name != flask.current_app.config["BASE_TEMPLATE"]:
        return flask.render_template(
            extends or flask.current_app.config["BASE_TEMPLATE"], content=template
        )
    return template.content


def init_app(app: flask.Flask) -> None:
    app.register_blueprint(jinja_editor, url_prefix="/jinja_editor")
