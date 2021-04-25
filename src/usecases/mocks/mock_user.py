from typing import Dict, List
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

        if not isinstance(username, str) or not isinstance(password, str):
            return {"success": False, "data": None}

        response = mock_user()

        return {"success": True, "data": response}


class FindUserStub:
    """ Find User Stub """

    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.find_user_param = {}

    def execute(self, user_id: str) -> User:
        """ Find user """

        self.find_user_param["user_id"] = user_id

        return mock_user()


class FetchUsersStub:
    """ Fetch Users Stub """

    def __init__(self, user_repository: any):
        self.user_repository = user_repository

    def execute(self) -> List[User]:
        """ Fetch Users """

        return [mock_user()]
