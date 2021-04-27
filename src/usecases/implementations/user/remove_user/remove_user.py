from typing import Type
from src.usecases.contracts.user_repository import UserRepositoryInterface
from src.usecases.contracts import RemoveUser


class RemoveUserUseCase(RemoveUser):
    """ Remove User Usecase Implementation """

    def __init__(self, user_repository: Type[UserRepositoryInterface]):
        self.user_repository = user_repository

    def execute(self, user_id: int) -> bool:
        """Remove an user from our application.
        : param - user_id: User's unique id
        : return - status of success
        """

        user_removal = self.user_repository.remove(user_id=user_id)

        return {"users_removed": user_removal}
