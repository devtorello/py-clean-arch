from typing import Type
from src.usecases.contracts import RemoveUser
from src.controllers.contracts import Controller, HttpRequest, HttpResponse
from src.shared.validation.contracts import Validation
from src.controllers.errors import HttpErrors


class RemoveUserController(Controller):
    """ Class to define controller to remove_user use case """

    def __init__(self, remove_user_uc: Type[RemoveUser], validation: Type[Validation]):
        self.remove_user_uc = remove_user_uc
        self.validation = validation

    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        """ Method to call usecase and validation """

        try:
            params = http_request.query

            error = self.validation.validate(params)

            response = None
            if error is None:
                user_id = params["user_id"]
                response = self.remove_user_uc.execute(user_id=int(user_id))

            return HttpResponse(status_code=200, body=response)
        except ValueError as except_error:
            error = HttpErrors.bad_request(str(except_error))

            return HttpResponse(status_code=error["status_code"], body=error["body"])
        except Exception as except_error:
            error = HttpErrors.server_error(str(except_error))

            return HttpResponse(status_code=error["status_code"], body=error["body"])
