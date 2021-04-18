from typing import Dict
from faker import Faker
from src.entities import User

faker = Faker()


def mock_user() -> User:
    """ Mocking User """

    return User(
        id=faker.random_number(digits=5), username=faker.name(), password=faker.name()
    )


class RegisterUserStub:
    """ Register User Stub """

    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.register_param = {}

    def execute(self, username: str, password: str) -> Dict[bool, User]:
        """ Registry user """

        self.register_param["username"] = username
        self.register_param["password"] = password

        response = None
        validate_entry = isinstance(username, str) and isinstance(password, str)

        if validate_entry:
            response = mock_user()

        return {"success": validate_entry, "data": response}
