from typing import Type
from src.usecases.contracts import RegisterUser
from src.controller.contracts import HttpRequest, HttpResponse, Controller
from src.shared.validation.contracts import Validation
from src.controller.errors import HttpErrors


class RegisterUserController(Controller):
    """ Class to define controller to register_user use case """

    def __init__(
        self, register_user_usecase: Type[RegisterUser], validation: Type[Validation]
    ):
        self.register_user_usecase = register_user_usecase
        self.validation = validation

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Method to call usecase """

        try:
            body = http_request.body

            error = self.validation.validate(body)

            response = None

            if error is None:
                response = self.register_user_usecase.execute(
                    username=body["username"], password=body["password"]
                )

            if response["success"] is False:
                error = HttpErrors.unprocessable_entity()

                return HttpResponse(
                    status_code=error["status_code"], body=error["body"]
                )

            return HttpResponse(status_code=200, body=response["data"])
        except ValueError as except_error:
            error = HttpErrors.bad_request(str(except_error))

            return HttpResponse(status_code=error["status_code"], body=error["body"])
        except Exception as except_error:
            error = HttpErrors.server_error(str(except_error))

            return HttpResponse(status_code=error["status_code"], body=error["body"])
