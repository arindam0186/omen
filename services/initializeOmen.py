import time

from tqdm import tqdm

from controllers.voiceEngineController import setEngineProperties
from services.omenTextToSpeech import speak
from util.engineConfig import voice, defVolume, defRate, initRate, initVolume


def initialize_omen():
    setEngineProperties(initVolume, initRate, voice)

    for i in tqdm(range(100), ncols=100, desc='Initializing OMEN......', bar_format='{l_bar}{bar}|'):
        if i == 99:
            speak('Initializing Omen')
        time.sleep(.01)
    setEngineProperties(defVolume, defRate, voice)
