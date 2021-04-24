from typing import List
from src.entities.user import User
from .mock_user import mock_user


class UserRepositoryStub:
    """ Stub to User Repository Methods """

    def __init__(self):
        self.insert_user_params = {}
        self.find_user_params = {}

    def insert(self, username: str, password: str) -> User:
        """ Spy to all the attributes """

        self.insert_user_params["username"] = username
        self.insert_user_params["password"] = password

        return mock_user()

    def fetch(self) -> List[User]:
        """ Spy to all the attributes """

        return [mock_user()]

    def find(self, user_id: int = None) -> User:
        """ Spy to all the attributes """

        self.find_user_params["id"] = user_id

        return mock_user()
