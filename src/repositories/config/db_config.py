from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


class DBConnectionHandler:
    """ SQLAlchemy database connection """

    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.session = None
        self.select = None

    def get_select(self):
        """Get select instance
        :return - select instance of sqlalchemy
        """

        return select

    def get_engine(self):
        """Return connection engine
        :param - None
        :return - engine connection to Database
        """

        engine = create_engine(self.__connection_string)

        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        self.session = Session(engine, future=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
