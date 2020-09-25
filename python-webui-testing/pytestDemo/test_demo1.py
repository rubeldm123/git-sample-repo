import pytest

@pytest.fixture()
def setup():
    print("I will execute first")
    yield
    print("I will execute at the end")

def test_firstProgram(setup):
    print("I will execute for test ")