import pytest
from src.shared.validation.errors.is_number_error import is_number_error
from .is_number_validation import IsNumberValidation

FIELD = "valid_field"


def test_is_number_validation_valid():
    """ Should validate if field value is number """

    sut = IsNumberValidation(FIELD)

    error = sut.validate({FIELD: 1})

    assert error is None


def test_required_field_validation_invalid():
    """ Should throws if field value is not a number """

    sut = IsNumberValidation(FIELD)

    with pytest.raises(TypeError) as execinfo:
        sut.validate({FIELD: "1"})

        assert execinfo == is_number_error(FIELD)
