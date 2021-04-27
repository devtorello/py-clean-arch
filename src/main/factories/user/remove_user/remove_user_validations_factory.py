from typing import Type
from src.shared.validation.validators.builder import ValidationBuilder as Builder
from src.shared.validation.validators.composite import ValidatorComposite


def remove_user_validations() -> Type[ValidatorComposite]:
    """ Make Remove User Validations """

    arr_validations = [Builder.field("user_id").required().build()]

    validations = sum(arr_validations, [])

    return ValidatorComposite.build(validations)
