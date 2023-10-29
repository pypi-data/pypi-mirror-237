from py_avataaars import PyAvataaar
import py_avataaars as pa
import random
import flask
from markupsafe import Markup

avatar_cache = {}


def generate_random_avatar() -> str:
    """Generate a random avatar"""

    avatar = PyAvataaar(
        style=pa.AvatarStyle.CIRCLE,
        skin_color=random.choice(list(pa.SkinColor)),
        hair_color=random.choice(list(pa.HairColor)),
        facial_hair_type=random.choice(list(pa.FacialHairType)),
        facial_hair_color=random.choice(list(pa.HairColor)),
        top_type=random.choice(list(pa.TopType)),
        hat_color=random.choice(list(pa.Color)),
        mouth_type=random.choice(list(pa.MouthType)),
        eye_type=random.choice(list(pa.EyesType)),
        eyebrow_type=random.choice(list(pa.EyebrowType)),
        nose_type=random.choice(list(pa.NoseType)),
        accessories_type=random.choice(list(pa.AccessoriesType)),
        clothe_type=random.choice(list(pa.ClotheType)),
        clothe_color=random.choice(list(pa.Color)),
        clothe_graphic_type=random.choice(list(pa.ClotheGraphicType)),
    )
    return avatar.render_svg()


def init_app(app: flask.Flask) -> None:
    def gen(id=None):
        if id in avatar_cache:
            return avatar_cache[id]
        a = generate_random_avatar()
        # Mark as safe for Jinja
        a = Markup(a)
        if id:
            avatar_cache[id] = a
        return a

    app.jinja_env.globals.update(avatar=gen)
