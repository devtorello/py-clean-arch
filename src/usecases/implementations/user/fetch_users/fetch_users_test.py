from faker import Faker
from pytest_mock.plugin import MockerFixture
from src.entities.user import User
from src.usecases.mocks import UserRepositoryStub
from .fetch_users import FetchUsersUseCase

faker = Faker()


def make_sut():
    """ Make test SUT """

    user_repo = UserRepositoryStub()
    fetch_users_uc = FetchUsersUseCase(user_repo)

    return {"sut": fetch_users_uc, "user_repo": user_repo}


def test_fetch_user():
    """ Should fetch users """

    sut_variables = make_sut()

    sut = sut_variables["sut"]

    result = sut.execute()

    assert result is not None
    assert isinstance(result, list)
    assert isinstance(result[0], User)
    assert len(result) > 0


def test_fetch_user_empty_list(mocker: MockerFixture):
    """ Should fetch users and return empty list if there is no user """

    sut_variables = make_sut()

    sut, user_repo = sut_variables["sut"], sut_variables["user_repo"]

    mocker.patch.context_manager(user_repo, "fetch", return_value=[])

    result = sut.execute()

    assert result is not None
    assert isinstance(result, list)
    assert len(result) == 0
