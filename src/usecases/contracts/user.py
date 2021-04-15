from abc import ABC, abstractclassmethod
from typing import Dict
from src.entities import User


class RegisterUser(ABC):
    """ Interface to Register User Usecase """

    @abstractclassmethod
    def execute(cls, username: str, password: str) -> Dict[bool, User]:
        """ Register User Usecase """

        raise Exception("Method not Implemented: Register User")
