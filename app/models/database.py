from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db=client['addon-Grocery']
users=db['users']

def close_db_connection():
    client.close()