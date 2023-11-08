import cv2
import sys
import platform
from pathlib import Path
import torch
from utils.torch_utils import select_device
from utils.general import LOGGER, check_img_size, non_max_suppression, scale_boxes, Profile
from models.common import DetectMultiBackend
from utils.dataloaders import LoadStreams
from ultralytics.utils.plotting import Annotator, colors

def main(weights, imgsz=(640, 480), device="cpu") -> int:
    """
    weights => model path
    imgsz => image size, default is 640x640
    device => device to run inference, default is cpu but you can use cuda device
    """

    # Load model
    device = select_device(device)
    model = DetectMultiBackend(weights, device=device)
    stride, names, pt = model.stride, model.names, model.pt
    imgsz = check_img_size(imgsz, s=stride)  # check image size

    dataset = LoadStreams("0", img_size=imgsz, stride=stride, auto=pt, vid_stride=1)
    bs = len(dataset)  # batch_size

    # Run inference
    model.warmup(imgsz=(bs, 3, *imgsz))  # warmup
    seen, windows, dt = 0, [], (Profile(), Profile(), Profile())

    for path, im, im0s, vid_cap, s in dataset:
        boxes, s, has_detection = process(dt, model, path, im, im0s, names, seen, s, windows)
        print(boxes)
        # LOGGER.info(f"{s}{'' if has_detection else '(no detections), '}{dt[1].dt * 1E3:.1f}ms")

    return 0

def process(dt, model, path, im, im0s, names, seen, s, windows, show=False):
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
        seen += 1
        WIN, im0 = path[i], im0s[i].copy()
        # s += f"{i}: " + "%gx%g " % im.shape[2:]  # print string
        WIN = Path(WIN)  # to Path
        annotator = Annotator(im0, line_width=3, example=str(names)) if show else None
        if len(det):
            # Rescale boxes from img_size to im0 size
            det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()

            # Print results
            for c in det[:, 5].unique():
                n = (det[:, 5] == c).sum()  # detections per class
                s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

            for *xyxy, conf, cls in reversed(det):
                c = int(cls)  # integer class
                confidence = float(conf)
                label = f'{names[c]} {confidence:.2f}'
                s += f'{label}, '
                boxes[label] = (confidence, [float(p) for p in xyxy])
                # print(f"Box: {[float(p) for p in xyxy]}, Label: {label}")
                if show:
                    annotator.box_label(xyxy, label, color=colors(c, True))

        if show:
            # Stream results
            im0 = annotator.result()
            if platform.system() == 'Linux' and WIN not in windows:
                windows.append(WIN)
                cv2.namedWindow(str(WIN), cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)  # allow window resize (Linux)
                cv2.resizeWindow(str(WIN), im0.shape[1], im0.shape[0])
            cv2.imshow(str(WIN), im0)

        return boxes, s, len(det) > 0


if __name__ == '__main__':
    weights_path = "src/weights/medium/best.onnx"
    if "--weight" in sys.argv:
        index = sys.argv.index("--weight") + 1
        if index < len(sys.argv):
            weights_path = sys.argv[index]
    sys.exit(main(weights=weights_path))
