from typing import Optional
from src.di.repository import grocery_list_repository
from src.model.grocery_list_dto import GroceryListDTO
from fastapi import APIRouter

router = APIRouter()


class GroceryListController:

    @router.post('/add_list')
    def add_items(items: GroceryListDTO):
        return grocery_list_repository.add_items(items)

    @router.get('/list_by_name/{list_name}')
    def get_list_by_name(list_name: str, date: Optional[str] = None):
        return grocery_list_repository.get_list_by_name(list_name, date)

    @router.get('/data_by_page/{page_no}/{page_size}')
    def data_by_page(page_no: int, page_size: int):
        return grocery_list_repository.data_by_page(page_no, page_size)
