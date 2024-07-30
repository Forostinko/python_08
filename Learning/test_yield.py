import pytest

@pytest.fixture
def example_fixture():
    print("\n--- Setup part of the fixture ---")
    yield
    print("\n--- Teardown part of the fixture ---")

@pytest.fixture
def sample_data():
    data = {"key": "value"}
    # передача данных в тестовую ф-ю
    yield data
    print("\n--- Teardown part of the fixture ---")

def test_example(example_fixture):
    assert 1 == 1

def test_sample_data(sample_data):
    assert sample_data["key"] == "value"