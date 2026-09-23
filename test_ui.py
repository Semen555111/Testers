import pytest
@pytest.fixture()
def bef_aft():
    print("before")
    yield
    print("\n after")
def test_dem2():
    assert 1 == 1
def test_dem1(bef_aft):
    assert 1 == 2

