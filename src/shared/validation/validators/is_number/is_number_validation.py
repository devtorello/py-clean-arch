from typing import Type, Any
from src.shared.validation.contracts import FieldValidation
from src.shared.validation.errors import is_number_error


class IsNumberValidation(FieldValidation):
    """ Required Field Validation """

    field: str

    def __init__(self, field: str):
        super().__init__(field=field)
        self.field = field

    def validate(self, attribute: Any) -> Type[ValueError]:
        """ Execute required field validation """

        if isinstance(attribute[self.field], int):
            return None

        raise TypeError(is_number_error(self.field))
