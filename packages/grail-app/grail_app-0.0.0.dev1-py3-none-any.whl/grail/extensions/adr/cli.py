from . import lib as adr_func
import click
import flask
from typing import Optional 
cli = click.Group("adr", help="Create, List or Serve Architectural Decision Records")


@cli.command(
    help="Creates a new, numbered ADR. The TITLE arguments are concatenated to form the title of the new ADR"
)
@click.option(
    "-s",
    "--supersede",
    default=None,
    help="A reference (number or partial filename) of a previous decision that the new decision supercedes",
)
@click.option(
    "-l",
    "--link",
    default=None,
    help="TARGET:LINK:REVERSE-LINK, Links the new ADR to a previous ADR.  TARGET is a reference (number or partial filename) of a previous decision. LINK is the description of the link created in the new ADR. REVERSE-LINK is the description of the link created in the existing ADR that will refer to the new ADR.",
)
@click.argument("title", nargs=-1)
def new(title: str, supersede: Optional[str]=None, link: Optional[str] = None) -> None:
    """
    Creates a new, numbered ADR. The TITLE arguments are concatenated to form the title of the new ADR.

    TITLE is the title of ADR.
    """
    adr_func.set_adr_verbosity(True)
    new_adr = adr_func.adr_new(" ".join(title), superseded=supersede, links=link)
    try:
        import editor  # type: ignore

        editor.editor(filename=new_adr, editor="code")
        print(f'Opening ADR file "{new_adr}" in editor "{editor.default_editor()}".')
    except Exception as e:
        print(e)


@cli.command("list", help="List all architectural decision records")
@click.option(
    "--adr-path",
    default=lambda: flask.current_app.config["ADR_PATH"],
    help="Directory containing ADR files.",
    show_default=True,
)
def list_all(adr_path: str) -> None:
    adrs = adr_func.adr_list(adr_path)
    for adr in adrs:
        click.echo(adr)


@cli.command("report", help="Generate the report in ADR_PATH/report.html")
@click.option(
    "--adr-path",
    default=lambda: flask.current_app.config["ADR_PATH"],
    help="Directory containing ADR files.",
    show_default=True,
)
@click.option(
    "--output",
    default=lambda: f"{flask.current_app.config['ADR_PATH']}/report.html",
    help="File to write output to.",
    show_default=True,
)
def report(adr_path, output):
    try:
        from adr_viewer import generate_content
    except Exception as e:
        click.echo(
            f'Missing adr_viewer package. Try "pip install adr_viewer": {e}', err=True
        )
        return

    content = generate_content(
        adr_path,
        template_dir_override=flask.current_app.config["ADR_VIEWER_TEMPLATE_DIR"],
    )
    with open(output, "w") as out:
        out.write(content)

    click.echo(f"Generated {output} from {adr_path}")
    try:
        import webbrowser

        webbrowser.open(output)
    except Exception as e:
        click.echo(f"Unable to open web browser: {e}", err=True)
