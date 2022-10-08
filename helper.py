"""Module for any helper methods
"""

def mifflin_st_jeor(age, weight, height, gender):
    """calculate the bmr using mifflin equation [standard for now]"""
    if gender == "m":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    return int(bmr)