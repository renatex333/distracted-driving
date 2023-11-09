from flask import Flask, request, jsonify, render_template
import numpy as np
import cv2
import torch
from src.utils.torch_utils import select_device
from src.utils.general import check_img_size, non_max_suppression, scale_boxes, Profile
from src.models.common import DetectMultiBackend
from src.utils.augmentations import letterbox

app = Flask(__name__)

# Initialize the model
model = None
names = None
weights = "app/src/weights/medium/best.onnx"
img_size = (640, 640)

def load_model(weights, imgsz=(640, 640), device="cpu"):
    """
    weights => model path
    imgsz => image size, default is 640x640
    device => device to run inference, default is cpu but you can use cuda device
    """
    global model
    global names

    # Load model
    device = select_device(device)
    model = DetectMultiBackend(weights, device=device)
    imgsz = check_img_size(imgsz)  # check image size

    # Run inference
    model.warmup(imgsz=(1, 3, *imgsz))  # warmup
    names = model.names

    print("Model loaded successfully")
    return 0

# Call the function to load the model when the server starts
with app.app_context():
    load_model(weights=weights, imgsz=img_size)

@app.route("/")
def index():
    return render_template('distracted-driving.html')

@app.route('/process', methods=['POST'])
def process_frame():
    dt = (Profile(), Profile(), Profile())
    file = request.files['frame'].read()
    nparr = np.fromstring(file, np.uint8)
    img0 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    im = letterbox(img0, img_size)[0]  # padded resize
    im = im.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
    im = np.ascontiguousarray(im)  # contiguous

    # Process the image and find the box coordinates
    with dt[0]:
        im = torch.from_numpy(im).to(model.device).float()
        im /= 255  # 0 - 255 to 0.0 - 1.0
        if len(im.shape) == 3:
            im = im[None]  # expand for batch dim

    # Inference
    with dt[1]:
        pred = model(im, augment=False, visualize=False)

    # NMS
    with dt[2]:
        pred = non_max_suppression(pred, max_det=1000)

    boxes = {}
    # Process predictions
    for i, det in enumerate(pred):  # per image
        if len(det):
            # Rescale boxes from img_size to im0 size
            det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], img0.shape).round()

            # Print results
            # for c in det[:, 5].unique():
            #     n = (det[:, 5] == c).sum()  # detections per class
            #     s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

            for *xyxy, conf, cls in reversed(det):
                c = int(cls)  # integer class
                confidence = float(conf)
                label = f'{names[c]} {confidence:.2f}'
                # s += f'{label}, '
                boxes[label] = (confidence, [float(p) for p in xyxy])
            return jsonify({'box':boxes})

    # Example box coordinates (replace with actual model prediction)
    nothing = {'x': 100, 'y': 100, 'width': 50, 'height': 50}

    return jsonify({'nothing': nothing})

if __name__ == '__main__':
    app.run(debug=True)
