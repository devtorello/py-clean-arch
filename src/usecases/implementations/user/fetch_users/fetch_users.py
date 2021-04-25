from typing import List, Type
from src.usecases.contracts import FetchUsers, UserRepositoryInterface
from src.entities import User


class FetchUsersUseCase(FetchUsers):
    """ Fetch User Usecase Implementation """

    def __init__(self, user_repository: Type[UserRepositoryInterface]):
        self.user_repository = user_repository

    def execute(self) -> List[User]:
        """Fetch registered users.
        : return - User instance list
        """

        return self.user_repository.fetch()
