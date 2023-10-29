import flask
import pathlib, subprocess
import flask_flatpages
import os

bp = flask.Blueprint("generators", __name__, template_folder="templates")


def preprocess_frontmatter(yaml_template: str) -> dict[str, str]:
    from io import StringIO
    import yaml

    meta_string = flask.render_template_string(yaml_template)
    meta = {}
    for doc in yaml.safe_load_all(StringIO(meta_string)):
        if doc is not None:
            meta.update(doc)
    if not meta:
        return {}
    if not isinstance(meta, dict):
        raise ValueError(
            "Expected a dict in metadata for got {1}".format(type(meta).__name__)
        )

    return meta


def validate_python_syntax(code):
    try:
        # p = ast.parse(code)
        # print(p)
        return None  # Syntax is valid
    except SyntaxError as e:
        import traceback

        pathlib.Path("dump").write_text(code)
        print(traceback.format_exc())

        return str(e.text)  # Syntax error message


@bp.route("/<path:path>.py.jinja2/")
@bp.route("/<path:path>.py.j2")
@bp.route("/<path:path>.py.j2/")
@bp.route("/<path:path>/")
@bp.route("/<path:path>")
def get(path: str):
    generators: flask_flatpages.FlatPages = flask.current_app.extensions["flatpages"][
        "gen"
    ]

    generator = generators.get_or_404(path.rstrip("/"))

    generator.meta = preprocess_frontmatter(generator._meta)

    rendered = generator.html_renderer(generator)

    error = validate_python_syntax(rendered)

    if error:
        return error, 500
    return rendered, 200


def init_app(app: flask.Flask):
    app.register_blueprint(bp, url_prefix="/generators")

    app.config["FLATPAGES_GEN_ROOT"] = str(pathlib.Path(bp.root_path) / "templates")
    app.config["FLATPAGES_GEN_EXTENSION"] = ".py.jinja2,.py.j2"
    pages = flask_flatpages.FlatPages(app, name="gen")

    if os.environ.get("DISABLED_WRITE"):
        return
    coglines = []
    for fname, genpath in app.config.get("GENERATORS", {}).items():
        filepath = pathlib.Path(fname)
        if not filepath.is_absolute():
            filepath = pathlib.Path(app.root_path).absolute() / filepath
        line = COGTEXT.format(filename=filepath, genpath=genpath)
        coglines.append(line)
    COGFILE = pathlib.Path(flask.current_app.root_path) / ".cog.txt"

    COGFILE.write_text("\n".join(coglines))
    subprocess.run(["cog", f"@{COGFILE}"])


COGTEXT = """{filename} -I /app -p 'from grail.extensions.generators.gen import run;genpath="{genpath}"; gen=lambda path: cog.outl(run(path))' -z -r"""
