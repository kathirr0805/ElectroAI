$(document).ready(function() {
    // Handle form submission for typing input
    $('#user-input-form').submit(function(event) {
        event.preventDefault();
        var user_input = $('#user_input').val();

        // Display what the user said
        $('#user-message').html('You said: ' + user_input);

        // Send the user input to the server
        $.ajax({
            url: '/get_response',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ query: user_input }),
            success: function(response) {
                $('#response').html('Assistant: ' + response.response);
            },
            error: function() {
                $('#response').html('Sorry, something went wrong.');
            }
        });

        // Clear the input field after submission
        $('#user_input').val('');
    });

    // Speech Recognition
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    // Start speech recognition when the button is clicked
    document.getElementById('start-btn').addEventListener('click', () => {
        recognition.start();
        document.getElementById('response').textContent = "Listening...";
    });

    // Handle speech recognition result
    recognition.onresult = function (event) {
        const userSpeech = event.results[0][0].transcript;
        document.getElementById('response').textContent = `You said: ${userSpeech}`;

        // Send the recognized speech text to the server
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

    // Handle speech recognition errors
    recognition.onerror = function (event) {
        document.getElementById('response').textContent = 'Error occurred in recognition: ' + event.error;
    };
});
