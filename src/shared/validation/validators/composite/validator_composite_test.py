import pytest
from src.shared.validation.validators.required_field import RequiredFieldValidation
from src.shared.validation.errors import GeneralException
from .validator_composite import ValidatorComposite


def test_validator_composite_success():
    """ Should return null validations does not fail """

    sut = ValidatorComposite.build([RequiredFieldValidation("any_field")])

    validations = sut.validate({"any_field": "any_value"})

    assert validations is None


def test_validator_composite_failure():
    """ Should return null validations fail """

    sut = ValidatorComposite.build([RequiredFieldValidation("any_field")])

    with pytest.raises(GeneralException) as execinfo:
        validations = sut.validate({"invalid_field": "any_value"})

        assert execinfo.value == validations
