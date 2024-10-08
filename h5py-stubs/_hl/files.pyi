from typing import Any, Literal

from .group import Group

class File(Group):
    def __init__(self, name: str, mode: Literal["w", "r", "r+", "a", "w-"] = "r", **kwargs: Any)
    def close(self) -> None: ...
    def __enter__(self) -> File: ...
    def __exit__(self, *args: Any) -> None: ...
    @property
    def filename(self) -> str: ...
    def flush(self) -> None: ...
