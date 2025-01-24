import pytest
from pydantic import ValidationError
from finance.web.utilities.models.input_model import InputModel  # Asegúrate de importar la clase desde el módulo correcto


@pytest.mark.parametrize("input_str, input_int, expected_valid", [
    ('validString', 100, True),  # Caso válido
    ('invalid@String', 100, False),  # input_str con caracteres especiales
    ('validString', '150', True),  # input_int como cadena válida
    ('validString', 'invalidInt', False),  # input_int como cadena no válida
    ('', 100, False),  # input_str vacío
    ('validString', 250, False),  # input_int fuera de rango
    (None, 100, False),  # input_str None no es válido
    ('validString', None, False),  # input_int None es válido
    ('validString', 0, False),  # input_int igual a 0
    ('validString', -10, False),  # input_int negativo
    ('validString', 199, True),  # input_int en el límite superior válido
    ('validString', 1, True),  # input_int en el límite inferior válido
])
def test_input_model(input_str, input_int, expected_valid):
    if expected_valid:
        model = InputModel(input_str=input_str, input_int=input_int)
        if input_str is not None:
            assert model.input_str == input_str.strip()
        if input_int is not None:
            assert model.input_int == int(input_int) if isinstance(input_int, str) else input_int
    else:
        with pytest.raises(ValidationError):
            InputModel(input_str=input_str, input_int=input_int)

@pytest.mark.parametrize("input_str, input_int, expected_exception", [
    ('validString', 'invalidInt', ValueError),  # input_int como cadena no válida
    ('invalid@String', 100, ValueError),  # input_str con caracteres especiales
    ('', 100, ValueError),  # input_str vacío
    ('validString', 250, ValueError),  # input_int fuera de rango
    (None, 100, ValidationError),  # input_str None no es válido
    ('validString', 0, ValueError),  # input_int igual a 0
    ('validString', -10, ValueError),  # input_int negativo
])
def test_input_model_exceptions(input_str, input_int, expected_exception):
    with pytest.raises(expected_exception):
        InputModel(input_str=input_str, input_int=input_int)

if __name__ == '__main__':
    pytest.main()