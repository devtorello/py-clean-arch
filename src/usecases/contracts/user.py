from abc import ABC, abstractclassmethod
from typing import Dict, List
from src.entities import User


class FetchUsers(ABC):
    """ Interface to Fetch Users Usecase """

    @abstractclassmethod
    def execute(cls) -> List[User]:
        """ Fetch Users Usecase """

        raise Exception("Method not Implemented: Fetch Users")


class FindUser(ABC):
    """ Interface to Find User Usecase """

    @abstractclassmethod
    def execute(cls, user_id: int) -> User:
        """ Find User Usecase """

        raise Exception("Method not Implemented: Find User")


class RegisterUser(ABC):
    """ Interface to Register User Usecase """

    @abstractclassmethod
    def execute(cls, username: str, password: str) -> Dict[bool, User]:
        """ Register User Usecase """

        raise Exception("Method not Implemented: Register User")


class RemoveUser(ABC):
    """ Interface to Remove User Usecase """

    @abstractclassmethod
    def execute(cls, user_id: int) -> bool:
        """ Remove User Usecase """

        raise Exception("Method not Implemented: Remove User")
