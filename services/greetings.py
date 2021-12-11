from controllers.configController import user, virtual_assistant
from services.currentDateTime import h, time
from services.omenTextToSpeech import speak


def greet_user():
    if (h >= 6) and (h < 12):
        speak(f"Good Morning {user}")
    elif (h >= 12) and (h < 16):
        speak(f"Good afternoon {user}")
    elif (h >= 16) and (h < 20):
        speak(f"Good Evening {user}")
    else:
        speak(f"Hello {user}")
    speak(f'Current time is {time}')
    speak(f"My name is {virtual_assistant}, your virtual assistant. How may I assist you today?")
