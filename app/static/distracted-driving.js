const FPS = 30;
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
                if(data.box){
                    drawBox(data.box);
                }
            });
    });
}

// {
//     "d3 - Eyes Open 0.37": [
//         0.3675169348716736,
//         [
//             304,
//             191,
//             510,
//             471
//         ]
//     ]
// }

// Function to draw the box
function drawBox(box) {
    const firstKey = Object.keys(box)[0];
    const cord = box[firstKey][1];
    const [x1, y1, x2, y2] = cord;
    context.beginPath();
    context.rect(x1, y1, x2 - x1, y2 - y1);
    context.strokeStyle = "red";
    context.stroke();
    console.log(box);
}

// Send frames every second
setInterval(sendFrame, 1000 / FPS);
