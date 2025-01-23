from pydantic import ValidationError
from finance.web.utilities.models.input_model import InputModel


def validate_field(value, field_type):
    try:
        if field_type == 'int':
            if isinstance(value, str) and value.isdigit():
                InputModel(input_int=int(value))
            elif isinstance(value, int):
                InputModel(input_int=value)
            else:
                raise ValueError('input_int must be a number')
        elif field_type == 'str':
            InputModel(input_str=value)
        else:
            raise ValueError('Unsupported field type')
        return {"valid": True, "value": value}
    except ValidationError as e:
        return {"valid": False, "errors": e.errors()}
    except ValueError as e:
        return {"valid": False, "errors": [{"msg": str(e)}]}
    

def validate_and_extract(args, param_name, default_value, field_type):
    input_value = args.get(param_name, default_value)
    validation_result = validate_field(input_value, field_type)
    if validation_result["valid"]:
        return validation_result["value"]
    else:
        raise ValueError(f"invalid input")