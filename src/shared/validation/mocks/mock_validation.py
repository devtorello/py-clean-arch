from src.shared.validation.errors.required_params_error import required_param_error
from typing import Any
from src.shared.validation.contracts import Validation


class ValidationStub(Validation):
    """ Validation Stub """

    def validate(self, attributes: Any) -> Exception:
        """ Validation Spy Implementation """

        if "valid_field" in attributes:
            return None

        raise ValueError(required_param_error("valid_field"))
