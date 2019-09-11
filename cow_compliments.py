import matplotlib.pyplot as plt
import numpy as np
from darkflow.net.build import TFNet
import cv2
import random
import pyautogui
import time

from PIL import ImageGrab
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

# X_START = 960
# Y_START = 40
# X_STOP = 1910
# Y_STOP = 930

# Smaller version
X_START = 1160
Y_START = 240
X_STOP = 1710
Y_STOP = 730

CURRENT_TIME = time.time()

def time_diff(prefix):
    global CURRENT_TIME
    print("{}: {}".format(prefix, time.time() - CURRENT_TIME))
    CURRENT_TIME = time.time()

def click_coordinates(predictions):
    result = random.choice(predictions)
    if (not result or result['confidence'] < 0.3):
        print("no cow found")
        return

    top_x = result['topleft']['x']
    top_y = result['topleft']['y']
    btm_x = result['bottomright']['x']
    btm_y = result['bottomright']['y']

    avg_x = (top_x + btm_x) / 2
    avg_y = (top_y + btm_y) / 2
    x_coord = X_START + avg_x
    y_coord = Y_START + avg_y

    # makes program execution pause for 10 sec 
    # pyautogui.moveTo(x_coord, y_coord, duration = 0.1)  
    pyautogui.click(x=x_coord, y=y_coord, button='right')

    time.sleep(0.35)
    im2=ImageGrab.grab(bbox=(x_coord-100, y_coord, x_coord + 50, y_coord + 100))
    im2.save('cow_compliment_imgs/options.png')
    MPx,MPy = click_walk_here()
    pyautogui.click(x=x_coord, y=(y_coord + MPy + 10))

def click_walk_here():
    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = cv2.imread('cow_compliment_imgs/walkhere.png')
    large_image = cv2.imread('cow_compliment_imgs/options.png')

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    return mnLoc


if __name__ == "__main__":

    options = {"model": "cfg/cow_custom_full.cfg",
           "load": 1000,
           "labels": "./classes.txt",
           "threshold": 0.5,
           "GPU": 0.8}

    tfnet2 = TFNet(options)

    tfnet2.load_from_ckpt()

    import pprint as pp
    import os

    for i in range(10):
        # Save part of the screen where osrs is
        im=ImageGrab.grab(bbox=(X_START,Y_START,X_STOP,Y_STOP)).convert('RGB')
        im.save('cow_compliment_imgs/current.png')
        # original_img = np.array(ImageGrab.grab(bbox=(X_START,Y_START,X_STOP,Y_STOP)).convert('RGB'))
        
        # Read image and make predictions
        original_img = cv2.imread('cow_compliment_imgs/current.png')
        time_diff('start pred')
        results = tfnet2.return_predict(original_img)
        time_diff('end pred')

        click_coordinates(results)
        time.sleep(0.5)


        def boxing(original_img , predictions):
            newImage = np.copy(original_img)

            for result in predictions:
                top_x = result['topleft']['x']
                top_y = result['topleft']['y']

                btm_x = result['bottomright']['x']
                btm_y = result['bottomright']['y']
                
                avg_x = int((top_x + btm_x) / 2)
                avg_y = int((top_y + btm_y) / 2)
                x_coord = X_START + avg_x
                y_coord = Y_START + avg_y

                # print('top x: {}, bot x: {}, top y: {}, bot y: {}, avg x: {}, avg y: {}, final: {}, {}'.format(top_x, btm_x, top_y, btm_y, avg_x, avg_y, x_coord, y_coord))

                confidence = result['confidence']
                label = result['label'] + " " + str(round(confidence, 3))
                
                if confidence > 0.3:
                    newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (255,0,0), 3)
                    newImage = cv2.putText(newImage, label, (top_x, top_y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.8, (0, 230, 0), 1, cv2.LINE_AA)
                    newImage = cv2.circle(newImage,  (avg_x, avg_y), 5, (255,0,0), thickness=4, lineType=8, shift=0)
            return newImage

        cv2.imwrite('cow_compliment_imgs/current_pred.png',boxing(original_img, results))

 

