from datetime import datetime
from pydantic import BaseModel, field_validator
from typing import List, Optional


class GroceryListDTO(BaseModel):
    date: Optional[str]
    list_name: str
    list_items: List[str]

    @field_validator('date')
    def validate_date_format(cls, value):
        date_format = '%d-%m-%Y'
        try:
            datetime.strptime(value, date_format)
        except ValueError:
            raise ValueError("Incorrect data format, should be DD-MM-YYYY")
        return value
