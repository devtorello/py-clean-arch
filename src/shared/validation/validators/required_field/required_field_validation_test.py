import pytest
from src.shared.validation.errors import required_param_error
from .required_field_validation import RequiredFieldValidation

FIELD = "valid_field"


def test_required_field_validation_valid():
    """ Testing case of success to Required Field Validation """

    sut = RequiredFieldValidation(FIELD)

    error = sut.validate({"valid_field": "any_value"})

    assert error is None


def test_required_field_validation_invalid():
    """ Testing case of failure to Required Field Validation """

    sut = RequiredFieldValidation(FIELD)

    with pytest.raises(Exception) as execinfo:
        sut.validate({"invalid_field": "any_value"})

        assert execinfo == required_param_error(FIELD)
