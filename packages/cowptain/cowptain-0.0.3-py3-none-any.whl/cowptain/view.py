from itertools import chain

from .const import Method, Status
from .headers import Headers
from .re import Request, Response


class View:
    def __init__(self, app):
        self.app = app

    def __call__(self, request: Request) -> Response:
        pass


class AutoView(View):
    def __call__(self, request: Request) -> Response:
        method_map = {
            Method.get: self.get,
            Method.post: self.post,
            Method.put: self.put,
            Method.patch: self.patch,
            Method.delete: self.delete,
            Method.options: self.options,
        }
        return method_map[request.method](request)

    def get(self, request: Request) -> Response:
        return self.not_implemented(request)

    def post(self, request: Request) -> Response:
        return self.not_implemented(request)

    def put(self, request: Request) -> Response:
        return self.not_implemented(request)

    def patch(self, request: Request) -> Response:
        return self.not_implemented(request)

    def delete(self, request: Request) -> Response:
        return self.not_implemented(request)

    def options(self, request: Request) -> Response:
        return self.not_implemented(request)

    def not_implemented(self, request: Request) -> Response:
        return Response(
            headers=Headers({}),
            status=Status.NotFound,
            body=[],
        )


class OptionsAutoView(AutoView):
    def options(self, request: Request) -> Response:
        func_names = {"get", "post", "put", "patch", "delete"}
        mro = self.__class__.mro()
        mro = filter(lambda c: issubclass(AutoView) and c is not AutoView, mro)
        class_dict_keys = map(lambda c: c.__dict__.keys(), mro)
        unique_keys = set(chain.from_iterable(class_dict_keys))

        implemented = {
            method for method in func_names if method in unique_keys
        }
        print(implemented)
        return Response(
            headers=Headers({}),
            status=Status.NotFound,
            body=[],
        )
