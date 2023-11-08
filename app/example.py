import cv2 as cv
import numpy as np

from mtcnn.mtcnn import MTCNN
from flask import Flask, render_template
from flask_sock import Sock

detector = MTCNN()
app = Flask(__name__)
sock = Sock(app)


@app.route("/")
def index():
    return render_template('example.html')


# @sock.route('/socket')
# def echo(socket):
#     while True:
#         input_data = socket.receive()
#         input_array = np.frombuffer(input_data, np.uint8)
#         input_image = cv.imdecode(input_array, cv.IMREAD_COLOR)
#         output_image = process(input_image)
#         _, output_array = cv.imencode('.png', output_image)
#         output_data = output_array.tobytes()
#         socket.send(output_data)


# def process(input_image):
#     # output_image = cv.Canny(input_image, 100, 200)
#     output_image = input_image.copy()
#     for face in detector.detect_faces(input_image):
#        x, y, width, height = face['box']
#        cv.rectangle(output_image, (x, y), (x + width, y + height), (0, 255, 0), 2)
#     return output_image

def stringfy_data(data_array):
    s = ""
    for tuple in data_array:
        for el in tuple:
            s += str(el) + " "
        s += "/ "
    s += "&"
    return s

@sock.route('/socket')
def echo(socket):
    while True:
        input_data = socket.receive()
        input_array = np.frombuffer(input_data, np.uint8)
        input_image = cv.imdecode(input_array, cv.IMREAD_COLOR)
        faces = process(input_image)
        output_data = bytes(stringfy_data(faces), 'utf-8')
        socket.send(output_data)

def process(input_image):
    faces = []
    for face in detector.detect_faces(input_image):
        x, y, width, height = face['box']
        faces.append((x, y, width, height))
    return faces
