from collections import namedtuple
from src.repositories.config import DBConnectionHandler
from src.entities import User


class UserRepository:
    """ Class to manage User Repository """

    @classmethod
    def insert(cls, username: str, password: str) -> User:
        """Insert user into user entity/table.
        :param  - username: User's username
                - password: User's password
        :return - tuple with inserted user
        """

        InsertData = namedtuple("User", "id, username, password")

        with DBConnectionHandler() as db_connection:
            try:
                new_user = User(username=username, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return InsertData(
                    id=new_user.id,
                    username=new_user.username,
                    password=new_user.password,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
