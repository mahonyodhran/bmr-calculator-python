""" Module to test any helper methods [may be broken down further in time]
"""
from helper import mifflin_st_jeor
from models.user import test_male, test_female


def test_mifflin_st_jeor_male():
    """Test a male calculation
    """
    assert mifflin_st_jeor(test_male) == 1990
    
    """Test a female calculation with same values except gender
    """
def test_mifflin_st_jeor_female():

    assert mifflin_st_jeor(test_female) == 1824