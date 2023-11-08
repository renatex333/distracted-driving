const FPS = 1;
const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d");

// Get access to the camera
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices
        .getUserMedia({ video: true })
        .then(function (stream) {
            video.srcObject = stream;
            video.play();
        });
}

// Function to send the image to the backend
function sendFrame() {
    context.drawImage(video, 0, 0, 640, 640);
    canvas.toBlob(function (blob) {
        const data = new FormData();
        data.append("frame", blob);

        fetch("/process", { method: "POST", body: data })
            .then((response) => response.json())
            .then((data) => {
                drawBox(data.box);
            });
    });
}

// Function to draw the box
function drawBox(box) {
    context.beginPath();
    context.rect(box.x, box.y, box.width, box.height);
    context.strokeStyle = "red";
    context.stroke();
}

// Send frames every second
setInterval(sendFrame, 1000 / FPS);
