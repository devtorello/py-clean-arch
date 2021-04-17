import pytest
from .required_field_validation import RequiredFieldValidation
from src.shared.validation.errors import GeneralException

FIELD = "valid_field"


def test_required_field_validation_valid():
    """ Testing case of success to Required Field Validation """

    sut = RequiredFieldValidation(FIELD)

    error = sut.validate({"valid_field": "any_value"})

    assert error is None


def test_required_field_validation_invalid():
    """ Testing case of failure to Required Field Validation """

    sut = RequiredFieldValidation(FIELD)

    with pytest.raises(GeneralException) as execinfo:
        error = sut.validate({"invalid_field": "any_value"})

        # raise GeneralException({"error": f"Missing Param: {FIELD}"})

        assert execinfo.value == error
