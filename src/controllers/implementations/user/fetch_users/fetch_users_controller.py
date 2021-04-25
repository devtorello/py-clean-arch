from typing import Type
from src.usecases.contracts import FetchUsers
from src.controllers.contracts import Controller, HttpRequest, HttpResponse
from src.controllers.errors import HttpErrors


class FetchUsersController(Controller):
    """ Class to define controller to fetch_users use case """

    def __init__(self, fetch_users_usecase: Type[FetchUsers]):
        self.fetch_users_usecase = fetch_users_usecase

    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        """ Method to call usecase """

        try:
            response = self.fetch_users_usecase.execute()

            return HttpResponse(status_code=200, body=response)
        except Exception as except_error:
            error = HttpErrors.server_error(str(except_error))

            return HttpResponse(status_code=error["status_code"], body=error["body"])
