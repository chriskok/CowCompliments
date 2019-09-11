from PIL import ImageGrab
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()
from pynput.mouse import Listener, Button

if __name__ == "__main__":


    # part of the screen
    # im=ImageGrab.grab(bbox=(960,40,1910,930))
    # im.show()

    # im=ImageGrab.grab(bbox=(pos[0] - 30, pos[1] + 20, pos[0], pos[1] + 50))
    # to file
    # im.save('im2.png')
    print('hi')


# def on_click(x, y, button, pressed):
#     print(x, y, button, pressed)

#     if (button == Button.right):
#         im=ImageGrab.grab(bbox=(x-60, y + 25, x + 30, y + 40))
#         im.save('walkhere.png')
    
#     if button == Button.left:
#         raise MyException(x)


# class MyException(Exception): pass

# with Listener(on_click=on_click) as listener:
#     listener.join()