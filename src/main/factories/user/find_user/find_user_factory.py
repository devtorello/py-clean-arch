from src.controllers.contracts import Controller
from src.controllers.implementations.user.find_user import FindUserController
from src.usecases.implementations.user.find_user import FindUserUseCase
from src.repositories.implementations.user.user_repository import UserRepository
from .find_user_validations_factory import find_user_validations


def find_user_factory() -> Controller:
    """ Creating Find User Controller """

    repository = UserRepository()
    use_case = FindUserUseCase(repository)
    validations = find_user_validations()
    register_user_controller = FindUserController(use_case, validations)

    return register_user_controller
