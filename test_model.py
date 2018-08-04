import numpy as np
import cv2
import time
from grabscreen import grab_screen
from DirectKeys import PressKey, ReleaseKey, W, A, S, D
from alexNet import alexnet
from  getkeys import key_check
import os

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'pygta5-car-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2',EPOCHS)

t_time = 0.04

def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)


def left():
    PressKey(A)
    PressKey(W)
    ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(A)


def right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(D)


model = alexnet(WIDTH, HEIGHT, LR)

model.load(MODEL_NAME)
def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

   # last_time = time.time()
    paused = False
    while True:
        if not paused:
            screen = grab_screen(region=(0, 40, 800, 640))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (160, 120))
           # print('loop took {} seconds'.format(time.time() - last_time))
            #last_time = time.time()
            predictions = model.predict([screen.reshape(WIDTH, HEIGHT, 1)])[0]

            turn_threshhold = 0.75
            frd_threshold = 0.7

            if predictions[1] > frd_threshold:
                straight()
            elif predictions[0] > turn_threshhold:
                left()
            elif predictions[2] > turn_threshhold:
                right()
            else:
                straight()
        key = key_check()

        if 'T' in key:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)




main()
