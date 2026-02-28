import pytest

@pytest.fixture()
def return_list():
    """Returns a list to be used in test_list"""
    return [1, 2, 3, "one", "two", "three"]

@pytest.fixture()
def return_tuple():
    return (1, 2, 3, "one", "two", "three")

@pytest.fixture(scope="module")
def return_dict():
    print("Starting fixture setup")
    yield {"California": "Sacramento", "Colorado": "Denver", "Florida": "Tallahassee"}
    print("\nStarting fixture teardown")


def test_list(return_list):
    my_list = return_list
    assert type(my_list) is list

def test_tuple(return_tuple):
    my_tuple = return_tuple
    assert type(my_tuple) is tuple

def test_dict(return_dict):
    my_dict = return_dict
    assert type(my_dict) is dict

def test_dict_access(return_dict):
    my_dict = return_dict
    assert my_dict["California"] == "Sacramento"