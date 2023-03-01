from sqlalchemy import CHAR, Column, SmallInteger, String, Integer, Float

from database.db_connector import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    age = Column(SmallInteger)
    weight = Column(Float)
    height = Column(SmallInteger)
    gender = Column(CHAR)
    bmr = Column(SmallInteger)
    email = Column(String)

    def __init__(self, age, weight, height, gender):
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender

test_male = User(28, 100, 180, 'm')
test_female = User(28, 100, 180, 'f')