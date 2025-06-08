import cv2

def detect_faces_haar(image):
    cascade_path = 'haarcascade_frontalface_default.xml'  # Path to the Haar Cascade file
    face_cascade = cv2.CascadeClassifier(cascade_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    return faces

if __name__ == "__main__":
    # Example of using the detection
    image_path = 'path/to/image.jpg'
    image = cv2.imread(image_path)
    faces = detect_faces_haar(image)
    print("Detected Faces:", faces)
