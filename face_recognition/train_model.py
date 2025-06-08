import face_recognition
import os
import numpy as np
from database.fetch_data import fetch_all_thieves

def train_model():
    db_thieves = fetch_all_thieves()
    known_face_encodings = []
    known_face_names = []

    for thief in db_thieves:
        image_path = thief['image_path']
        thief_name = thief['name']
        
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        
        known_face_encodings.append(encoding)
        known_face_names.append(thief_name)

    return known_face_encodings, known_face_names

if __name__ == "__main__":
    encodings, names = train_model()
    print("Model trained with names:", names)
