# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = configuration_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class File:
    name: str
    path: Optional[str] = None
    override: Optional[bool] = None
    pattern: Optional[str] = None
    replace: Optional[str] = None
    ignore_case: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'File':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        path = from_union([from_str, from_none], obj.get("path"))
        override = from_union([from_bool, from_none], obj.get("override"))
        pattern = from_union([from_str, from_none], obj.get("pattern"))
        replace = from_union([from_str, from_none], obj.get("replace"))
        ignore_case = from_union([from_bool, from_none], obj.get("ignore_case"))
        return File(name, path, override, pattern, replace, ignore_case)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["path"] = from_union([from_str, from_none], self.path)
        result["override"] = from_union([from_bool, from_none], self.override)
        result["pattern"] = from_union([from_str, from_none], self.pattern)
        result["replace"] = from_union([from_str, from_none], self.replace)
        result["ignore_case"] = from_union([from_bool, from_none], self.ignore_case)
        return result


@dataclass
class Action:
    name: str
    files: List[File]

    @staticmethod
    def from_dict(obj: Any) -> 'Action':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        files = from_list(File.from_dict, obj.get("files"))
        return Action(name, files)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["files"] = from_list(lambda x: to_class(File, x), self.files)
        return result


@dataclass
class Project:
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Project':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        return Project(name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        return result


@dataclass
class PullRequest:
    name: str
    branch: str

    @staticmethod
    def from_dict(obj: Any) -> 'PullRequest':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        branch = from_str(obj.get("branch"))
        return PullRequest(name, branch)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["branch"] = from_str(self.branch)
        return result


@dataclass
class Repository:
    default_branch: str
    pattern: str
    ignore_case: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Repository':
        assert isinstance(obj, dict)
        default_branch = from_str(obj.get("default_branch"))
        pattern = from_str(obj.get("pattern"))
        ignore_case = from_bool(obj.get("ignore_case"))
        return Repository(default_branch, pattern, ignore_case)

    def to_dict(self) -> dict:
        result: dict = {}
        result["default_branch"] = from_str(self.default_branch)
        result["pattern"] = from_str(self.pattern)
        result["ignore_case"] = from_bool(self.ignore_case)
        return result


@dataclass
class Configuration:
    project: Project
    pull_request: PullRequest
    repository: Repository
    assets_directory: str
    actions: List[Action]

    @staticmethod
    def from_dict(obj: Any) -> 'Configuration':
        assert isinstance(obj, dict)
        project = Project.from_dict(obj.get("project"))
        pull_request = PullRequest.from_dict(obj.get("pull_request"))
        repository = Repository.from_dict(obj.get("repository"))
        assets_directory = from_str(obj.get("assets_directory"))
        actions = from_list(Action.from_dict, obj.get("actions"))
        return Configuration(project, pull_request, repository, assets_directory, actions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["project"] = to_class(Project, self.project)
        result["pull_request"] = to_class(PullRequest, self.pull_request)
        result["repository"] = to_class(Repository, self.repository)
        result["assets_directory"] = from_str(self.assets_directory)
        result["actions"] = from_list(lambda x: to_class(Action, x), self.actions)
        return result


def configuration_from_dict(s: Any) -> Configuration:
    return Configuration.from_dict(s)


def configuration_to_dict(x: Configuration) -> Any:
    return to_class(Configuration, x)