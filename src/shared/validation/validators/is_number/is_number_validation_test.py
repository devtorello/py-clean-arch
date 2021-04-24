from .is_number_validation import IsNumberValidation

FIELD = "valid_field"


def test_is_number_validation_valid():
    """ Should validate if field value is number """

    sut = IsNumberValidation(FIELD)

    error = sut.validate({FIELD: 1})

    assert error is None
