from re import fullmatch

from .errors import CowptainError
from .utils import ReadOnlyDict


class Path:
    def __init__(self, path):
        self._parts = []
        path = path.strip("/")

        if path:
            self._parts = path.split("/")

    def __getitem__(self, index: int | slice) -> "Path":
        path = self._parts[index]

        if isinstance(index, slice):
            path = "/".join(path)

        path = "/" + path
        return Path(path)

    def __len__(self):
        return len(self._parts)

    def __iter__(self):
        return iter(self._parts)

    def __str__(self):
        path = "/".join(self._parts)
        return "/" + path

    def __eq__(self, other):
        if not isinstance(other, Path):
            return False

        return self._parts == other._parts

    def __repr__(self):
        arg = self.__str__()
        return f'Path("{arg}")'


class Vars(ReadOnlyDict):
    def __init__(self, path: Path, pattern: Path):
        strpath = str(path)
        strpattern = str(pattern)

        strpattern = strpattern.replace("<", "(?P<")
        strpattern = strpattern.replace(">", ">[a-zA-Z0-9]+)")

        match = fullmatch(strpattern, strpath)
        if not match:
            raise CowptainError("shouldn't happen")

        super().__init__(match.groupdict())


class Query(ReadOnlyDict):
    def __init__(self, query: str):
        if not query:
            super().__init__()
            return

        params = query.split("&")

        def split_param(param):
            parts = param.split("=")
            if len(parts) == 1:
                parts = [parts[0], ""]
            return parts

        data = dict(map(split_param, params))
        super().__init__(data)
