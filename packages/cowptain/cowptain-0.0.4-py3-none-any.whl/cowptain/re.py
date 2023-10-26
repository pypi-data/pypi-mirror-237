from collections.abc import Iterable
from dataclasses import dataclass

from .const import Method, Status
from .headers import Cookies, Headers
from .path import Path, Query, Vars


class Input:
    def __init__(self, wsgi_input, content_length):
        self._wsgi_input = wsgi_input
        self._content_length = content_length
        self._read = 0

    def read(self, size=None) -> bytes:
        left_to_read = self._content_length - self._read

        if not left_to_read > 0:
            return b""

        if size is None or size > left_to_read:
            size = left_to_read

        self._read += size
        return self._wsgi_input.read(size)


@dataclass(frozen=True)
class Request:
    method: Method
    headers: Headers
    cookies: Cookies
    path: Path
    vars: Vars
    query: Query
    input: Input

    @classmethod
    def from_environ(cls, environ, route):
        method = Method(environ["REQUEST_METHOD"])
        headers = {
            key.removeprefix("HTTP_"): value
            for key, value in environ.items()
            if key.startswith("HTTP_")
        }
        if content_type := environ.get("CONTENT_TYPE"):
            headers["content-type"] = content_type

        if content_length := environ.get("CONTENT_LENGTH"):
            headers["content-length"] = content_length

        headers = Headers(headers)
        cookies = Cookies(environ.get("HTTP_COOKIE", ""))

        query = environ.get("QUERY_STRING", "")
        query = Query(query)
        path = environ.get("PATH_INFO")

        path = Path(path)
        vars = Vars(path=path, pattern=route.path)

        wsgi_input = environ["wsgi.input"]
        content_length = int(environ.get("CONTENT_LENGTH") or "0")

        input = Input(wsgi_input, content_length)

        return cls(
            method=method,
            headers=headers,
            cookies=cookies,
            path=path,
            vars=vars,
            query=query,
            input=input,
        )


@dataclass(frozen=True)
class Response:
    headers: Headers
    status: Status
    body: Iterable[bytes]
