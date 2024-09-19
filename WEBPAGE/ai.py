from flask import Flask, render_template, request, jsonify
import pyttsx3
import wikipedia
import os
import pandas as pd
import random
import webbrowser  # Add missing import for web browser
import datetime

app = Flask(__name__)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Setting up properties for female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Load intents and projects from Excel files
def load_intents():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    intents_file_path = os.path.join(script_dir, 'Intents', 'intents.xlsx')
    intents_df = pd.read_excel(intents_file_path, engine='openpyxl') if os.path.exists(intents_file_path) else pd.DataFrame(columns=['Intent', 'Pattern', 'Response'])
    intents = {}
    for _, row in intents_df.iterrows():
        intent = row['Intent']
        pattern = row['Pattern'].lower()
        response = row['Response']
        if intent not in intents:
            intents[intent] = {"patterns": [], "responses": []}
        intents[intent]["patterns"].append(pattern)
        intents[intent]["responses"].append(response)
    return intents

def load_projects():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    projects_file_path = os.path.join(script_dir, 'Projects', 'projects.xlsx')
    projects_df = pd.read_excel(projects_file_path, engine='openpyxl') if os.path.exists(projects_file_path) else pd.DataFrame(columns=['Project', 'Components', 'Connection'])
    projects = {}
    for _, row in projects_df.iterrows():
        project = row['Project']
        components = row['Components'].split(', ')
        connection = row['Connection']
        projects[project] = {"components": components, "connection": connection}
    return projects

intents = load_intents()
projects = load_projects()

# Function to generate a response based on user input
def process_user_input(user_input):
    user_input_lower = user_input.lower()
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern.lower() in user_input_lower:
                return random.choice(data["responses"])
    return "I'm sorry, I don't understand that."

# Function to suggest a project based on components
def suggest_project(components):
    for project, details in projects.items():
        if all(comp.lower() in components.lower() for comp in details["components"]):
            return f"{project}:\n{details['connection']}"
    return "I couldn't find a suitable project based on the components you provided."

# Function to speak out and print text
def speak(text):
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the POST request for user input
@app.route('/get_response', methods=['POST'])
def handle_user_response():
    data = request.json
    user_input = data['query']
    
    # Call your process_user_input function based on user input
    response_text = process_user_input(user_input)

    return jsonify({'response': response_text})

@app.route('/get', methods=['POST'])
def get_response_route():
    user_input = request.form['user_input']  # assuming input comes from a form
    response_text = process_user_input(user_input)  # Pass user input to the function
    return jsonify({'response': response_text})

@app.route('/process', methods=['POST'])
def process_request():
    query = request.form.get('query')

    if query.startswith('open '):
        website = query.split('open ')[1]
        if not website.endswith('.com'):
            website += '.com'
        webbrowser.open(website)
        return jsonify({"response": f"Opening {website}"})

    elif 'project helper' in query:
        components = request.form.get('components')
        project_response = suggest_project(components)
        return jsonify({"response": project_response})

    elif 'what is' in query:
        query = query.replace('what is', '')
        try:
            results = wikipedia.summary(query, sentences=2)
            return jsonify({"response": results})
        except wikipedia.exceptions.PageError:
            return jsonify({"response": "Sorry, I couldn't find any information on that topic."})

    else:
        response = process_user_input(query)
        return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
