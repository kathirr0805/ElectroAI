# main.py

import sys
import pandas as pd
import pyttsx3
import datetime
import wikipedia
import webbrowser
import random
from speech_recognition import Recognizer, Microphone
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main_window import Ui_MainWindow

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Setting up properties for female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Index 1 typically corresponds to a female voice

# Determine the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load intents from Excel
intents_file_path = os.path.join(script_dir, 'Intents', 'intents.xlsx')
intents_df = pd.read_excel(intents_file_path, engine='openpyxl')

# Convert DataFrame to dictionary
intents = {}
for _, row in intents_df.iterrows():
    intent = row['Intent']
    pattern = row['Pattern'].lower()
    response = row['Response']
    
    if intent not in intents:
        intents[intent] = {"patterns": [], "responses": []}
    
    intents[intent]["patterns"].append(pattern)
    intents[intent]["responses"].append(response)

# Load projects from Excel
projects_file_path = os.path.join(script_dir, 'Projects', 'projects.xlsx')
projects_df = pd.read_excel(projects_file_path, engine='openpyxl')

# Convert DataFrame to dictionary
projects = {}
for _, row in projects_df.iterrows():
    project = row['Project']
    components = row['Components'].split(', ')
    connection = row['Connection']
    projects[project] = {"components": components, "connection": connection}

# Function to generate a response based on user input
def get_response(user_input):
    user_input_lower = user_input.lower()  # Convert user_input to lowercase
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            pattern_lower = pattern.lower()  # Convert pattern to lowercase
            if pattern_lower in user_input_lower:
                return random.choice(data["responses"])
    return "I'm sorry, I don't understand that."

# Function to suggest a project based on user components
def suggest_project(components):
    for project, details in projects.items():
        if all(comp.lower() in components.lower() for comp in details["components"]):
            response = f"{project}:\n{details['connection']}"
            return response
    return "I couldn't find a suitable project based on the components you provided."

# Function to speak out and print text
def speak_and_print(text, rate=150):
    print(text)
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def take_command():
    r = Recognizer()
    with Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak_and_print("Say that again please...")
        return "None"
    return query

# Main Window Class
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.radioChat.toggled.connect(self.on_radio_chat_toggled)
        self.radioVoice.toggled.connect(self.on_radio_voice_toggled)
        self.submitChat.clicked.connect(self.handle_chat)
        self.voiceButton.clicked.connect(self.handle_voice)
        
        self.setup_initial_mode()

    def setup_initial_mode(self):
        self.chat_mode = self.radioChat.isChecked()
        self.voice_mode = self.radioVoice.isChecked()

        self.userInput.setVisible(self.chat_mode)
        self.submitChat.setVisible(self.chat_mode)
        self.voiceButton.setVisible(self.voice_mode)
    
    def on_radio_chat_toggled(self):
        if self.radioChat.isChecked():
            self.chat_mode = True
            self.voice_mode = False
        self.update_mode()
    
    def on_radio_voice_toggled(self):
        if self.radioVoice.isChecked():
            self.chat_mode = False
            self.voice_mode = True
        self.update_mode()
    
    def update_mode(self):
        self.userInput.setVisible(self.chat_mode)
        self.submitChat.setVisible(self.chat_mode)
        self.voiceButton.setVisible(self.voice_mode)
        if self.voice_mode:
            self.responseDisplay.setText("Press the 'Voice Command' button to start listening.")
    
    def handle_chat(self):
        if not self.chat_mode:
            return
        user_input = self.userInput.text()
        if user_input:
            response = get_response(user_input)
            self.responseDisplay.setText(response)
            speak_and_print(response)
    
    def handle_voice(self):
        if not self.voice_mode:
            return
        command = take_command()
        response = get_response(command)
        self.responseDisplay.setText(response)
        speak_and_print(response)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
