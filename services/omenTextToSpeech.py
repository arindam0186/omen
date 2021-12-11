from controllers.voiceEngineController import engine


# Text to Speech Conversion

def speak(text):
    engine.say(text)
    engine.runAndWait()
