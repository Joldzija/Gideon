from win32api import GetKeyState
import threading
import time
import pyttsx3
import speech_recognition as sr 
import wikipedia 
import pyaudio
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

def key_down(key):
        state = GetKeyState(key)
        if (state != 0) and (state != 1):
            return True
        else:
            return False

def speak(text):
    engine.say(text)
    engine.runAndWait() 

def starter():
    while True:
        if key_down(56):
            takeCommand()
        time.sleep(0.2)
def takeCommand():
    ear = sr.Recognizer()
    with sr.Microphone() as source:
        speak("How can i help you...")
        audio = ear.listen(source)

    try:
        print("Recognizing...")
        query = ear.recognize_google(audio)
        speak(query)
        resolveCommand(query)
    except Exception as e:
        print(e)
        speak("No commands")

def resolveCommand(query):

    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        speak(results)

    elif 'who made you' in query.lower():
        speak('yolgiya created me')

    elif 'who are you' in query.lower():
        speak('Hi i am Gideon an interactive artificial consciousness')
    
    elif 'open youtube' in query.lower():
        print('openning yt')
        url = "https://www.youtube.com/"
        webbrowser.open_new(url)
        
starter()
