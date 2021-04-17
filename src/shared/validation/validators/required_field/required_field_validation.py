from typing import Type, Any
from src.shared.validation.contracts import FieldValidation
from src.shared.validation.errors import GeneralException


class RequiredFieldValidation(FieldValidation):
    """ Required Field Validation """

    field: str

    def __init__(self, field: str):
        super().__init__(field=field)
        self.field = field

    def validate(self, attribute: Any) -> Type[GeneralException]:
        """ Execute required field validation """

        if self.field in attribute:
            return None

        raise GeneralException(f"Missing Param: {self.field}")
