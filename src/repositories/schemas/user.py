from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.repositories.config import Base


class UserSchema(Base):
    """ User Entity """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id_pet = relationship("PetSchema")

    def __rep__(self):
        return f"Usr: [name={self.name}]"
