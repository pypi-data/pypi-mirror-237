from flask_appbuilder import BaseView, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView
from .model import Page
from .config import grapesjs_config
import flask
from pathlib import Path
import json

HERE = Path(__file__).parent

static_bp = flask.Blueprint(
    "grapesjs",
    __name__,
    static_folder=str(HERE / "static"),
    template_folder=str(HERE / "templates"),
    static_url_path="/grapesjs/static",
)


class PagesView(ModelView):
    formatters_columns = {
        "name": lambda n: flask.Markup(
            f"""<a href="{flask.url_for('PagesView.view',id=n)}">{n}</a>"""
        )
    }

    datamodel = SQLAInterface(Page)
    list_columns = ["name", "description", "created_at", "updated_at"]
    edit_columns = [
        "name",
        "description",
        "pages",
        "styles",
        "assets",
        "template",
    ]
    add_columns = edit_columns
    template_folder = str(HERE / "templates")

    @expose("/view/<id>")
    def view(self, id):
        page = (
            flask.current_app.appbuilder.session.query(Page)
            .filter(Page.name == id)
            .first_or_404()
        )
        conf = grapesjs_config(pages=page.pages, storage_manager=False)
        return flask.render_template(
            "grapesjs/index2.html", page=page, grapesjs_config=conf
        )

    @expose("/editor")
    def editor(self):
        conf = grapesjs_config(storage_manager=True)
        return flask.render_template("grapesjs/index2.html", grapesjs_config=conf)

    @expose("/new", methods=["POST"])
    def new(self):
        page = Page(name="New Page", html="Edit Me!")
        return flask.render_template("grapesjs/index.html", page=page)

    @expose("/preview/<name>")
    def preview(self, name):
        page = (
            flask.current_app.appbuilder.session.query(Page)
            .filter(Page.name == name)
            .first_or_404()
        )
        page.html = flask.render_template_string(page.html)
        return flask.render_template("grapesjs/preview.html", page=page)

    @expose("/update/<name>", methods=["POST"])
    def update(self, name):
        import re

        session = flask.current_app.appbuilder.session
        html = flask.request.form.get("html")
        css = flask.request.form.get("css")
        page = session.query(Page).filter(Page.name == name).first_or_404()
        if html:
            page.html = re.compile(r"<body[^>]+>").sub("", html).removesuffix("</body>")
        if css:
            page.css = css
        session.add(page)
        session.commit()
        flask.flash(f'Updated page "{name}"!', category="success")
        return flask.jsonify({"result": page.to_json()})

    @expose("/load", methods=["GET"])
    def all(self):
        pages = flask.current_app.appbuilder.session.query(Page).all()
        pages_json = []
        for page in pages:
            pages_json.append(page.to_json())
        return flask.jsonify(pages_json)

    @expose("/load/<path:id>", methods=["GET"])
    def load(self, id):
        page = (
            flask.current_app.appbuilder.session.query(Page)
            .filter(Page.id == id)
            .first()
        )
        if not page:
            return flask.jsonify({})
        return flask.jsonify(page.to_json())

    @expose("/store", methods=["POST"])
    @expose("/store/<id>", methods=["POST"])
    def store(self, id=None):
        page = Page.from_json(flask.request.json)
        flask.current_app.appbuilder.session.add(page)
        flask.current_app.appbuilder.session.commit()
        return flask.jsonify(page.to_json())

    @expose("/remove", methods=["DELETE"])
    @expose("/remove/<name>", methods=["DELETE"])
    def remove(self, name=None):
        page = (
            flask.current_app.appbuilder.session.query(Page)
            .filter(Page.name == name)
            .first()
        )
        if not page:
            return flask.jsonify({})
        flask.current_app.appbuilder.session.delete(page)
        flask.current_app.appbuilder.session.commit()
        return 200


def init_app(app: flask.Flask):
    appbuilder = app.extensions.get("appbuilder")
    if not appbuilder:
        return

    appbuilder.add_view(PagesView, "Builder", icon="fa-wrench", category="Developer")
    csrf = app.extensions.get("csrf")
    if csrf:
        csrf.exempt(app.blueprints[PagesView.__name__])
    app.register_blueprint(static_bp)
