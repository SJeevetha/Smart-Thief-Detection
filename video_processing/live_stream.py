import cv2

def start_live_stream():
    video_capture = cv2.VideoCapture(0)  # Use 0 for the default camera

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        cv2.imshow('Live Stream', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_live_stream()
