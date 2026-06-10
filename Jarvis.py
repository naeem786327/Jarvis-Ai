import pyttsx3
import speech_recognition as sr
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, boss I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

def open_application(command):
    if 'browser' in command:
        webbrowser.open('http://www.google.com')
        speak("Open web browser.")
    if 'whatsapp' in command:
        webbrowser.open('https://web.whatsapp.com/')
        speak("Open whatsapp.")
    if 'chrome' in command:
        webbrowser.open('chrome://newtab/https://web.whatsapp.com/')
        speak("Open chrome.")
    if 'playlist' in command:
        webbrowser.open('https://www.youtube.com/watch?v=mrFvRJCNlwU&ab_channel=MuhammadAlMuqit')
        speak("Open my naats playlist.")


    if 'youtube' in command:
        webbrowser.open('https://www.youtube.com/watch?v=1I5EmZvofkE&list=RDGMEMgGOgHdkrBSNHvacS9Sp8bgVM1I5EmZvofkE&start_radio=1&ab_channel=ThraceMusic')
        speak("open youtube.")
    elif 'notepad' in command:
        os.startfile('notepad.exe')
        speak("Open Notepad.")
    elif 'calculator' in command:
        os.startfile('calc.exe')
        speak("Open Calculator.")
    else:
        speak("Sorry,boss I can't open that.")

def main():
    speak("Hello, Sir . how are you boss today ?")
    while True:
        command = listen()
        if 'exit' in command:
            speak("Goodbye")
            break
        open_application(command)

if __name__ == "__main__":
    main()
    speak("take care boss")