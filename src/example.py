import cv2 as cv
import numpy as np
import sys
import torch
import torchvision.transforms as transforms

CAM = 2
FPS = 30
WIN = 'Rave Maluca'

def main() -> int:

    device = torch.device("cpu")
    # Model
    model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5/runs/train/exp/weights/best.onnx', trust_repo=True)
    # model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5/runs/train/exp/weights/best.torchscript', autoshape=False) 

    # Images
    img_path = './teste1.jpg'  # or file, Path, PIL, OpenCV, numpy, list

    # _image = cv.imread(img_path)
    # _image = np.array(_image).astype(np.float32) 
    # image = torch.from_numpy(_image)
    # image = image[np.newaxis, :]
    # image = image.permute(0, 3, 1, 2) 
    # Inference
    results = model(img_path)

    # Results
    results.print()  # or .show(), .save(), .crop(), .pandas(), etc.

    # capture = cv.VideoCapture(CAM)
    # delay = round(1000 / FPS)
    # cv.namedWindow(WIN)

    # while cv.getWindowProperty(WIN, cv.WND_PROP_VISIBLE):
    #     success, frame = capture.read()

    #     if success:
    #         height, width, num_channels = frame.shape
    #         image = np.empty((height, 2 * width, num_channels), frame.dtype)
    #         image[:, :width] = frame
    #         image[:, width:] = process(frame)
    #         cv.imshow(WIN, image)

    #     if cv.waitKey(delay) == ord('q'):
    #         break

    # cv.destroyWindow(WIN)
    return 0

# def process(frame):
#     # output = frame.copy()

#     # Inference
#     results = model(frame)

#     # Results
#     results.print()  # or .show(), .save(), .crop(), .pandas(), etc.

#     return 0

if __name__ == '__main__':
    # sys.exit(main())
    main()
