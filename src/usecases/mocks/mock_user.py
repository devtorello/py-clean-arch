from faker import Faker
from src.entities import User

faker = Faker()


def mock_user() -> User:
    """ Mocking User """

    return User(
        id=faker.random_number(digits=5), username=faker.name(), password=faker.name()
    )
