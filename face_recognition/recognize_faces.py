from alert_system.email_alert import send_email_alert
import face_recognition
import cv2
from utils.config import IMAGE_PATH

def recognize_faces():
    # Load the known image (pic1) for comparison
    known_image = face_recognition.load_image_file(IMAGE_PATH)
    known_encoding = face_recognition.face_encodings(known_image)[0]

    # Capture a frame from the webcam
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()

    # Convert the frame to RGB (OpenCV uses BGR by default)
    rgb_frame = frame[:, :, ::-1]

    # Find all face locations and face encodings in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Compare the detected faces with the known image
    for face_encoding, face_location in zip(face_encodings, face_locations):
        match = face_recognition.compare_faces([known_encoding], face_encoding)

        if match[0]:
            # If a match is found, trigger an alert
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Send an email alert
            send_email_alert("Thief detected!")

    # Display the processed frame
    cv2.imshow('Video', frame)

    # Release the webcam and close windows
    video_capture.release()
    cv2.destroyAllWindows()

