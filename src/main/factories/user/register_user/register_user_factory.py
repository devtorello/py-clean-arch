from src.controllers.contracts import Controller
from src.controllers.implementations.user.register_user import RegisterUserController
from src.usecases.implementations.user.register_user import RegisterUserUsecase
from src.repositories.implementations.user.user_repository import UserRepository
from .register_user_validations import register_user_validations


def register_user_factory() -> Controller:
    """ Creating Register User Controller """

    repository = UserRepository()
    use_case = RegisterUserUsecase(repository)
    validations = register_user_validations()
    register_user_controller = RegisterUserController(use_case, validations)

    return register_user_controller
