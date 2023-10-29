from open_alchemy import init_yaml
import pathlib
import flask


def init_app(app: flask.Flask):
    # Construct model
    spec_dir = app.config["SPEC_DIR"] = pathlib.Path(
        app.config.get("SPEC_DIR", pathlib.Path(app.root_path) / "spec")
    )
    models_dir = app.config.get("OPENALCHEMY_MODELS_DIR")
    if models_dir:
        models_dir = pathlib.Path(models_dir)
        if not models_dir.is_absolute():
            models_dir = pathlib.Path(app.root_path) / models_dir
        if not models_dir.exists():
            models_dir.mkdir(parents=True, exist_ok=True)
    spec_files = (
        (f for f in spec_dir.iterdir() if f.is_file() and f.suffix in [".yml", ".yaml"])
        if spec_dir.exists()
        else ()
    )

    sqla_ext = app.extensions["sqlalchemy"]
    db = getattr(sqla_ext, "db", sqla_ext)

    for f in spec_files:
        spec = f.stem
        spec_file = spec_dir / f"{spec}.yaml"
        models_file = str(models_dir / f"{spec}.py") if models_dir else None
        init_yaml(str(spec_file), base=db.Model, models_filename=models_file)

    with app.app_context():
        db.create_all()
