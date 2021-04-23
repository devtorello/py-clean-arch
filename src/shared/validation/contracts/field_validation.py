from abc import ABC, abstractmethod


class FieldValidation(ABC):
    """ Interface to Validation """

    field: str

    def __init__(self, field: str):
        self.field = field

    @abstractmethod
    def validate(self, attribute: str) -> Exception:
        """ abstractmethod """

        raise Exception("Method not Implemented: FieldValidation")
