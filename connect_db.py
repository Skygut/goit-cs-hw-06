from pymongo import MongoClient
from datetime import datetime

# Підключення до MongoDB
client = MongoClient("localhost", 27017)
db = client["messages_db"]
collection = db["messages"]

# Вставка документа
post = {"date": datetime.now(), "username": "user", "message": "Hello"}
collection.insert_one(post)
