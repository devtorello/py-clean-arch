from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.repositories.config import DBConnectionHandler
from src.repositories.schemas import UserSchema
from src.usecases.contracts import UserRepositoryInterface
from src.entities import User


class UserRepository(UserRepositoryInterface):
    """ Class to manage User Repository """

    @classmethod
    def fetch(cls) -> List[User]:
        """Fetch all users from database.
        :return - return a list of users
        """

        with DBConnectionHandler() as db_connection:
            try:
                select = db_connection.get_select()
                statement = select(
                    UserSchema.id, UserSchema.username, UserSchema.password
                ).order_by(UserSchema.id)
                result = db_connection.session.execute(statement).all()

                return result
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def find(cls, user_id: int = None) -> User:
        """Find a specific user on database.
        :params - user_id: User's id
                - username: User's username
        :return - return a specific User
        """

        with DBConnectionHandler() as db_connection:
            try:
                select = db_connection.get_select()
                statement = select(
                    UserSchema.id, UserSchema.username, UserSchema.password
                ).filter_by(id=user_id)
                result = db_connection.session.execute(statement).one()

                return dict(
                    User(
                        id=result.id, username=result.username, password=result.password
                    )._asdict()
                )
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
                new_user = UserSchema(username=username, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return dict(
                    User(
                        id=new_user.id,
                        username=new_user.username,
                        password=new_user.password,
                    )._asdict()
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
