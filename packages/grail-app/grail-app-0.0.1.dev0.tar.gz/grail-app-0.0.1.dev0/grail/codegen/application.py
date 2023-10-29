from typing import Any
from typing import Generic, Sequence
import enum
from pydantic import BaseModel
from .base import Base, MM


# --------------------------------------
# Application MetaModel (Frontend)


class DataTypeKind(str, enum.Enum):
    FLOAT = "float"
    INT = "int"
    STRING = "string"
    DATE = "date"
    DATETIME = "datetime"
    TIME = "time"
    BOOLEAN = "boolean"
    ENUM = "enum"
    JSON = "json"
    UUID = "uuid"
    URL = "url"
    EMAIL = "email"
    PASSWORD = "password"
    FILE = "file"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    HTML = "html"
    MARKDOWN = "markdown"
    BB_CODE = "bb_code"
    XML = "xml"
    YAML = "yaml"
    TOML = "toml"
    CSV = "csv"
    TSV = "tsv"


class DataType(Base):
    kind: DataTypeKind = DataTypeKind.STRING


class Attribute(Base):
    datatype: DataType = DataType(kind=DataTypeKind.STRING)
    default: Any | None = None
    validators: list[Any] = []


class RelationshipKind(enum.Enum):
    ONE_TO_ONE = "one_to_one"
    ONE_TO_MANY = "one_to_many"
    MANY_TO_ONE = "many_to_one"
    MANY_TO_MANY = "many_to_many"


class Relationship(Base):
    kind: RelationshipKind
    model: str


class Model(Base):
    attributes: list[Attribute] = []
    relationships: list[Relationship] = []


class Action(Base):
    parameters: dict[str, Model | str] = {}
    body: str
    result: Model | None = None


class Query(Base):
    args: list[Model]
    result: Any | None


class Permission(Base):
    pass


class Page(Base):
    pass


class BREADPage(Page):
    class Browse(BaseModel):
        columns: list[str] = []
        filters: list[str] = []
        actions: list[Action] = []
        search: list[str] = []
        order_by: list[str] = []
        page_size: int = 100
        template: str = ""

    class Read(BaseModel):
        columns: list[str] = []
        actions: list[Action] = []
        template: str = ""

    class Edit(BaseModel):
        columns: list[str] = []
        actions: list[Action] = []
        template: str = ""

    class Add(BaseModel):
        columns: list[str] = []
        actions: list[Action] = []
        template: str = ""

    class Delete(BaseModel):
        confirm: str = "Are you sure you want to delete this item?: {model.name}"
        template: str = ""

    model: str
    browse: Browse | None = Browse()
    read: Read | None = Read()
    edit: Edit | None = Edit()
    add: Add | None = Add()
    delete: Delete | None = Delete()


class Event(Base):
    pass


class DataModel(Generic[MM], Base):
    models: Sequence[MM]


class PageModel(Generic[MM], Base):
    pages: Sequence[MM]


class ActionModel(Generic[MM], Base):
    actions: Sequence[MM]


class QueryModel(Generic[MM], Base):
    queries: Sequence[MM]


class EventModel(Generic[MM], Base):
    events: Sequence[MM]


class Application(Base):
    datamodel: DataModel[Model]
    pagemodel: PageModel[Page]
    actionmodel: ActionModel[Action]
    querymodel: QueryModel[Query]
    eventmodel: EventModel[Event]
