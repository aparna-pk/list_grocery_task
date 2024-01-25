import math
from src.entity.grocery_list import GroceryList
from src.db import list_of_items
from typing import Optional


class GroceryListRepository:
    def add_items(self, items: GroceryList):
        if items.list_name == "" or len(items.list_items) == 0 or any(i == "" for i in items.list_items):
            return "field can't be empty"
        elif len(items.list_items) >= 15:
            return "limit of the list is 15 items"
        existing_list = list_of_items.find_one({"list_name": items.list_name, "date": items.date})
        if existing_list:
            return "List with the same name and date already exists"

        data_to_insert = {
            "date": items.date,
            "list_name": items.list_name,
            "list_items": items.list_items
        }
        list_of_items.insert_one(data_to_insert)
        return items

    def get_list_by_name(self, list_name: str, date: Optional[str] = None):
        result_cursor = list_of_items.find({"list_name": list_name})
        data_to_get = self.to_dict(result_cursor)
        if date is not None:
            for d in data_to_get:
                if d["date"] == date:
                    return d
            return {"message": "Date not found"}
        return data_to_get

    def data_by_page(self, page_no: int, page_size: int):
        #     Step 1: find the total number of data and total number of pages
        total_count = list_of_items.count_documents({})
        total_pages = math.ceil(total_count / page_size)
        #     Step 2: find the off set and query the data with limit
        offset = (page_no - 1) * page_size
        limit = page_size
        result = list_of_items.find({}).skip(offset).limit(limit)
        return {"total_count": total_count, "total_pages": total_pages, "data": self.to_dict(result)}

    def to_dict(self, result_cursor):
        data_to_get = [{"date": item['date'],
                        "list_name": item['list_name'],
                        "list_items": item['list_items']} for item
                       in result_cursor]
        # data_to_get = dict(**result_cursor.dict())
        return data_to_get










# @app.get('/get_list/{list_name}')
# def get_list_by_name(list_name: str):
#     result_cursor = list_of_items.find({"list_name": list_name})
#     data_to_get = to_dict(result_cursor)
#     return data_to_get


# @app.get('/pagination_list/{page_no}/{page_size}')
# def get_pagination(page_no: int, page_size: int):
#     params = Params(size=page_size, page=page_no)
#     return paginate(get_all(), params)


# @app.get('/pagination_list/{page_no}/{page_size}')
# def get_pagination(page_no: int, page_size: int):
#     total_items = len(all_data)
#     total_pages = (total_items // page_size + 1)
#     start_index = (page_no - 1) * page_size
#     end_index = page_no * page_size
#     page_data = all_data[start_index:end_index]
#     return {"Total items": total_items, "Total pages": total_pages, "Page data": page_data}
