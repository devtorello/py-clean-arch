from src.controllers.contracts import Controller
from src.controllers.implementations.user.remove_user import RemoveUserController
from src.usecases.implementations.user.remove_user import RemoveUserUseCase
from src.repositories.implementations.user.user_repository import UserRepository
from .remove_user_validations_factory import remove_user_validations


def remove_user_factory() -> Controller:
    """ Creating Remove User Controller """

    repository = UserRepository()
    use_case = RemoveUserUseCase(repository)
    validations = remove_user_validations()
    controller = RemoveUserController(use_case, validations)

    return controller
