from handler import validate_input


def test_validate_input():
    input = '+1 sausage'
    assert validate_input(input)