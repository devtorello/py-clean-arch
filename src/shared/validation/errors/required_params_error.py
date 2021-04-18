def required_param_error(field: str) -> str:
    """ Return a required param error factory """

    return f"Missing param: {field}"
