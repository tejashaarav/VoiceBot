import pygame
from pygame import mixer
import time
from mutagen.mp3 import MP3

mixer.init()
mixer.init()
mixer.music.load("res.mp3")
song = MP3('res.mp3')
songlen = song.info.length
print("time delay starts from now")
time.sleep(float(songlen) + 1)

print("hi this kinda works brother")
