import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.dih9c.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print(db.list_collections_names)