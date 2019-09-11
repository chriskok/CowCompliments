from PIL import ImageGrab
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()
from pynput.mouse import Listener, Button
import cv2
import pyautogui
import time

if __name__ == "__main__":


    # part of the screen
    # im=ImageGrab.grab(bbox=(960,40,1910,930))
    # im.show()

    # im=ImageGrab.grab(bbox=(pos[0] - 30, pos[1] + 20, pos[0], pos[1] + 50))
    # to file
    # im.save('im2.png')
    print('hi')

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

def on_click(x, y, button, pressed):
    print(x, y, button, pressed)

    if (button == Button.right and pressed == True):
        # im=ImageGrab.grab(bbox=(x-60, y + 25, x + 30, y + 40))
        # im.save('cow_compliment_imgs/walkhere.png')
        time.sleep(0.35)
        im2=ImageGrab.grab(bbox=(x-100, y , x + 50, y + 100))
        im2.save('cow_compliment_imgs/options.png')
        # time.sleep(2)
        MPx,MPy = click_walk_here()
        # pyautogui.click(x=MPx, y=MPy)
        pyautogui.moveTo(x, y + MPy + 10, duration = 0.1)
    elif button == Button.left:
        raise MyException(x)


class MyException(Exception): pass

with Listener(on_click=on_click) as listener:
    listener.join()