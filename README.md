# ELECTRO AI

## Overview

**Electro AI** is an advanced virtual assistant tailored for electronics enthusiasts and learners. Combining sophisticated technologies such as speech recognition, natural language processing, and text-to-speech conversion, this assistant offers a dynamic platform for exploring electronics. Users can engage with the assistant through voice commands to ask questions, generate project ideas, and receive detailed explanations, making the learning process interactive and practical.

## Features

- **Comprehensive Component Database**: Access detailed information on a wide range of electronic components, including their functionalities and applications.
- **Project Idea Generation**: Suggests project ideas based on the components users have, complete with connection instructions.
- **Interactive Learning Experience**: Engage with the assistant through voice commands for real-time responses and explanations on electronics concepts.
- **Voice-Activated Commands**: Ask about the time, open applications, search Wikipedia, and more.
- **Web-Based Interface**: A user-friendly web interface built with Flask, HTML, CSS, and JavaScript, allowing users to interact with the AI assistant from any device.

## Technologies Used

- **Python**: Core programming language for building the assistant.
- **Flask**: Web framework for creating the web-based interface.
- **HTML, CSS, JavaScript**: Frontend technologies for the web interface.
- **SpeechRecognition**: Library for converting speech to text.
- **pyttsx3**: Text-to-speech library for vocal responses.
- **Wikipedia API**: For fetching information from Wikipedia.
- **Webbrowser**: To open websites.
- **pandas**: For managing Excel data related to intents and projects.
- **openpyxl**: For reading and writing Excel files.

## Installation

To set up the project, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/kathirr0805/ElectroAI.git
   cd ElectroAI

2. **Installation**
Ensure you have Python installed. Then, install the necessary Python packages using pip:

## Imports

| Module               | Description                                             |
|----------------------|---------------------------------------------------------|
| `Flask`              | Web framework for creating the web-based interface.    |
| `render_template`    | Renders HTML templates for Flask.                      |
| `request`            | Handles HTTP requests in Flask.                        |
| `jsonify`            | Converts data to JSON format in Flask.                  |
| `pyttsx3`            | Text-to-speech library for vocal responses.            |
| `wikipedia`          | Fetches information from Wikipedia.                    |
| `os`                 | Provides functions to interact with the operating system.|
| `pandas`             | Data manipulation and analysis library.                |
| `random`             | Generates random numbers or choices.                   |
| `webbrowser`         | Opens web pages in the default browser.                |
| `datetime`           | Handles date and time operations.                      |
| `speech_recognition` | Converts speech to text.                              |
| `subprocess`         | Executes system commands.                              |
| `PyQt5.QtWidgets`    | Provides GUI elements for PyQt5 applications.          |
| `QApplication`       | Manages the application’s control flow in PyQt5.       |
| `QMainWindow`        | Main application window in PyQt5.                      |
| `QMessageBox`        | Displays message boxes in PyQt5.                       |
| `Ui_MainWindow`      | UI design class for the main window (imported from `ui_main_window`). |

## Access the Application

Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to start interacting with the AI assistant.

## Usage

**Voice Commands**: Use voice commands to interact with the assistant. For example, ask for details about an electronic component, request a project suggestion, or perform tasks like opening applications.

Commands you can use include:
- "What is [topic]?"
- "Open [website]"
- "Tell me about you"
- "What will you do?"
- "The time"
- "Shutdown"
- "Project helper"
- "Open [app]"

**Project Suggestions**: Input the components you have, and the assistant will suggest possible projects and provide connection instructions.

**Wikipedia Integration**: Ask the assistant to search for topics on Wikipedia for quick information retrieval.

## Contributing

Contributions to Electro AI are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request.

You can also report issues or request new features via the issue tracker.

## Contact

For any questions or further assistance, reach out to the project maintainer:
- Kathirr0805 - itz.kathir2005@gmail.com
- GitHub: [kathirr0805](https://github.com/kathirr0805)
