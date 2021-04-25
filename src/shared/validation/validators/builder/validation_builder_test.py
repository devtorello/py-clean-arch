from src.shared.validation.validators.is_number.is_number_validation import (
    IsNumberValidation,
)
from src.shared.validation.validators.required_field import RequiredFieldValidation
from .validation_builder import ValidationBuilder


def test_validation_builder_required_param():
    """ Should return an array containing a RequiredFieldValidation """

    validations = ValidationBuilder.field("any_field").required().build()

    assert isinstance(validations[0], RequiredFieldValidation) is True


def test_validation_builder_is_number():
    """ Should return an array containing a RequiredFieldValidation """

    validations = ValidationBuilder.field("any_field").is_number().build()

    assert isinstance(validations[0], IsNumberValidation) is True
