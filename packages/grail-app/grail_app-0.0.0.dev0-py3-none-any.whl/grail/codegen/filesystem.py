from .base import Base, Generator
import black
from pydantic import Field, validator
import textwrap
import pathlib


class FilesystemModel(Base):
    path: str
    content: str


class FilesystemFormatter(Generator[list[FilesystemModel], list[FilesystemModel]]):
    def generate(self, inp: list[FilesystemModel]) -> list[FilesystemModel]:
        def do_format(s: FilesystemModel) -> str:
            r: str = s.content
            try:
                r = black.format_str(s.content, mode=black.FileMode())
            except Exception as e:
                print(f"Failed to parse {s.path} {s.content}: {e}")
            return r

        return [
            FilesystemModel(
                name=f.name,
                description=f.description,
                path=f.path,
                content=do_format(f),
            )
            for f in inp
        ]


class FileLoader(Generator[list[str], list[FilesystemModel]]):
    """Load a list of files from the filesystem

    Args:
        base_path (str): The base path to load files from


    Returns:
        _type_: _description_
    """

    base_path: str

    def generate(self, inp: list[str]) -> list[FilesystemModel]:
        files: list[FilesystemModel] = [
            FilesystemModel(name=fname, path=fname, content=p.read_text())
            for p, fname in [
                (pathlib.Path(self.base_path) / pathlib.Path(fname), fname)
                for fname in inp
            ]
        ]
        return files


class FileDumper(Generator[list[FilesystemModel], pathlib.Path]):
    build_dir: str = Field(
        title="Build Directory",
        description="""
        Which directory to use for writing the files. If not provided, a temporary directory is used.
        TODO: Allow S3, GCS, FTP, etc. as build directories.
        """,
        example="/home/developer/myapp",
        default="",
    )

    @validator("build_dir")
    def check_build_dir(cls, v: str) -> str:
        if not pathlib.Path(v).exists():
            raise ValueError(f"Path {v} does not exist")
        return v

    def generate(self, inp: list[FilesystemModel]) -> pathlib.Path:
        import pathlib, tempfile

        # Create a tempformatterorary directory inside a with statement

        dirname = pathlib.Path(self.build_dir)

        files_to_write: dict[pathlib.Path, str] = {}
        for pyfile in inp:
            codefile: pathlib.Path = pathlib.Path(dirname) / pathlib.Path(pyfile.path)
            if codefile in files_to_write:
                raise ValueError(
                    textwrap.dedent(
                        f"""
                        File {codefile} already already written with content 
                        Existing -----------:
                        {files_to_write[codefile]} 
                        
                        New ---------------:
                        {pyfile.content}
                        """
                    ).lstrip()
                )

            files_to_write[codefile] = pyfile.content

        for codefile, content in files_to_write.items():
            codefile.parent.mkdir(parents=True, exist_ok=True)
            codefile.write_text(content)

        return dirname
