import pandas as pd
import pyttsx3
import datetime
import wikipedia
import webbrowser
import random
from speech_recognition import Recognizer, Microphone
import os
import subprocess

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Setting up properties for female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Index 1 typically corresponds to a female voice

# Determine the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load intents from Excel in the 'Intents' folder
intents_file_path = os.path.join(script_dir, 'Intents', 'intents.xlsx')
if os.path.exists(intents_file_path):
    intents_df = pd.read_excel(intents_file_path, engine='openpyxl')
else:
    print(f"Error: The file {intents_file_path} does not exist.")
    intents_df = pd.DataFrame(columns=['Intent', 'Pattern', 'Response'])

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

# Load projects from Excel in the 'Projects' folder
projects_file_path = os.path.join(script_dir, 'Projects', 'projects.xlsx')
if os.path.exists(projects_file_path):
    projects_df = pd.read_excel(projects_file_path, engine='openpyxl')
else:
    print(f"Error: The file {projects_file_path} does not exist.")
    projects_df = pd.DataFrame(columns=['Project', 'Components', 'Connection'])

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

# Function to wish user as per the current time
def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak_and_print("Good Morning")
    elif 12 <= hour < 18:
        speak_and_print("Good Afternoon")
    else:
        speak_and_print("Good Evening")
    speak_and_print("I am Electro AI. How may I assist you today?")

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()
        # Logic for executing tasks based on query
        if 'what is' in query:
            query = query.replace("what is", "")
            try:
                results = wikipedia.summary(query, sentences=3)
                speak_and_print(results)
            except wikipedia.exceptions.PageError:
                speak_and_print("Sorry, I couldn't find any information on that topic.")
            except wikipedia.exceptions.DisambiguationError:
                speak_and_print("There are multiple possible meanings for this term. Please be more specific.")
        elif query.startswith('open '):
            website = query.split('open ')[1]
            if not website.endswith('.com'):
                website += '.com'
            webbrowser.open(website)
            speak_and_print(f"Opening {website.capitalize()}")
        elif 'tell about you' in query:
            speak_and_print("I am Electronics Assistant Robot made by Kathir Kaavyasrie Thanushree Hamsaveni...I will be very useful if you are a ECE engineer")
        elif 'what will you do' in query:
            speak_and_print("I will help you to understand the concepts of Basics in Electronics..But I am still in under development...But still I will give you the connections of any circuits if you give or show just the components...")
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak_and_print(f"The time is {str_time}")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")  
        elif 'project helper' in query:
            speak_and_print("Sure, I can help you with project ideas based on the components you have. Please list the components you have.")
            user_components = take_command()
            project_idea = suggest_project(user_components)
            speak_and_print(project_idea)
        elif 'app' in query:
            app_name = query.split('app ')[1].lower()  
            app_executables = {
                'calculator': 'C:\\Windows\\System32\\calc.exe',
                'notepad': 'C:\\Windows\\System32\\notepad.exe',
                'Edge': 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
                'word': 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE',
                'excel': 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE',
                'powerpoint': 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE',
                'proteus': r'C:\Program Files (x86)\Labcenter Electronics\Proteus 8 Professional\BIN\PDS.EXE',
                'matlab': r'C:\Program Files\MATLAB\R2013a\bin\matlab.exe',
                'arduino': r'C:\Users\Home\AppData\Local\Programs\Arduino IDE\Arduino IDE.exe',
                'kicad': r'C:\Program Files\KiCad\8.0\bin\kicad.exe',
                'pcb': r'C:\Program Files\KiCad\8.0\bin\kicad.exe',
            }
            if app_name in app_executables:
                app_executable = app_executables[app_name]
                subprocess.Popen(app_executable)  # Open the specified app
                speak_and_print(f"Opening {app_name.capitalize()} application")
            else:
                speak_and_print("App not found. Please specify a valid app name.")      
        elif 'exit' in query or 'bye' in query:
            speak_and_print("Goodbye")
            exit()
        else:
            response = get_response(query)
            speak_and_print(response)
