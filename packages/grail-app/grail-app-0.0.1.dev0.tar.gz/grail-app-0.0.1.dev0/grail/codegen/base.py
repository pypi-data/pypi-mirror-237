from pydantic import BaseModel
from typing import TypeVar, Any, Generic, Callable
import subclass_register

MM = TypeVar("MM")
M = TypeVar("M")


models = subclass_register.SubclassRegister("Model")
generators = subclass_register.SubclassRegister("Generator")


@models.link_base
class Base(BaseModel):
    name: str = ""
    description: str = ""

    class Config:
        orm_mode = True
        frozen = True

    @classmethod
    def from_yaml(cls, data: str) -> Any:
        return from_yaml(cls, data)

    def to_yaml(self) -> str:
        return to_yaml(self)

    @classmethod
    def schema_yaml(cls) -> str:
        yaml = YAML()
        yaml.default_flow_style = False
        f = StringIO()
        yaml.dump(cls.schema(), f)
        return f.getvalue()


@generators.link_base
class Generator(Generic[MM, M], BaseModel):
    name: str = ""
    description: str = ""

    class Config:
        orm_mode = True
        frozen = True

    def generate(self, inp: MM) -> M:
        raise NotImplementedError

    def __call__(self, m: MM) -> M:
        return self.generate(m)

    def __rshift__(self, other: "Generator[M, Any]") -> "Generator[MM, Any]":
        @generators.skip
        class NewGenerator(Generator[MM, Any]):
            def generate(s, inp: MM) -> Any:
                return other.generate(self.generate(inp))

        return NewGenerator(name=f"{self.name} | {other.name}")


class Function(Generator[MM, M]):
    name: str = ""
    description: str = ""
    func: Callable[[MM], M] | str

    def generate(self, inp: MM) -> M:
        match self.func:
            case str():
                import importlib

                mod = importlib.import_module(".".join(self.func.split(".")[:-1]))
                func: Callable[[MM], M] = getattr(mod, self.func.split(".")[-1])
                self.func = func
            case _ if not callable(self.func):
                raise ValueError(f"Invalid function: {self.func}")

        return self.func(inp)


from ruamel.yaml import YAML
from io import StringIO
from pydantic import BaseModel
from typing import Any


def to_yaml(obj: BaseModel) -> str:
    yaml = YAML()
    yaml.default_flow_style = False
    f = StringIO()
    yaml.dump(obj.dict(), f)
    return f.getvalue()


def from_yaml(cls: type, data: str) -> Any:
    yaml = YAML()
    data_dict: dict[str, Any] = yaml.load(data)
    return cls(**data_dict)
