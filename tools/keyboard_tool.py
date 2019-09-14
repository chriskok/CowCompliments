import pyautogui

def bot_speak(msg):
    pyautogui.typewrite(msg, interval=0.25)
    pyautogui.press('enter')  # press the Enter key 

def main():
    # f= open("guru99.txt","w+")
    # #f=open("guru99.txt","a+")
    # for i in range(10):
    #      f.write("This is line %d\r\n" % (i+1))
    # f.close()

    #Open the file and read the contents
    f=open("cow_compliments.py", "r")
    fl =f.readlines()
    for x in fl:
        bot_speak(x)
if __name__== "__main__":
    main()