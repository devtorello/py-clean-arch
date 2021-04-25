from src.controllers.contracts import Controller
from src.controllers.implementations.user.fetch_users import FetchUsersController
from src.usecases.implementations.user.fetch_users import FetchUsersUseCase
from src.repositories.implementations.user.user_repository import UserRepository


def fetch_users_factory() -> Controller:
    """ Creating Fetch Users Controller """

    repository = UserRepository()
    use_case = FetchUsersUseCase(repository)
    controller = FetchUsersController(use_case)

    return controller
