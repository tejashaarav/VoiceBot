import numpy as np
import pandas as pd
import os
import datetime
import sys
import speech_recognition as sr
from gtts import gTTS
import os
from pygame import mixer
from mutagen.mp3 import MP3
import time
import transformers





class ChatBot():
    def __init__(self, name, language):
        print(".........Starting Bot", name, "...........")
        self.name = name
        self.language = 
    

    def speech_to_text(self, language):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            print("Listening....")
            audio = recognizer.listen(mic)

        try:
            self.text = recognizer.recognize_google(audio, language= language)
            print("Tejash : ", self.text)
        
        except:
            print("Tejash : Error")
    
    
    
    @staticmethod
    def text_to_speech(text):
        
        print("ai --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        os.system("start res.mp3")
        # mixer.init()
        # mixer.music.load("res.mp3")
        song = MP3('res.mp3')
        songlen = song.info.length
        # mixer.music.set_volume(0.7)
        # mixer.music.play() 
        time.sleep(float(songlen) + 1)
        os.remove("res.mp3")

    
    def wake_up(self, text):
        return True if self.name in text.lower() else False
    

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')
    


    

    

        



if __name__ == "__main__":
    ai = ChatBot(name = "siri")
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"

    while True:
        ai.speech_to_text()

        if ai.wake_up(ai.text) is True:
            res = "Hello Tejash I'm Siri, what's up?"
        elif "time" in ai.text:

            res = ai.action_time()
        
         ## respond politely
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(
                  ["you're welcome!","anytime!",
                   "no problem!","cool!",
                   "I'm here if you need me!","peace out!"])
        else:
            chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
            res = str(chat)
            res = res[res.find("bot >> ")+6:].strip()

        
        ai.text_to_speech(res)