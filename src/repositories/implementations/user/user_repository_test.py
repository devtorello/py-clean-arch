from faker import Faker
from src.repositories.config import DBConnectionHandler
from .user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()
db_conn_handler = DBConnectionHandler()


def test_insert_user():
    """ Should insert user into database """

    username = faker.name()
    password = faker.word()
    engine = db_conn_handler.get_engine()

    new_user = user_repository.insert(username=username, password=password)
    query_user = engine.execute(
        "SELECT * FROM user WHERE id='{}';".format(new_user.id)
    ).fetchone()

    engine.execute("DELETE FROM user WHERE id='{}';".format(new_user.id))

    assert new_user.id == query_user.id
    assert new_user.username == query_user.username
    assert new_user.password == query_user.password
