from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_voice', methods=['POST'])
def process_voice():
    data = request.get_json()
    command = data.get('command')
    
    response_text = "I didn't understand that. Can you repeat?"
    
    if command:
        response_text = f"You said: {command}"
        # Add custom logic to handle specific commands here
        if 'hello' in command.lower():
            response_text = "Hello! How can I assist you today?"
        elif 'time' in command.lower():
            from datetime import datetime
            response_text = f"The current time is {datetime.now().strftime('%I:%M %p')}"
        
        speak(response_text)
    
    return jsonify({ 'response': response_text })

if __name__ == '__main__':
    app.run(debug=True)
