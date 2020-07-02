from app.env import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
from flask_pymongo import pymongo

CONNECTION_STRING = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_HOST}.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.students_db
