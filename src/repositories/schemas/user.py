from sqlalchemy import Column, String, Integer
from src.repositories.config import Base


class UserSchema(Base):
    """ User Entity """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def __rep__(self):
        return f"Usr: [name={self.name}]"
