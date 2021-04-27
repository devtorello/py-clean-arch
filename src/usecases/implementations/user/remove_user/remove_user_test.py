from faker import Faker
from pytest_mock.plugin import MockerFixture
from src.usecases.mocks import UserRepositoryStub
from .remove_user import RemoveUserUseCase

faker = Faker()


def make_sut():
    """ Make test SUT """

    user_repo = UserRepositoryStub()
    remove_user_uc = RemoveUserUseCase(user_repo)

    return {"sut": remove_user_uc, "user_repo": user_repo}


def test_remove_user_success():
    """ Should remove user """

    sut_variables = make_sut()

    sut, user_repo = sut_variables["sut"], sut_variables["user_repo"]

    user_id = faker.random_number()

    result = sut.execute(user_id=user_id)

    assert user_repo.remove_user_params["user_id"] == user_id
    assert result["users_removed"] == 1


def test_remove_user_failure(mocker: MockerFixture):
    """ Should return 0 if user was not removed or found """

    sut_variables = make_sut()

    sut, user_repo = sut_variables["sut"], sut_variables["user_repo"]

    mocker.patch.context_manager(user_repo, "remove", return_value=0)

    user_id = faker.random_number()

    result = sut.execute(user_id=user_id)

    assert result["users_removed"] == 0
