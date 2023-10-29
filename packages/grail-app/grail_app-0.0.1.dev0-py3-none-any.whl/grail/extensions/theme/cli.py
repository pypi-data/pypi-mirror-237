import click
from .html_to_jinja import load_config, write_config, transform_html  # type: ignore
from pathlib import Path
import flask
import contextlib
import os, sys

THEMES_DIR = Path(__file__).parent / "themes"
HERE = Path(__file__).parent


@click.command("create", short_help="Create a new template theme.")
@click.argument(
    "directory",
)
def create_theme(directory) -> None:
    """Create theme from this config file."""
    theme_dir = THEMES_DIR / directory
    demo_dir = Path(flask.current_app.config["DEMO_FOLDER"])
    if not theme_dir.exists():
        demo_path = demo_dir / directory
        if not demo_path.exists():
            flask.abort(404, f"Demo theme '{directory} not found in '{demo_path}'")
        new_config_file = theme_dir / "config.yaml"
        default_file = load_config(str(HERE / "config.yaml"))
        default_file.input_file = str(
            Path(demo_path / "dist" / "index.html").relative_to(demo_dir)
        )
        write_config(default_file, new_config_file)
    with cd(theme_dir):
        config = load_config()
        input_file = str(demo_dir / config.input_file)
        config.input_file = input_file
        html = Path(config.input_file).read_text()
        html_out = transform_html(html, config)
        Path(config.output_file).write_text(html_out)


@contextlib.contextmanager
def cd(path: Path):
    CWD = os.getcwd()
    os.chdir(path)
    try:
        yield
    except Exception as e:
        flask.current_app.logger.error(f"Error setting directory: {e}")
    finally:
        os.chdir(CWD)
