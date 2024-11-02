# 0x03. Unittests and Integration Tests

1. Mocking
-------------
Mocking is a technique that allows you to replace parts of your application with “mock” versions to isolate and control the behavior of dependencies.

```python
from unittest.mock import Mock

# Creating a mock object
mock_service = Mock()
mock_service.get_data.return_value = {'data': 'mocked'}

# Using the mock in the test
assert mock_service.get_data() == {'data': 'mocked'}

```
2. Parametrization

Parametrization allows you to run the same test logic with multiple sets of input data, which helps increase test coverage without duplicating code.
```python
import pytest

@pytest.mark.parametrize("input_value, expected_output",[(5, 25),(-3, 9),(0, 0)])

def test_square(input_value, expected_output):
    assert square(input_value) == expected_output
def square(x):
    return x * x
```
3. Fixtures
Fixtures are reusable components that help set up the preconditions needed for tests. They can include preparing data.
```python
import pytest

@pytest.fixture
def sample_data():
    # setup code
    data = {"name": "Test", "age": 30}
    return data
def test_usernames(sample_data):
    assert sample_data["name"] == "Test"
def test_user_age(sample_data):
    assert sample_data["age"] == 30

```
## utils.access_nested_map explain

```python
# nasted map 
dict_ = {
    "a": {"b": {1:2}}
}
# if we want to access the the 2 =>a, b, 1
# it should look like this to access
res = access_nested_map(dict_, ["a", "b", 1])
```
- now create the function
```python

def access_nested_map(map,path):
    level = map
    for key in path:
        if key in level:
            level = level[key]
        else:
            raise keyError(f"key {key} not found in the map")
    return level
```
