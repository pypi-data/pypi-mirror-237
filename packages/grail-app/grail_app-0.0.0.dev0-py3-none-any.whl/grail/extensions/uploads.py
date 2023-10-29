import flask
import pathlib

bp = flask.Blueprint("uploads", "uploads")


@bp.route("/upload", methods=["POST"])
def upload():
    from flask import request, flash, redirect, url_for
    from werkzeug.utils import secure_filename

    def allowed_file(filename):
        return "." in filename and filename.rsplit(".", 1)[1].lower() in ["go"]

    files = flask.request.files.getlist("files")
    if not files:
        return "", 404

    for file in files:
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            dirname = pathlib.Path(flask.current_app.config["UPLOAD_FOLDER"])
            if not dirname.is_absolute():
                dirname = pathlib.Path(flask.current_app.root_path) / dirname
            if not dirname.exists():
                dirname.mkdir(parents=True, exist_ok=True)
            file.save(dirname / filename)

    headers = {"HX-Redirect": url_for("pages.page", path="/files")}
    if len(files) == 1:
        headers = {
            "HX-Redirect": url_for("pages.page", path="/files", filename=filename)
        }

    return flask.make_response("", 303, headers)


def init_app(app: flask.Flask) -> None:
    app.register_blueprint(bp)

    f = app.config.get("UPLOAD_FOLDER")
    if f:
        app.config["UPLOAD_FOLDER"] = pathlib.Path(f)
