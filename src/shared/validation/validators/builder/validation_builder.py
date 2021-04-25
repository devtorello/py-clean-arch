from __future__ import annotations
from typing import List
from src.shared.validation.contracts import FieldValidation
from src.shared.validation.validators.required_field import RequiredFieldValidation
from src.shared.validation.validators.is_number import IsNumberValidation


class ValidationBuilder:
    """ Validation Builder Class """

    def __init__(self, field_name: str, validations: List):
        self.field_name = field_name
        self.validations = validations

    @classmethod
    def field(cls, field_name: str) -> ValidationBuilder:
        """ Return new ValidationBuilder instance for the given field """

        return cls(field_name=field_name, validations=[])

    def required(self) -> ValidationBuilder:
        """ Verify required fields """

        self.validations.append(RequiredFieldValidation(field=self.field_name))

        return self

    def is_number(self) -> ValidationBuilder:
        """ Verify if param is number """

        self.validations.append(IsNumberValidation(field=self.field_name))

        return self

    def build(self) -> List[FieldValidation]:
        """ Build Validation Builder """

        return self.validations
