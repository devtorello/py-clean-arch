from typing import Type, Dict
from src.usecases.contracts import RegisterUser, UserRepositoryInterface
from src.entities import User


class RegisterUserUsecase(RegisterUser):
    """ Register User Usecase Implementation """

    def __init__(self, user_repository: Type[UserRepositoryInterface]):
        self.user_repository = user_repository

    def execute(self, username: str, password: str) -> Dict[bool, User]:
        """Register an user in our application.
        : param - username: User's username in our application
                - password: User's password in our application
        : return - dictionary containing information about the proccess
        """

        result = None
        validate_entry = isinstance(username, str) and isinstance(password, str)

        if validate_entry:
            result = self.user_repository.insert(username, password)

        return {"Success": validate_entry, "Data": result}
