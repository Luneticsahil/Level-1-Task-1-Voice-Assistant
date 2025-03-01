const startBtn = document.getElementById('start-btn');
const responseText = document.getElementById('response-text');

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'en-US';
recognition.interimResults = false;

startBtn.onclick = () => {
    recognition.start();
};

recognition.onresult = (event) => {
    const speechResult = event.results[0][0].transcript;
    responseText.textContent = `You said: "${speechResult}"`;
    sendVoiceCommand(speechResult);
};

function sendVoiceCommand(command) {
    fetch('/process_voice', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command })
    })
    .then(response => response.json())
    .then(data => {
        responseText.textContent = data.response;
    })
    .catch(error => console.error('Error:', error));
}
