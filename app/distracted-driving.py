from flask import Flask, request, jsonify, render_template
from ultralytics import YOLO
import cv2
import numpy as np

app = Flask(__name__)

CONFIDENCE_THRESHOLD = 0.7

# Call the function to load the model when the server starts
with app.app_context():
    model = YOLO("app/models/distracted-driving.onnx")

# Set up the main route
@app.route("/")
def index():
    return render_template('distracted-driving.html')

# Set up the process route, which will receive requests containing an image
@app.route('/process', methods=['POST'])
def process_frame():
    file = request.files['frame'].read()
    nparr = np.fromstring(file, np.uint8)
    im = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    detections = model(im)[0]
    """
    Attributes of "detections" (ultralytics.engine.results.Results):
        boxes (Boxes, optional): A Boxes object containing the detection bounding boxes.
        names (dict): A dictionary of class names.

    Attributes of "boxes" (ultralytics.utils.results.Boxes):
        data (torch.Tensor): The raw bboxes tensor (alias for `boxes`).
    """
    boxes_data = detections.boxes.data.tolist()
    classes_names = detections.names
    boxes = {}
    for data in boxes_data:
        confidence = data[4]
        if float(confidence) < CONFIDENCE_THRESHOLD:
            continue
        class_id = int(data[5])
        class_name = classes_names[class_id]
        xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
        boxes[class_name] = (confidence, [xmin, ymin, xmax, ymax])

    if len(boxes) == 0:
        return jsonify({'boxes': "None"})
    return jsonify({'boxes': boxes})

if __name__ == '__main__':
    app.run(debug=True)
