from typing import Type
from src.shared.validation.validators.builder import ValidationBuilder as Builder
from src.shared.validation.validators.composite import ValidatorComposite


def register_user_validations() -> Type[ValidatorComposite]:
    """ Make Register User Validations """

    arr_validations = [
        Builder.field("username").required().build(),
        Builder.field("password").required().build(),
    ]

    validations = sum(arr_validations, [])

    return ValidatorComposite.build(validations)
