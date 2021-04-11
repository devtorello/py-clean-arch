from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.repositories.config import DBConnectionHandler
from src.entities import User


class UserRepository:
    """ Class to manage User Repository """

    @classmethod
    def fetch(cls) -> List[User]:
        """Fetch all users from database.
        :return - return a list of users
        """

        with DBConnectionHandler() as db_connection:
            try:
                select = db_connection.get_select()
                statement = select(User.id, User.username).order_by(User.id)
                result = db_connection.session.execute(statement).all()

                return result
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def find(cls, user_id: int = None):
        """Find a specific user on database.
        :params - user_id: User's id
                - username: User's username
        :return - return a specific User
        """

        with DBConnectionHandler() as db_connection:
            try:
                select = db_connection.get_select()
                statement = select(User.id, User.username).filter_by(id=user_id)
                result = db_connection.session.execute(statement).one()

                return User(id=result.id, username=result.username)
            except NoResultFound:
                return None
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def insert(cls, username: str, password: str) -> User:
        """Insert user into user entity/table.
        :param  - username: User's username
                - password: User's password
        :return - tuple with inserted user
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = User(username=username, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return User(id=new_user.id, username=new_user.username)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
