import numpy as np
from PIL import ImageGrab
import cv2
import time
from DirectKeys import ReleaseKey, PressKey, W, A, S, D




last_time = time.time()
def process_img(image):
    processing_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processing_img = cv2.Canny(processing_img, threshold1=200, threshold2=300)
    return processing_img

for i in list(range(6))[::-1]:
    print(i+1)
    time.sleep(1)

while True:
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
    new_screen = process_img(screen)
   # print('down')
    #PressKey(W)
    #print('up')
    #print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow('window', new_screen)
    #cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord ('q'):
        cv2.destroyAllWindows()
        break

