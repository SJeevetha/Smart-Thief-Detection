from pymongo import MongoClient

def connect_to_db():
    client = MongoClient('mongodb://localhost:27017/')  # Update with your MongoDB URI
    db = client['SmartThiefAlertSystem']
    return db

def close_connection(client):
    client.close()
