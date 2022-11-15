# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = repository_from_dict(json.loads(json_string))

from dataclasses import dataclass
from uuid import UUID
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Repository:
    id: UUID
    name: str
    remote_url: str

    @staticmethod
    def from_dict(obj: Any) -> 'Repository':
        assert isinstance(obj, dict)
        id = UUID(obj.get("id"))
        name = from_str(obj.get("name"))
        remote_url = from_str(obj.get("remoteUrl"))
        return Repository(id, name, remote_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = str(self.id)
        result["name"] = from_str(self.name)
        result["remoteUrl"] = from_str(self.remote_url)
        return result


def repository_from_dict(s: Any) -> Repository:
    return Repository.from_dict(s)


def repository_to_dict(x: Repository) -> Any:
    return to_class(Repository, x)
