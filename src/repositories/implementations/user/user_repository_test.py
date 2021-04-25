import pytest
from faker import Faker
from pytest_mock.plugin import MockerFixture
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
        "SELECT * FROM user WHERE id='{}';".format(new_user["id"])
    ).fetchone()

    engine.execute("DELETE FROM user WHERE id='{}';".format(new_user["id"]))

    assert new_user["id"] == query_user["id"]
    assert new_user["username"] == query_user["username"]


def test_insert_user_except(mocker: MockerFixture):
    """ Should raise exception if insert throws """

    engine = db_conn_handler.get_engine()
    stub = mocker.stub(name="db_conn_handler.session.rollback")

    with pytest.raises(Exception):
        user_repository.insert(username="any_username", password="any_pass")

        engine.execute("DELETE FROM user WHERE id='{}';".format(1))

        stub.assert_called()


def test_insert_user_finally(mocker: MockerFixture):
    """ Should call close when code reaches finally """

    engine = db_conn_handler.get_engine()
    stub = mocker.stub(name="db_conn_handler.session.close")

    with pytest.raises(Exception):
        user_repository.insert(username="any_username", password="any_pass")

        engine.execute("DELETE FROM user WHERE id='{}';".format(1))

        stub.assert_called()


def test_fetch_users():
    """ Should fetch users from database """

    username1 = faker.name()
    username2 = faker.name()
    password = faker.word()
    engine = db_conn_handler.get_engine()

    new_user1 = user_repository.insert(username=username1, password=password)
    new_user2 = user_repository.insert(username=username2, password=password)

    result = user_repository.fetch()

    engine.execute("DELETE FROM user WHERE id='{}';".format(new_user1["id"]))
    engine.execute("DELETE FROM user WHERE id='{}';".format(new_user2["id"]))

    assert new_user1["id"] == result[0]["id"]
    assert new_user2["id"] == result[1]["id"]


def test_fetch_users_empty():
    """ Should return an empty list if there is no users """

    result = user_repository.fetch()

    assert len(result) == 0
    assert result == []


def test_fetch_user_except(mocker: MockerFixture):
    """ Should raise exception if fetch throws """

    stub = mocker.stub(name="db_conn_handler.session.rollback")

    with pytest.raises(Exception):
        user_repository.fetch()

        stub.assert_called()


def test_fetch_user_finally(mocker: MockerFixture):
    """ Should raise finally when code reaches finally """

    stub = mocker.stub(name="db_conn_handler.session.close")

    with pytest.raises(Exception):
        user_repository.fetch()

        stub.assert_called()


def test_find_user():
    """ Should find a specific user in database """

    username1 = faker.name()
    username2 = faker.name()
    password = faker.word()
    engine = db_conn_handler.get_engine()

    new_user1 = user_repository.insert(username=username1, password=password)
    new_user2 = user_repository.insert(username=username2, password=password)

    result = user_repository.find(user_id=new_user2["id"])

    engine.execute("DELETE FROM user WHERE id='{}';".format(new_user1["id"]))
    engine.execute("DELETE FROM user WHERE id='{}';".format(new_user2["id"]))

    assert new_user2["id"] == result["id"]


def test_not_find_user():
    """ Should not find user if it didn't exist """

    result = user_repository.find(user_id="1")

    assert result is None


def test_find_user_except(mocker: MockerFixture):
    """ Should raise exception if find throws """

    stub = mocker.stub(name="db_conn_handler.session.rollback")

    with pytest.raises(Exception):
        user_repository.find(user_id="1")

        stub.assert_called()


def test_find_user_finally(mocker: MockerFixture):
    """ Should raise finally when code reaches finally """

    stub = mocker.stub(name="db_conn_handler.session.close")

    with pytest.raises(Exception):
        user_repository.fetch()

        stub.assert_called()


def test_remove_user_success():
    """ Should remove an user from user table """

    username = faker.name()
    password = faker.word()

    new_user = user_repository.insert(username=username, password=password)

    removed_user = user_repository.remove(user_id=new_user["id"])

    assert removed_user == 1
