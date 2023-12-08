const FPS = 5;
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const alerts = document.getElementById('alerts');

// Get access to the camera and play the video
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            video.srcObject = stream;
            video.onloadedmetadata = () => {
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
            };
            video.play();
        })
        .catch(err => console.error("Error accessing camera: ", err));
}

// Function to send the image to the backend
function sendFrame() {
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob(function (blob) {
        const data = new FormData();
        data.append("frame", blob);

        fetch("/process", { method: "POST", body: data })
            .then((response) => response.json())
            // Contents of response data: boxes[class_name] = (confidence, [x, y, w, h])
            .then((data) => {
                if(data.boxes){
                    var bestConfidence = 0;
                    var bestConfidenceCoords = [0, 0, 0, 0];
                    alerts.innerHTML = '';
                    Object.keys(data.boxes).forEach(function(key) {
                        var value = data.boxes[key];
                        if(value[0] > bestConfidence){
                            bestConfidence = value[0];
                            bestConfidenceCoords = value[1];
                        }
                        var coords = value[1];
                        const newAlert = document.createElement("p");
                        newAlert.innerHTML = key + ": " + value[0] + "<br>" + "x: " + coords[0] + "<br>" + "y: " + coords[1] + "<br>" + "w: " + coords[2] + "<br>" + "h: " + coords[3] + "<br>";
                        alerts.appendChild(newAlert);
                    });
                    
                    drawBox(bestConfidenceCoords);
                }
            })
            .catch(err => console.error("Error fetching data: ", err));
    });
}

// Function to draw a box around the detected distraction
function drawBox(coords) {
    context.lineWidth = "2";
    context.strokeStyle = "#af472a";
    context.strokeRect(coords[0] * canvas.width, coords[1] * canvas.height, coords[2] * canvas.width, coords[3] * canvas.height);
}


// Send frames every second
setInterval(sendFrame, 1000 / FPS);
