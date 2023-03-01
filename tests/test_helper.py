""" Module to test any helper methods [may be broken down further in time]
"""
from helper import mifflin_st_jeor
from models.user import User


def test_mifflin_st_jeor_male():
    """Test a male calculation
    """
    male = User(28, 100, 180, 'm')
    assert mifflin_st_jeor(male) == 1990
    
    """Test a female calculation with same values except gender
    """
def test_mifflin_st_jeor_female():
    female = User(28, 100, 180, 'f')
    assert mifflin_st_jeor(female) == 1824