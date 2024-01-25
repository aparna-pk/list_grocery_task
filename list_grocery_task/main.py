from fastapi import FastAPI
from src.controllers.grocery_list_controller import router

app = FastAPI()
app.include_router(router)
