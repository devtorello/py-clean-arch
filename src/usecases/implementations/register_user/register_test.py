from faker import Faker
from src.usecases.mocks import UserRepositoryStub
from .register import RegisterUserUsecase

faker = Faker()


def test_register_user():
    """ Testing registry usecase """

    user_repo = UserRepositoryStub()
    register_user_uc = RegisterUserUsecase(user_repo)

    attributes = {"username": faker.name(), "password": faker.name()}

    result = register_user_uc.execute(
        username=attributes["username"], password=attributes["password"]
    )

    # Testing Input
    assert user_repo.insert_user_params["username"] == attributes["username"]
    assert user_repo.insert_user_params["password"] == attributes["password"]

    # Testing Output
    assert result["Success"] is True
    assert result["Data"] is not None


def test_register_user_fail():
    """ Testing registry usecase when it fails """

    user_repo = UserRepositoryStub()
    register_user_uc = RegisterUserUsecase(user_repo)

    attributes = {"username": faker.random_number(), "password": faker.name()}

    result = register_user_uc.execute(
        username=attributes["username"], password=attributes["password"]
    )

    # Testing Input
    assert user_repo.insert_user_params == {}

    # Testing Output
    assert result["Success"] is False
    assert result["Data"] is None
