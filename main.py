import pyttsx3
import speech_recognition as sr

from datetime import datetime
from random import choice
from decouple import config
from utils import opening_text
from functions.offline_operations import open_cmd, open_camera, open_calculator, open_notepad
from functions.online_operations import find_my_ip

username = config('username')
virtual_assistant = config('virtual_assistant')

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Text to Speech Conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_user():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {username}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {username}")
    elif (hour >= 16) and (hour < 20):
        speak(f"Good Evening {username}")
    else:
        speak(f"Hello {username}")
    speak(f"I am {virtual_assistant}. How may I assist you today?")


def take_user_input():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query

if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')
