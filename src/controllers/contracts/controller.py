from typing import Type
from abc import ABC, abstractmethod
from .http_models import HttpRequest, HttpResponse


class Controller(ABC):
    """ Interface to Route Adapter """

    @abstractmethod
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Defining Route Handle """

        raise Exception("Should implement Controller method: Handle")
