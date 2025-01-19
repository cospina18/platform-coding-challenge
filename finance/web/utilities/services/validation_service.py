from pydantic import ValidationError
from finance.web.utilities.models.input_model import InputModel

def validate_inputs(input1, input2):
    try:
        data = InputModel(input_str=input1, input_int=input2)
        return data
    except ValidationError as e:
        return e.errors()