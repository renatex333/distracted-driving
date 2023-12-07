const FPS = 10;
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const dataDiv = document.getElementById('data');
const context = canvas.getContext('2d');

// Get access to the camera
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            video.srcObject = stream;
            video.play();
            // video.onloadedmetadata = () => {
            //     canvas.width = video.videoWidth;
            //     canvas.height = video.videoHeight;
            //     draw();
            // };
        })
        .catch(err => console.error("Error accessing camera: ", err));
}

// Function to send the image to the backend
function sendFrame() {
    context.drawImage(video, 0, 0, 640, 480);
    canvas.toBlob(function (blob) {
        const data = new FormData();
        data.append("frame", blob);

        fetch("/process", { method: "POST", body: data })
            .then((response) => response.json())
            .then((data) => {
                if(data.boxes){
                    console.log(data.boxes);
                    // drawBox(data.boxes);
                    // dataDiv.innerHTML = printBox(data.boxes);
                    dataDiv.innerHTML = JSON.stringify(data.boxes);
                    // boxes[class_name] = (confidence, [xmin, ymin, xmax, ymax])
                }
            })
            .catch(err => console.error("Error fetching data: ", err));
    });
}

// Function to draw the box
function drawBox(box) {
    console.log(box);
    const firstKey = Object.keys(box)[0];
    const cord = box[firstKey][1];
    const [x1, y1, x2, y2] = cord;
    context.beginPath();
    context.rect(x1, y1, x2 - x1, y2 - y1);
    context.strokeStyle = "red";
    context.lineWidth = 5;
    context.stroke();
    console.log(box);
}

// Send frames every second
setInterval(sendFrame, 1000 / FPS);
