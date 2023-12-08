const FPS = 5;
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const alerts = document.getElementById('alerts');

const audioMapping = {
    'c1 - Texting': 'audio-intermitente',
    'c2 - Talking on the phone': 'audio-intermitente',
    'c3 - Operating the Radio': 'audio-unico',
    'c5 - Reaching Behind': 'audio-intermitente',
    'd0 - Eyes Closed': 'audio-muito-intenso',
    'd1 - Yawning': 'audio-descanso',
    'd2 - Nodding Off': 'audio-muito-intenso',
    // 'd3 - Eyes Open': 'audio-descanso', // Usado apenas para teste dos áudios
};

const blinkMapping = {
    'c4 - Drinking': 'blink',
    'd3 - Eyes Open': 'blink', // Usado apenas para teste de piscar
}

let isBlinking = false;

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
            .then((data) => {
                if (data.boxes) {
                    const distraction = Object.keys(data.boxes)[0];
                    let bestConfidence = 0;
                    let bestConfidenceCoords = [0, 0, 0, 0];
                    alerts.innerHTML = '';
                    Object.keys(data.boxes).forEach(function (key) {
                        let value = data.boxes[key];
                        if (value[0] > bestConfidence) {
                            bestConfidence = value[0];
                            bestConfidenceCoords = value[1];
                        }
                        let coords = value[1];
                        const newAlert = document.createElement("p");
                        newAlert.innerHTML = key + ": " + value[0] + "<br>" + "x: " + coords[0] + "<br>" + "y: " + coords[1] + "<br>" + "w: " + coords[2] + "<br>" + "h: " + coords[3] + "<br>";
                        alerts.appendChild(newAlert);
                    });

                    drawBox(bestConfidenceCoords);
                    playAlertSound(distraction);

                    if (distraction in blinkMapping) {
                        blinkScreen();
                    }
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

function playAlertSound(distraction) {
    const audioId = audioMapping[distraction];

    if (audioId) {
        document.getElementById(audioId).play();
    }
}

function pauseAllAudio() {
    const audioElements = document.querySelectorAll("audio");
    audioElements.forEach((audioElement) => {
        audioElement.pause();
        audioElement.currentTime = 0;
    })
}

function blinkScreen() {
    if (!isBlinking) {
        isBlinking = true;
        const originalBackgroundColor = document.body.style.backgroundColor;

        document.body.style.backgroundColor = 'white';

        setTimeout(() => {
            document.body.style.backgroundColor = originalBackgroundColor;
            isBlinking = false;
        }, 200);
    }
}

// Send frames every second
setInterval(sendFrame, 1000 / FPS);
