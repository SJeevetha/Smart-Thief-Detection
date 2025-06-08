from database.db_connection import connect_to_db

def fetch_all_thieves():
    db = connect_to_db()
    collection = db['thief_details']
    thieves = collection.find()
    return list(thieves)

if __name__ == "__main__":
    all_thieves = fetch_all_thieves()
    print("Thief Details:", all_thieves)
