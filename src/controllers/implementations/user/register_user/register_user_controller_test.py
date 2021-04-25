from faker import Faker
from src.controllers.contracts.http_models import HttpRequest
from src.shared.validation.errors.required_params_error import required_param_error
from src.shared.validation.mocks.mock_validation import ValidationStub
from src.usecases.mocks.mock_user_repository import UserRepositoryStub
from src.usecases.mocks.mock_user import RegisterUserStub
from .register_user_controller import RegisterUserController

faker = Faker()


def mock_http_request(pass_validation: bool = True, pass_unp_entity: bool = True):
    """ Mock Http Request """

    if pass_validation and pass_unp_entity:
        return {
            "username": faker.word(),
            "password": faker.word(),
            "valid_field": faker.word(),
        }

    if pass_unp_entity is False:
        return {
            "username": faker.random_number(),
            "password": faker.word(),
            "valid_field": faker.word(),
        }

    return {"username": faker.word(), "password": faker.word()}


def make_sut():
    """ Make test SUT """

    user_repo_stub = UserRepositoryStub()
    register_stub = RegisterUserStub(user_repository=user_repo_stub)
    validation_stub = ValidationStub()

    sut = RegisterUserController(
        register_user_usecase=register_stub, validation=validation_stub
    )

    return {
        "sut": sut,
        "register_stub": register_stub,
        "validation_stub": validation_stub,
    }


def test_register_user_controller_success():
    """ Should return status 200 """

    sut_variables = make_sut()

    sut, register_stub = sut_variables["sut"], sut_variables["register_stub"]

    attributes = mock_http_request()
    response = sut.handle(HttpRequest(body=attributes))

    assert register_stub.register_param["username"] == attributes["username"]
    assert register_stub.register_param["password"] == attributes["password"]

    assert response.status_code == 200
    assert response.body is not None


def test_register_user_controller_bad_request():
    """ Should return status 400 """

    sut_variables = make_sut()

    sut = sut_variables["sut"]

    attributes = mock_http_request(pass_validation=False)
    response = sut.handle(HttpRequest(body=attributes))

    assert response.status_code == 400
    assert response.body["error"] == required_param_error("valid_field")


def test_register_user_controller_unprocessable_entity():
    """ Should return 422 """

    sut_variables = make_sut()

    sut = sut_variables["sut"]

    attributes = mock_http_request(pass_unp_entity=False)
    response = sut.handle(HttpRequest(body=attributes))

    assert response.status_code == 422
    assert response.body["error"] == "Unprocessable Entity"


def test_register_user_controller_server_error():
    """ Should return 500 """

    sut_variables = make_sut()

    sut = sut_variables["sut"]

    response = sut.handle(HttpRequest(body=None))

    assert response.status_code == 500
    assert response.body["error"] is not None
