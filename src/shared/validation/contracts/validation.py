from typing import Any
from abc import ABC, abstractmethod


class Validation(ABC):
    """ Interface to Validation """

    @abstractmethod
    def validate(self, attributes: Any) -> Exception:
        """ abstractmethod """

        raise Exception("Method not Implemented: Validation")
