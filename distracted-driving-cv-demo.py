# from flask import Flask, request, jsonify, render_template
from ultralytics import YOLO
import cv2
import sys
import numpy as np

# app = Flask(__name__)

CONFIDENCE_THRESHOLD = 0.7
GREEN = (0, 255, 0)
CAM = 0
FPS = 60
WIN = 'Distracted Driving'
# Load the pre-trained YOLOv8n model
model = YOLO("app/models/distracted-driving.onnx")

def main() -> int:
    capture = cv2.VideoCapture(CAM)
    delay = round(1000 / FPS)
    cv2.namedWindow(WIN)
    while cv2.getWindowProperty(WIN, cv2.WND_PROP_VISIBLE):
        success, frame = capture.read()

        if success:
            output = frame.copy()
            boxes = process(frame)
            for box in boxes:
                cv2.rectangle(output, (box['x_min'], box['y_min']), (box['x_max'], box['y_max']), GREEN, 2)
            cv2.imshow(WIN, output)

        if cv2.waitKey(delay) == ord('q'):
            break

    capture.release()
    cv2.destroyWindow(WIN)
    return 0

def process(frame):

    detections = model(frame)[0]
    boxes = []
    for data in detections.boxes.data.tolist():
        confidence = data[4]
        if float(confidence) < CONFIDENCE_THRESHOLD:
            continue

        xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
        # class_id = int(data[5])
        # cv2.rectangle(output, (xmin, ymin) , (xmax, ymax), GREEN, 2)
        # cv2.putText(output, str(class_id), (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, GREEN, 2)
        boxes.append({'x_min': xmin, 'y_min': ymin, 'x_max': xmax, 'y_max': ymax})

    return boxes

# # Call the function to load the model when the server starts
# with app.app_context():
#     model = YOLO("models/distracted-driving.onnx")

# @app.route("/")
# def index():
#     return render_template('distracted-driving.html')

# @app.route('/process', methods=['POST'])
# def process_frame():


#     boxes = {}

#     # Example box coordinates (replace with actual model prediction)
#     nothing = {'x': 100, 'y': 100, 'width': 50, 'height': 50}

#     return jsonify({'nothing': nothing})

if __name__ == '__main__':
    # app.run(debug=True)
    sys.exit(main())
