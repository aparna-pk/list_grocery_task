from typing import List, Optional
from pydantic import BaseModel


class GroceryList(BaseModel):
    date: Optional[str]
    list_name: str
    list_items: List[str]

