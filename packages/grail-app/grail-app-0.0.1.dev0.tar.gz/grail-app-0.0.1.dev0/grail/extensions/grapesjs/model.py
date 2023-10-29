from sqlalchemy import String, Text, Column, DateTime, Boolean
import datetime, json
from flask_appbuilder import Model
import flask


class Page(Model):
    # __bind_key__ = 'pages'
    id = Column(String, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    pages = Column(Text)
    styles = Column(Text)
    assets = Column(Text)
    template = Column(Boolean, default=False)
    thumbnail = Column(Text)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    def to_json(self):
        import json

        page = self
        return {
            "id": page.name,
            "name": page.name,
            "template": page.template,
            "thumbnail": page.thumbnail,
            "description": page.description,
            "assets": json.loads(page.assets),
            "pages": json.loads(page.pages),
            "styles": json.loads(page.styles),
            "updated_at": page.updated_at,
        }

    @classmethod
    def from_json(cls, jsonin):
        id = jsonin["id"]
        page = (
            flask.current_app.appbuilder.session.query(cls).filter(cls.id == id).first()
        )
        if not page:
            page = cls(id=id)
        page.name = jsonin.get("name", page.name)
        page.description = jsonin.get("description", page.description)
        page.template = jsonin.get("template", page.template)
        page.thumbnail = jsonin.get("thumbnail", page.thumbnail)
        for attr in ["pages", "assets", "styles"]:
            if attr in jsonin:
                if not isinstance(jsonin[attr], str):
                    jsonin[attr] = json.dumps(jsonin[attr])

        page.pages = jsonin.get("pages")
        page.assets = jsonin.get("assets")
        page.styles = jsonin.get("styles")
        # page.updated_at = jsonin.get('updated_at',page.updated_at)
        return page


def init_app(app):
    pass
