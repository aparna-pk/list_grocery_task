from pymongo import MongoClient
from pymongo.server_api import ServerApi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url = "mongodb+srv://python:apa123@atlascluster.d7perzq.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(url, server_api=ServerApi('1'))

db = client.test
list_of_items = db.GroceryListDTO




