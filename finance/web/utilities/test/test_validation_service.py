import pytest
from pydantic import ValidationError
from finance.web.utilities.services.validation_service import validate_field, validate_and_extract

@pytest.mark.parametrize("value, field_type, expected_valid, expected_value", [
    (123, 'int', True, 123),
    ('abc', 'int', False, None),
    ('test', 'str', True, 'test'),
    ('test', 'float', False, None)
])
def test_validate_field(value, field_type, expected_valid, expected_value):
    result = validate_field(value, field_type)
    assert result['valid'] == expected_valid
    if expected_valid:
        assert result['value'] == expected_value
    else:
        assert 'errors' in result

@pytest.mark.parametrize("args, param_name, default_value, field_type, expected_value", [
    ({'param': 123}, 'param', '0', 'int', 123),
    ({'param': 'abc'}, 'param', '0', 'int', pytest.raises(ValueError, match='invalid input')),
    ({}, 'param', 'default', 'str', 'default')
])
def test_validate_and_extract(args, param_name, default_value, field_type, expected_value):
    if isinstance(expected_value, type(pytest.raises(ValueError))):
        with expected_value:
            validate_and_extract(args, param_name, default_value, field_type)
    else:
        result = validate_and_extract(args, param_name, default_value, field_type)
        assert result == expected_value

if __name__ == '__main__':
    pytest.main()