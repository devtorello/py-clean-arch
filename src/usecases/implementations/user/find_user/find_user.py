from typing import Type
from src.usecases.contracts import FindUser, UserRepositoryInterface
from src.entities import User


class FindUserUseCase(FindUser):
    """ Find User Usecase Implementation """

    def __init__(self, user_repository: Type[UserRepositoryInterface]):
        self.user_repository = user_repository

    def execute(self, user_id: int) -> User:
        """Find a registered user.
        : param - user_id: Registered user's id
        : return - User instance
        """

        return self.user_repository.find(user_id)
