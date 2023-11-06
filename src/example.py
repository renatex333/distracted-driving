import cv2 as cv
import numpy as np
import sys
import torch
import torchvision.transforms as transforms

CAM = 2
FPS = 30
WIN = 'Rave Maluca'

def main() -> int:

    ### EXEMPLO DE USO DE PYTORCH ###
    # Model
    model = torch.jit.load("src/best.torchscript", map_location="cpu")
    im = torch.empty((1, 3, 640, 640), device="cpu")

    # Images
    # im = 'src/teste1.jpg'  # or file, Path, PIL, OpenCV, numpy, list

    # image = cv.imread(im)

    # Convert BGR image to RGB image 
    # image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    # print(image.shape)
    
    # # Define a transform to convert 
    # # the image to torch tensor 
    # transform = transforms.Compose([ 
    #     transforms.ToTensor() 
    # ]) 
    
    # # Convert the image to Torch tensor 
    # tensor = transform(image)
    # print(tensor.shape)
    # Inference
    results = model(im)

    # Results
    results.print()  # .print(), .show(), .save(), .crop(), .pandas(), etc.

    ### EXEMPLO DADO EM AULA ###
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
