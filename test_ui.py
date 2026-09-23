import pytest
from forpytest.OOP import Calc
from forpytest.OOP import User
def test_user_age():
    user1 = User('Bobby')
    user2 = User('Andy')
    assert user1.name == "Andy"
    assert user2.name == "Andy"

