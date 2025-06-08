from database.db_connection import connect_to_db

def insert_thief_data(thief_info):
    db = connect_to_db()
    collection = db['thief_details']
    collection.insert_one(thief_info)
    print("Thief data inserted:", thief_info)

if __name__ == "__main__":
    # Example thief info
    thief_info = {
        'name': 'John Doe',
        'image_path': 'path/to/image.jpg',  # Provide the correct path
        'area': 'Downtown'
    }
    insert_thief_data(thief_info)
