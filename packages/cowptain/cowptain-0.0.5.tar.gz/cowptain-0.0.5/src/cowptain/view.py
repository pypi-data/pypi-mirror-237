from abc import ABC, abstractmethod

from .re import Request, Response


class View(ABC):
    def __init__(self, app):
        self.app = app

    @abstractmethod
    def __call__(self, request: Request) -> Response:
        pass
