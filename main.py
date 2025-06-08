from video_processing.live_stream import start_live_stream
from face_recognition.recognize_faces import recognize_faces
from alert_system.email_alert import send_email_alert
from database.fetch_data import fetch_all_thieves

def main():
    print("Starting Smart Thief Alert System...")
    # Uncomment one of the following lines based on your requirement
    # start_live_stream()  # For live stream
    recognize_faces()  # For face recognition

    # Example of sending an alert
    thieves = fetch_all_thieves()
    if thieves:  # Assuming at least one thief exists
        send_email_alert('recipient@example.com', 'Thief Alert', 'A thief has been detected!')

if __name__ == "__main__":
    main()
