import cv2

def record_video():
    video_capture = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        out.write(frame)
        cv2.imshow('Recording Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    record_video()
