from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

db_uri=os.getenv('DB_URI')
db_name=os.getenv('DB_NAME')

client = MongoClient(db_uri)
db=client[db_name]

#collections
users=db['users']
items=db['items']


def close_db_connection():
    client.close()

