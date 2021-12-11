import pyttsx3

engine = pyttsx3.init('sapi5')


def setEngineProperties(vol, rate, voice):
    # Set Rate
    engine.setProperty('rate', rate)

    # Set Volume
    engine.setProperty('volume', vol)

    # Set Voice
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[voice].id)
