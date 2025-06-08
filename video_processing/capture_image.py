import cv2

def capture_image():
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    if ret:
        cv2.imwrite('captured_image.jpg', frame)
        print("Image captured and saved as captured_image.jpg")
    video_capture.release()

if __name__ == "__main__":
    capture_image()
