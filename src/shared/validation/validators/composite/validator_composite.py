from __future__ import annotations
from typing import List
from src.shared.validation.contracts import Validation, FieldValidation


class ValidatorComposite(Validation):
    """ Validator Composite Class """

    def __init__(self, validators: List[FieldValidation]):
        self.validators = validators

    @classmethod
    def build(cls, validators: List[FieldValidation]) -> ValidatorComposite:
        """ Build Validator Composite """

        return cls(validators=validators)

    def validate(self, attributes) -> Exception:
        """ Validate Validators """

        for validator in self.validators:
            exception = validator.validate(attributes)

            if exception:
                return exception

        return None
