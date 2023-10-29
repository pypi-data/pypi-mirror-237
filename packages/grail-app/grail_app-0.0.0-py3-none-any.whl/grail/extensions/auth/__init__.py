import flask

auth = flask.Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@auth.route("/sign-in", methods=["GET", "POST"])
def sign_in() -> str:
    if flask.request.method == "POST":
        # Handle sign-in
        pass
    return flask.render_template("auth/sign-in.html")


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up() -> str:
    if flask.request.method == "POST":
        # Handle sign-up
        pass

    return flask.render_template("auth/sign-up.html")


def init_app(app: flask.Flask) -> None:
    app.register_blueprint(auth)
