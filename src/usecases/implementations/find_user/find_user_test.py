import pytest
from faker import Faker
from pytest_mock.plugin import MockerFixture
from sqlalchemy.orm.exc import NoResultFound
from src.entities.user import User
from src.usecases.mocks import UserRepositoryStub
from .find_user import FindUserUseCase

faker = Faker()


def make_sut():
    """ Make test SUT """

    user_repo = UserRepositoryStub()
    find_user_uc = FindUserUseCase(user_repo)

    return {"sut": find_user_uc, "user_repo": user_repo}


def test_find_user():
    """ Should find user """

    sut_variables = make_sut()

    sut, user_repo = sut_variables["sut"], sut_variables["user_repo"]

    user_id = faker.random_number()

    result = sut.execute(user_id)

    assert user_repo.find_user_params["id"] == user_id

    assert result is not None
    assert isinstance(result, User)


def test_find_user_not_fond(mocker: MockerFixture):
    """ Should return None if user does not exists """

    sut_variables = make_sut()

    sut, user_repo = sut_variables["sut"], sut_variables["user_repo"]

    user_id = faker.random_number()

    with pytest.raises(NoResultFound):
        mocker.patch.context_manager(
            user_repo, "find", return_value=None, side_effect=NoResultFound()
        )
        result = sut.execute(user_id)

        assert user_repo.find_user_params["id"] == user_id

        assert result is None
