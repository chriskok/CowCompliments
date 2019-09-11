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

def click_coordinates(predictions):
    result = random.choice(predictions)
    if (not result or result['confidence'] < 0.3):
        return
        print("no cow found")

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
    pyautogui.click(x=x_coord, y=(y_coord + 50))

def click_walk_here():
    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = cv2.imread('small_image.png')
    large_image = cv2.imread('large_image.jpeg')

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]

    # Step 3: Draw the rectangle on large_image
    cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

    # Display the original image with the rectangle around the match.
    cv2.imshow('output',large_image)

    # The image is only displayed if we call this
    cv2.waitKey(0)


if __name__ == "__main__":

    options = {"model": "cfg/cow_custom_full.cfg",
           "load": 1000,
           "labels": "./classes.txt",
           "threshold": 0.1}

    tfnet2 = TFNet(options)

    tfnet2.load_from_ckpt()

    import pprint as pp
    import os

    for i in range(1000):
        # Save part of the screen where osrs is
        im=ImageGrab.grab(bbox=(X_START,Y_START,X_STOP,Y_STOP)).convert('RGB')
        im.save('cow_compliment_imgs/current.png')
        # original_img = np.array(ImageGrab.grab(bbox=(X_START,Y_START,X_STOP,Y_STOP)).convert('RGB'))

        # Read image and make predictions
        original_img = cv2.imread('cow_compliment_imgs/current.png')
        results = tfnet2.return_predict(original_img)

        click_coordinates(results)
        time.sleep(0.5)


        # def boxing(original_img , predictions):
        #     newImage = np.copy(original_img)

        #     for result in predictions:
        #         top_x = result['topleft']['x']
        #         top_y = result['topleft']['y']

        #         btm_x = result['bottomright']['x']
        #         btm_y = result['bottomright']['y']

        #         confidence = result['confidence']
        #         label = result['label'] + " " + str(round(confidence, 3))
                
        #         if confidence > 0.3:
        #             newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (255,0,0), 3)
        #             newImage = cv2.putText(newImage, label, (top_x, top_y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.8, (0, 230, 0), 1, cv2.LINE_AA)
                
        #     return newImage

        # fig, ax = plt.subplots(figsize=(20, 10))
        # ax.imshow(boxing(original_img, results))
        # plt.show()

 

