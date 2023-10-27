from operator import itemgetter, methodcaller

from .utils import ReadOnlyDict


class Headers(ReadOnlyDict):
    def __init__(self, headers: dict):
        """
        HTTP_HEADER_A -> Header-A
        HeaDer-B -> Header-B
        header-c -> Header-C
        http_heaDER-D -> Header-D
        """
        data = list(headers.items())
        keys = map(itemgetter(0), data)
        values = map(itemgetter(1), data)
        keys = map(methodcaller("replace", "_", "-"), keys)
        keys = map(methodcaller("title"), keys)
        keys = map(methodcaller("removeprefix", "Http-"), keys)
        items = zip(keys, values)

        super().__init__(dict(items))


class Cookies(ReadOnlyDict):
    def __init__(self, cookie_string: str):
        if not cookie_string:
            super().__init__()
            return

        cookies = map(methodcaller("strip"), cookie_string.split(";"))
        data = dict(map(lambda c: c.split("="), cookies))

        super().__init__(data)
