from pydantic import BaseModel, Field, ValidationError, field_validator
import re

class InputModel(BaseModel):
    input_str: str = Field(None, min_length=1, max_length=50)
    input_int: int = Field(None, gt=0, lt=200)
    
    @field_validator('input_str')
    def no_special_characters(cls, value):
        if value and not re.match("^[a-zA-Z]*$", value):
            raise ValueError('input_str must not contain special characters')
        return value

    @field_validator('input_int', mode='before')
    def validate_and_convert_int(cls, value):
        if isinstance(value, str):
            if value.isdigit():
                value = int(value)
            else:
                raise ValueError('input_int must be a number')
        elif not isinstance(value, int):
            raise ValueError('input_int must be a number')
        return value

    class Config:
        anystr_strip_whitespace = True