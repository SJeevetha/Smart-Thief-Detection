from pymongo import MongoClient

def create_collections():
    client = MongoClient('mongodb://localhost:27017/')  # Update with your MongoDB URI
    db = client['SmartThiefAlertSystem']

    # Create collections if they don't exist
    db.create_collection('thief_details')
    db.create_collection('thief_images')

    print("Collections created: thief_details, thief_images")

if __name__ == "__main__":
    create_collections()
