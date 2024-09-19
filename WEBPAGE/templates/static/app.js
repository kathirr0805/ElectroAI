// Speech recognition
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'en-US';
recognition.interimResults = false;
recognition.maxAlternatives = 1;

document.getElementById('start-btn').addEventListener('click', () => {
    recognition.start();
    document.getElementById('response').textContent = "Listening...";
});

recognition.onresult = function (event) {
    const userSpeech = event.results[0][0].transcript;
    document.getElementById('response').textContent = `You said: ${userSpeech}`;

    // Send the speech text to the server
    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userSpeech }),
    })
        .then(response => response.json())
        .then(data => {
            const botResponse = data.response;
            document.getElementById('response').textContent = `Bot says: ${botResponse}`;

            // Convert response text to speech
            const utterance = new SpeechSynthesisUtterance(botResponse);
            window.speechSynthesis.speak(utterance);
        });
};

recognition.onerror = function (event) {
    document.getElementById('response').textContent = 'Error occurred in recognition: ' + event.error;
};
