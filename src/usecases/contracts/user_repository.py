from abc import ABC, abstractmethod
from typing import List
from src.entities import User


class UserRepositoryInterface(ABC):
    """ Interface to User Repository Class """

    @abstractmethod
    def fetch(self) -> List[User]:
        """ abstractmethod """

        raise Exception("Method not Implemented: Fetch Users")

    @abstractmethod
    def find(self, user_id: int) -> User:
        """ abstractmethod """

        raise Exception("Method not Implemented: Find User")

    @abstractmethod
    def insert(self, username: str, password: str) -> User:
        """ abstractmethod """

        raise Exception("Method not Implemented: Insert User")
