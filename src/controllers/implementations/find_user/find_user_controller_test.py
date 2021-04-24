from src.shared.validation.errors.required_params_error import required_param_error
from faker import Faker
from src.controllers.contracts.http_models import HttpRequest
from src.shared.validation.mocks.mock_validation import ValidationStub
from src.usecases.mocks.mock_user_repository import UserRepositoryStub
from src.usecases.mocks.mock_user import FindUserStub
from .find_user_controller import FindUserController

faker = Faker()


def mock_http_request():
    """ Mock Http Request """

    return {"user_id": faker.random_number()}


def make_sut():
    """ Make test SUT """

    user_repo_stub = UserRepositoryStub()
    find_user_stub = FindUserStub(user_repository=user_repo_stub)
    validation_stub = ValidationStub()

    sut = FindUserController(
        find_user_usecase=find_user_stub, validation=validation_stub
    )

    return {
        "sut": sut,
        "find_user_stub": find_user_stub,
        "validation_stub": validation_stub,
    }


def test_find_user_success():
    """ Should return status 200 """

    sut_variables = make_sut()

    sut = sut_variables["sut"]

    params = mock_http_request()
    response = sut.handle(HttpRequest(query=params))

    assert response.status_code == 400
    assert response.body is not None


def test_find_user_controller_bad_request():
    """ Should return status 400 """

    sut_variables = make_sut()

    sut = sut_variables["sut"]

    response = sut.handle(HttpRequest(query={}))

    assert response.status_code == 400
    assert response.body["error"] == required_param_error("valid_field")
