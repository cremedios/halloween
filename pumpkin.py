#! /usr/bin/env python

from os import listdir
import sys, pygame, time
import RPi.GPIO as GPIO
from datetime import datetime

print(f"{datetime.now()}: Starting up")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)  #Read output from PIR motion sensor

pygame.mixer.init()
sounds = [pygame.mixer.Sound("sounds/"+sound) for sound in listdir('sounds')]
sound_pivot = 0

while True:
    if datetime.now().time().hour > 20:
        print(f"{datetime.now()}: Time to go to bed")
        pygame.quit()
        sys.exit()

    if GPIO.input(7)==1:    #When output from motion sensor is HIGH
        print(f"{datetime.now()}: Movement detected")
        sounds[sound_pivot % len(sounds)].play()
        sound_pivot+=1
        time.sleep(15)
    else :        
        time.sleep(2)
        