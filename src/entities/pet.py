import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from src.repositories.config import Base


class AnimalTypes(enum.Enum):
    """ Defining animal types """

    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"
    FISH = "fish"
    TURTLE = "turtle"


class Pet(Base):
    """ Pet Entity """

    __tablename__ = "pet"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    species = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    def __rep__(self):
        return (
            f"Pet: [name={self.name}, species={self.species}, user_id={self.user_id}]"
        )
