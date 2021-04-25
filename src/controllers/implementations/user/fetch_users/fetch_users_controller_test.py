from faker import Faker
from pytest_mock import MockerFixture
from src.controllers.contracts.http_models import HttpRequest
from src.usecases.mocks import FetchUsersStub, UserRepositoryStub
from .fetch_users_controller import FetchUsersController

faker = Faker()


def make_sut():
    """ Make test SUT """

    user_repo_stub = UserRepositoryStub()
    fetch_users_stub = FetchUsersStub(user_repository=user_repo_stub)

    sut = FetchUsersController(fetch_users_usecase=fetch_users_stub)

    return {
        "sut": sut,
        "fetch_users_stub": fetch_users_stub,
    }


def test_fetch_users_success():
    """ Should return status 200 """

    sut_variables = make_sut()

    sut = sut_variables["sut"]

    response = sut.handle(HttpRequest())

    assert response.status_code == 200
    assert response.body is not None
    assert len(response.body) > 0


def test_find_user_controller_server_error(mocker: MockerFixture):
    """ Should return 500 """

    sut_variables = make_sut()

    sut, fetch_users_uc = sut_variables["sut"], sut_variables["fetch_users_stub"]

    mocker.patch.context_manager(fetch_users_uc, "execute", side_effect=Exception())

    response = sut.handle(HttpRequest())

    assert response.status_code == 500
    assert response.body["error"] is not None
