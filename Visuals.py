import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from DirectKeys import ReleaseKey, PressKey, W, A, S, D


def regOfInterest(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def draw_lines(img, lines):
    try:
        for line in lines:
            cords = line[0]
            cv2.line(img, (cords[0], cords[1]), (cords[2], cords[3]), [255, 255, 255], 3)
    except:
        pass


def process_img(image):
    processing_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processing_img = cv2.Canny(processing_img, threshold1=200, threshold2=300)
    processing_img = cv2.GaussianBlur(processing_img, (5, 5), 0)
    vertices = np.array([[10, 450], [10, 300], [266, 150], [532, 150], [800, 300], [800, 450]])
    processing_img = regOfInterest(processing_img, [vertices])
    lines = cv2.HoughLinesP(processing_img, 1, np.pi/180, 180, 50, 20)
    draw_lines(processing_img,lines)
    return processing_img


def main():
    last_time = time.time()
    while True:
        screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
        new_screen = process_img(screen)
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('window', new_screen)
        #cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord ('q'):
            cv2.destroyAllWindows()
            break

main()