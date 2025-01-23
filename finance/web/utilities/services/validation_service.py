from pydantic import ValidationError
from finance.web.utilities.models.input_model import InputModel

def validate_field(value):
    try:
        if isinstance(value, str):
            # Intentar convertir a int si es posible
            if value.isdigit():
                InputModel(input_int=int(value))
            else:
                InputModel(input_str=value)
        elif isinstance(value, int):
            InputModel(input_int=value)
        else:
            raise ValueError('Unsupported type')
        return {"valid": True, "value": value}
    except ValidationError as e:
        return {"valid": False, "errors": e.errors()}
    except ValueError as e:
        return {"valid": False, "errors": [{"msg": str(e)}]}