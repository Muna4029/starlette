from __future__ import annotations

from typing import Any, Iterator

from starlette.types import ASGIApp, Receive, Scope, Send


class _MiddlewareClass:
    def __init__(self, app: ASGIApp, **kwargs: Any) -> None:
        ...  # pragma: no cover

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        ...  # pragma: no cover


class Middleware:
    def __init__(self, cls: type, **options: Any) -> None:
        self.cls = cls
        self.options = options

    def __iter__(self) -> Iterator[Any]:
        as_tuple = (self.cls, self.options)
        return iter(as_tuple)

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        option_strings = [f"{key}={value!r}" for key, value in self.options.items()]
        args_repr = ", ".join([self.cls.__name__] + option_strings)
        return f"{class_name}({args_repr})"
