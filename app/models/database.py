from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db=client['addon-Grocery']

#collections
users=db['users']
items=db['items']


def close_db_connection():
    client.close()

