class HttpErrors:
    """ Class to define errors in http """

    @staticmethod
    def unprocessable_entity():
        """ HTTP 422: Unprocessable Entity """

        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}

    @staticmethod
    def bad_request(error: str):
        """ HTTP 400: Bad Request """

        return {"status_code": 400, "body": {"error": error}}

    @staticmethod
    def conflict_error():
        """ HTTP 409: Conflict Error """

        return {"status_code": 409, "body": {"error": "Conflict"}}

    @staticmethod
    def server_error(error: str):
        """ HTTP 500: Internal Server Error """

        return {"status_code": 500, "body": {"error": error}}
