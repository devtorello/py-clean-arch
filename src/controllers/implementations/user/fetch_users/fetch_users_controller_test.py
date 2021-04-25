from faker import Faker
from src.controllers.contracts.http_models import HttpRequest
from src.usecases.mocks import FetchUsersStub, UserRepositoryStub
from .fetch_users_controller import FetchUsersController

faker = Faker()


def make_sut():
    """ Make test SUT """

    user_repo_stub = UserRepositoryStub()
    fetch_user_stub = FetchUsersStub(user_repository=user_repo_stub)

    sut = FetchUsersController(fetch_users_usecase=fetch_user_stub)

    return {
        "sut": sut,
        "fetch_user_stub": fetch_user_stub,
    }


def test_fetch_users_success():
    """ Should return status 200 """

    sut_variables = make_sut()

    sut = sut_variables["sut"]

    response = sut.handle(HttpRequest())

    assert response.status_code == 200
    assert response.body is not None
    assert len(response.body) > 0
