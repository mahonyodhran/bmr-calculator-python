from sqlalchemy import CHAR, Column, SmallInteger, String, Integer

from database.db_connector import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    age = Column(SmallInteger)
    weight = Column(SmallInteger)
    height = Column(SmallInteger)
    gender = Column(CHAR)
    bmr = Column(SmallInteger)
    email = Column(String)

    def __init__(self, age, weight, height, gender):
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender