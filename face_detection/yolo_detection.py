import cv2
import numpy as np

def detect_faces_yolo(image):
    net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')  # Update with YOLO config and weights
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    height, width, _ = image.shape
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    faces = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Confidence threshold
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                faces.append((center_x, center_y, w, h))

    return faces

if __name__ == "__main__":
    # Example of using YOLO detection
    image_path = 'path/to/image.jpg'
    image = cv2.imread(image_path)
    faces = detect_faces_yolo(image)
    print("Detected Faces with YOLO:", faces)
