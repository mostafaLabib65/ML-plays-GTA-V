import numpy as np
import cv2
import time
from grabscreen import grab_screen
from  getkeys import key_check
import os


def keys_to_output(keys):
    output = [0, 0, 0]
    if 'A' in keys:
        output[0] = 1
    elif 'W' in keys:
        output[1] = 1
    elif 'D' in keys:
        output[2] = 1
    return  output



'''
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
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)

    processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)

    vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500],
                         ], np.int32)

    processed_img = regOfInterest(processed_img, [vertices])

    # more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    #                                     rho   theta   thresh  min length, max gap:
    lines = cv2.HoughLinesP(processed_img, 1, np.pi / 180, 180, 20, 15)
    m1 = 0
    m2 = 0
    try:
        l1, l2, m1, m2 = draw_lanes(original_image, lines)
        cv2.line(original_image, (l1[0], l1[1]), (l1[2], l1[3]), [0, 255, 0], 30)
        cv2.line(original_image, (l2[0], l2[1]), (l2[2], l2[3]), [0, 255, 0], 30)
    except Exception as e:
        print(str(e))
        pass
    try:
        for coords in lines:
            coords = coords[0]
            try:
                cv2.line(processed_img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 0, 0], 3)
            except Exception as e:
                print(str(e))
    except Exception as e:
        pass

    return processed_img, original_image, m1, m2


def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)


def left():
    PressKey(A)
    ReleaseKey(W)
    ReleaseKey(D)
    ReleaseKey(A)


def right():
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(W)
    ReleaseKey(D)

def slow():
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
'''


file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('file exist ..... loading')
    training_data = list(np.load(file_name))
else:
    print('file dosen\'t exist ')
    training_data = []


def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    while True:
        screen = grab_screen(region=(0, 40, 800, 640))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (80, 60))
        keys = key_check()
        output = keys_to_output(keys)
        training_data.append([screen, output])
        #print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()

        if len(training_data) % 500 == 0:
            print(len(training_data), '\n')
            np.save(file_name, training_data)

main()
