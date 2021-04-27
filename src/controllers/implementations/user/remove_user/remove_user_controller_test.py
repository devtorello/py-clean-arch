from faker import Faker
from src.controllers.contracts.http_models import HttpRequest
from src.shared.validation.mocks.mock_validation import ValidationStub
from src.usecases.mocks.mock_user_repository import UserRepositoryStub
from src.usecases.mocks.mock_user import RemoveUserStub
from .remove_user_controller import RemoveUserController

faker = Faker()


def mock_http_request():
    """ Mock Http Request """

    return {"user_id": "1", "valid_field": 1}


def make_sut():
    """ Make test SUT """

    user_repo_stub = UserRepositoryStub()
    remove_user_stub = RemoveUserStub(user_repository=user_repo_stub)
    validation_stub = ValidationStub()

    sut = RemoveUserController(
        remove_user_uc=remove_user_stub, validation=validation_stub
    )

    return {
        "sut": sut,
        "remove_user_stub": remove_user_stub,
        "validation_stub": validation_stub,
    }


def test_remove_user_success():
    """ Should return status 200 """

    sut_variables = make_sut()

    sut = sut_variables["sut"]

    params = mock_http_request()
    response = sut.handle(HttpRequest(query=params))

    assert response.status_code == 200
    assert response.body is not None
