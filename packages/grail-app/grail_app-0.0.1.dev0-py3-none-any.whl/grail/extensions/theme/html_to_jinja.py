from typing import List, Any, Literal, Optional, Union
from pydantic import BaseModel
from pathlib import Path
from bs4 import BeautifulSoup
from ruamel.yaml import YAML

yaml = YAML()
from pydantic import ValidationError
import re


class Variable(BaseModel):
    text: str
    variable: str


class CommentBlock(BaseModel):
    start_comment: str
    end_comment: str


class Block(BaseModel):
    selector: Union[str , CommentBlock]
    block: str
    output_file: Optional[str] = None
    swap: Union[Literal["innerHTML"] , Literal["outerHTML"] , Literal["text"] , Literal[
        "before_end"
    ]] = "outerHTML"


class URL(BaseModel):
    prefix: Optional[str] = None
    endpoint: Optional[str] = None
    replace: Optional[str] = None


class Config(BaseModel):
    version: str
    input_file: str
    output_file: str
    variables: List[Variable]
    blocks: List[Block]
    urls: List[URL]


import re


def replace_between_comments(
    data: str, start_comment: str, end_comment: str, replacement_text: str
) -> tuple[str, str]:
    """Replace text between the provided HTML comment tags and return the updated data and extracted text."""

    between_start = data.find(start_comment) + len(start_comment)
    between_end = data.find(end_comment)

    first = data[:between_start]
    middle = data[between_start:between_end]
    last = data[between_end:]

    updated_data = first + replacement_text + last

    return updated_data, middle


def check_output_paths(
    output_file: str, blocks: list[Block], mkdirs: bool = True
) -> None:
    """Check that all output paths exist, creating them if necessary.

    Args:
        output_file (str): _description_
        blocks (list[Block]): _description_
    """
    missing_dirs = []
    output_path = Path(output_file)
    if not output_path.parent.exists():
        missing_dirs.append(output_path.parent)
    for block in blocks:
        if block.output_file:
            output_path = Path(block.output_file)
            if not output_path.parent.exists():
                missing_dirs.append(output_path.parent)

    if missing_dirs:
        if mkdirs:
            print(f"Creating missing directories: {missing_dirs}")
            for missing_dir in missing_dirs:
                missing_dir.mkdir(parents=True, exist_ok=True)
        else:
            raise RuntimeError(f"Missing directories: {missing_dirs}")


def process_variables(soup: BeautifulSoup, variables: list[Variable]) -> dict[str, str]:
    replaced = {}
    soup_text = str(soup)
    for var in variables:
        if var.text in soup_text:
            soup_text = soup_text.replace(var.text, var.variable)
            replaced[var.text] = var.variable
    soup.__init__(soup_text, "html.parser")
    return replaced


def process_blocks(soup: BeautifulSoup, blocks: list[Block]) -> dict[str, str]:
    replaced = {}
    for block in blocks:
        if isinstance(block.selector, CommentBlock):
            soup_text, text = replace_between_comments(
                str(soup),
                block.selector.start_comment,
                block.selector.end_comment,
                block.block,
            )
            soup.__init__(soup_text, "html.parser")
            block_text = BeautifulSoup(text, "html.parser")
            if block.output_file:
                with open(block.output_file, "w") as file:
                    file.write(block_text.prettify())
                continue
        element = soup.select_one(block.selector)
        if element:
            if block.swap == "text":
                text = element.get_text()
                element.clear()
                element.append(block.block)
                if block.output_file:
                    with open(block.output_file, "w") as file:
                        file.write(text)
            elif block.swap == "innerHTML":
                if block.output_file:
                    with open(block.output_file, "w") as file:
                        bc = BeautifulSoup(element.decode_contents(), "html.parser")
                        file.write(bc.prettify())
                element.clear()
                element.append(block.block)
            elif block.swap == "outerHTML":
                element.replace_with(block.block)
                if block.output_file:
                    with open(block.output_file, "w") as file:
                        file.write(element.prettify())
            elif block.swap == "before_end":
                element.append(block.block)
                if block.output_file:
                    with open(block.output_file, "w") as file:
                        file.write(element.prettify())
            replaced[block.selector] = block.block
    return replaced


def convert_url_to_urlfor(
    soup: BeautifulSoup,
    endpoint: str = "static",
    prefix: str = "assets",
    replace_prefix: Optional[str] = None,
) -> dict[str, str]:
    # Open the HTML file and parse it with BeautifulSoup
    replaced = {}
    replace_prefix = prefix if replace_prefix is None else replace_prefix
    # Find all the tags with a 'src' attribute
    for tag in soup.find_all(href=True):
        # Get the original 'src' attribute
        original_src = tag["href"]
        if not original_src.startswith(prefix):
            continue
        new_src = original_src.replace(prefix, replace_prefix)
        # Replace the 'src' attribute with a Jinja 'url_for' statement
        if endpoint:
            new_src = "{{" + f"url_for('{endpoint}', filename='{new_src}')" + "}}"
        tag["href"] = new_src
        replaced[original_src] = new_src

    # Find all the tags with a 'src' attribute
    for tag in soup.find_all(src=True):
        # Get the original 'src' attribute
        original_src = tag["src"]
        if not original_src.startswith(prefix):
            continue
        new_src = original_src.replace(prefix, replace_prefix)
        # Replace the 'src' attribute with a Jinja 'url_for' statement
        if endpoint:
            new_src = "{{" + f"url_for('{endpoint}', filename='{new_src}')" + "}}"
        tag["src"] = new_src
        replaced[original_src] = new_src

    # Find all the tags with a 'style' attribute containing 'background-image:url'
    for tag in soup.find_all(style=re.compile("background-image:url")):
        # Get the original 'style' attribute
        original_style = tag["style"]

        # Find the URL within the 'background-image:url' statement
        url = re.search(r"url\('(.*?)'\)", original_style).group(1)
        if not url.startswith(prefix):
            continue
        new_url = url.replace(prefix, replace_prefix)
        # Replace the URL with a Jinja 'url_for' statement
        if endpoint:
            new_url = "{{" + f"url_for('{endpoint}', filename='{new_url}')" + "}}"

        new_style = original_style.replace(url, new_url)

        # Set the new 'style' attribute
        tag["style"] = new_style
        replaced[original_style] = new_style

    # Write the new HTML content back to the file
    return replaced


def process_urls(soup: BeautifulSoup, urls: list[Any]) -> dict[str, str]:
    replaced: dict[str, str] = {}
    for url in urls:
        r = convert_url_to_urlfor(soup, url.endpoint, url.prefix, url.replace)
        replaced = {**replaced, **r}
    return replaced


def transform_html(html_data: str, config: Config) -> str:
    check_output_paths(config.output_file, config.blocks)

    soup = BeautifulSoup(html_data, "html.parser")

    replaced_vars = process_variables(soup, config.variables)
    replaced_urls = process_urls(soup, config.urls)
    replaced_blocks = process_blocks(soup, config.blocks)

    print(
        f"""
    Replaced URLs: {len(replaced_urls)}
    Replaced variables: {replaced_vars}
    Replaced blocks: {replaced_blocks.keys()}
    """
    )

    return str(soup.prettify())


def load_config(path: str = "config.yaml") -> Config:
    with open(path, "r") as f:
        data = yaml.load(f)
    config = Config(**data)
    return config


def write_config(config: Config, path: str = "config.yaml") -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        yaml.dump(config.dict(), f)


if __name__ == "__main__":
    config = load_config()
    html = Path(config.input_file).read_text()
    html_out = transform_html(html, config)
    Path(config.output_file).write_text(html_out)
