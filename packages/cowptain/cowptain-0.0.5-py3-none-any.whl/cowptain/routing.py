from collections import defaultdict
from dataclasses import dataclass

from .errors import CowptainError
from .path import Path
from .view import View


@dataclass(frozen=True)
class Route:
    path: Path
    view: View

    def __str__(self):
        view_classname = self.view.__class__.__name__
        return f"{self.path} -> {view_classname}"


class Node:
    def __init__(self):
        self.route = None
        self.paths = defaultdict(Node)

    def add(self, route: Route):
        return self._inner_add(route, route.path)

    def _inner_add(self, route: Route, path: Path):
        if not path and self.route:
            raise CowptainError()

        if not path:
            self.route = route
            return

        part, rest = str(path[:1]), path[1:]
        if part.strip("/").startswith("<"):
            part = "*"

        self.paths[str(part)]._inner_add(route, rest)

    def match(self, path: Path):
        if not path and not self.route:
            raise CowptainError()

        if not path:
            return self.route

        part, rest = path[:1], path[1:]

        if str(part) in self.paths:
            return self.paths[str(part)].match(rest)

        if "*" in self.paths:
            return self.paths["*"].match(rest)

        raise CowptainError()

    def __str__(self):
        result = [f"Route: {self.route}"]
        for path, node in self.paths.items():
            node_str = str(node)
            node_lines = node_str.split("\n")
            node_lines[0] = f"{path}: {node_lines[0]}"
            node_lines = map(lambda line: f"    {line}", node_lines)
            result += node_lines
        return "\n".join(result)
