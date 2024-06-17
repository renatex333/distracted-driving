# Distracted Driving Detection Application

**Contributors:** Pedro Altobelli, Renato Laffranchi, Vinicius Morales

## Project Overview

This project aims to develop an innovative application designed to identify driver distractions and provide real-time alerts, thereby enhancing road safety and reducing the risk of accidents.

### Key Features

- **Closed Eyes Detection:** High-intensity alarm to alert the driver.
- **Head Dropping / Drowsiness Detection:** Low-intensity alarm to prevent microsleep.
- **Mobile Phone Use Detection:** Intermittent audio alerts for both handling and talking on the phone.
- **Reaching for Objects:** Progressive audio alerts to discourage reaching for items in the back seat.
- **Radio Adjustment:** Single audio alert to minimize distractions.
- **Yawning Detection:** Distinct audio alert with a suggestion to take a break.
- **Eating Detection:** Visual alert through screen flashing to remind the driver to stay focused.

### Final Deliverables

- A near real-time web application.
- A progressive alert system to handle various types of distractions.
- Mobile demonstration with server deployment.
- Comprehensive coverage of distraction types identified by YOLO.

## Environment Setup

To set up the development environment, create a virtual environment:

```sh
python3 -m venv env
```

Activate the virtual environment:

```sh
# Linux
source env/bin/activate
# Windows
env/Scripts/activate
```

## Installing Dependencies

Upgrade pip and install the required dependencies:

```sh
pip install --upgrade pip
pip install -r requirements.txt
```

If issues arise with `requirements.txt`, manually install dependencies:

```sh
pip install flask flask-sock opencv-python ultralytics
```

## Running the Flask Application

To start the Flask demo application, execute:

```sh
flask --app app/distracted-driving.py run
```

This project represents a cutting-edge solution in the field of driver safety, leveraging advanced detection algorithms to mitigate the risks associated with distracted driving. Our goal is to deliver a reliable, user-friendly application that can be seamlessly integrated into everyday use, contributing to safer roads and more attentive drivers.

## References

Sam Ansari. (2022). [How to Train YOLO Model to Detect Distracted Drivers](https://ansarisam.medium.com/how-to-train-yolo-v5-model-to-detect-distracted-drivers-ac62b2d44a27).

Yacine Rouizi. (2023). [Real-time Object Tracking with OpenCV and YOLOv8 in Python](https://thepythoncode.com/article/real-time-object-tracking-with-yolov8-opencv).

Ultralytics. (2023). [YoloV8 Docs](https://docs.ultralytics.com/).

Vercel. [Flask Hello World](https://vercel.com/templates/python/flask-hello-world).

Vercel. [Django Hello World](https://vercel.com/templates/python/django-hello-world).

Mozilla, MDN Web Docs. (2023). [Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API).

Ipylot project, Roboflow Universe. (2022). [Distracted Driving Dataset](https://universe.roboflow.com/ipylot-project/distracted-driving-v2wk5).
