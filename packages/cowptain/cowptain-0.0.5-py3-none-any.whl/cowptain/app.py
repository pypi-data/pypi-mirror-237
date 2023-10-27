from collections.abc import Callable

from .path import Path
from .re import Request
from .routing import Node, Route
from .view import View


class Application:
    def __init__(self):
        self._root = Node()

    def add_route(self, path: str, view: type[View]):
        route = Route(Path(path), view(self))
        self._root.add(route)

    def __call__(self, environ: dict, start_response: Callable) -> list[bytes]:
        path = self._get_path(environ)
        route = self._find_route(path)
        request = self._prepare_request(environ, route)

        response = route.view(request)

        status = str(response.status)
        headers = list(response.headers.items())
        start_response(status, headers)

        return response.body

    def _get_path(self, envirion: dict) -> Path:
        return Path(envirion["PATH_INFO"])

    def _find_route(self, path: Path):
        return self._root.match(path)

    def _prepare_request(self, envirion, route) -> Request:
        return Request.from_environ(envirion, route)
