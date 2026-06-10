import speech_recognition as sr
import pyttsx3
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

def execute_command(command):
    if "open" in command:
        app_name = command.split("open")[-1].strip()
        try:
            os.startfile(app_name)
            speak(f"Opening {app_name}")
        except Exception as e:
            speak(f"Sorry, I could not open {app_name}.")
            print(e)

if __name__ == "__main__":
    while True:
        command = listen_command()
        if "jarvis" in command:
            execute_command(command)
