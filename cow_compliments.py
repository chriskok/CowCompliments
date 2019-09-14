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

# Full Screen
X_START = 960
Y_START = 40
X_STOP = 1910
Y_STOP = 930

# Smaller version
# X_START = 1260
# Y_START = 340
# X_STOP = 1610
# Y_STOP = 630

CURRENT_TIME = time.time()

COMPLIMENT_ARRAY = ['You\'re that “Nothing” when people ask me what I\'m thinking about.\n', 'You look great today.\n', 'You\'re a smart cookie.\n', 'I bet you make babies smile.\n', 'You have impeccable manners.\n', 'I like your style.\n', 'You have the best laugh.\n', 'I appreciate you.\n', 'You are the most perfect you there is.\n', 'Our system of inside jokes is so advanced that only you and I get it. And I like that.\n', 'You\'re strong.\n', 'Your perspective is refreshing.\n', 'You\'re an awesome friend.\n', 'You light up the room.\n', 'You deserve a hug right now.\n', 'You should be proud of yourself.\n', 'You\'re more helpful than you realize.\n', 'You have a great sense of humor.\n', 'You\'ve got all the right moves!\n', 'Is that your picture next to “charming” in the dictionary?\n', 'Your kindness is a balm to all who encounter it.\n', 'You\'re all that and a super-size bag of chips.\n', 'On a scale from 1 to 10, you\'re an 11.\n', 'You are brave.\n', 'You\'re even more beautiful on the inside than you are on the outside.\n', 'You have the courage of your convictions.\n', 'Aside from food. You\'re my favorite.\n', 'If cartoon bluebirds were real, a bunch of them would be sitting on your shoulders singing right now.\n', 'You are making a difference.\n', 'You\'re like sunshine on a rainy day.\n', 'You bring out the best in other people.\n', 'Your ability to recall random factoids at just the right time is impressive.\n', 'You\'re a great listener.\n', 'How is it that you always look great, even in sweatpants?\n', 'Everything would be better if more people were like you!\n', 'I bet you sweat glitter.\n', 'You were cool way before hipsters were cool.\n', 'That color is perfect on you.\n', 'Hanging out with you is always a blast.\n', 'You always know — and say — exactly what I need to hear when I need to hear it.\n', 'You smell really good.\n', 'You may dance like no one\'s watching, but everyone\'s watching because you\'re an amazing dancer!\n', 'Being around you makes everything better!\n', 'When you say, “I meant to do that,” I totally believe you.\n', 'When you\'re not afraid to be yourself is when you\'re most incredible.\n', 'Colors seem brighter when you\'re around.\n', 'You\'re more fun than a ball pit filled with candy. (And seriously, what could be more fun than that?)\n', 'That thing you don\'t like about yourself is what makes you so interesting.\n', 'You\'re wonderful.\n', 'Everyday is just BLAH when I don\'t see you For reals! (awesome – you are halfway through the list. You\'re awesome!)\n', 'Jokes are funnier when you tell them.\n', 'You\'re better than a triple-scoop ice cream cone. With sprinkles.\n', 'Your bellybutton is kind of adorable.\n', 'Your hair looks stunning.\n', 'You\'re one of a kind!\n', 'You\'re inspiring.\n', 'If you were a box of crayons, you\'d be the giant name-brand one with the built-in sharpener.\n', 'You should be thanked more often. So thank you!!\n', 'Our community is better because you\'re in it.\n', 'Someone is getting through something hard right now because you\'ve got their back.\n', 'You have the best ideas.\n', 'You always know how to find that silver lining.\n', 'Everyone gets knocked down sometimes, but you always get back up and keep going.\n', 'You\'re a candle in the darkness.\n', 'You\'re a great example to others.\n', 'Being around you is like being on a happy little vacation.\n', 'You always know just what to say.\n', 'You\'re always learning new things and trying to better yourself, which is awesome.\n', 'If someone based an Internet meme on you, it would have impeccable grammar.\n', 'You could survive a Zombie apocalypse.\n', 'You\'re more fun than bubble wrap.\n', 'When you make a mistake, you fix it.\n', 'Who raised you? They deserve a medal for a job well done.\n', 'You\'re great at figuring stuff out.\n', 'Your voice is magnificent.\n', 'The people you love are lucky to have you in their lives.\n', 'You\'re like a breath of fresh air.\n', 'You\'re gorgeous — and that\'s the least interesting thing about you, too.\n', 'You\'re so thoughtful.\n', 'Your creative potential seems limitless.\n', 'You\'re the coolest person I know. And I consider myself bet friends with like all celebrities, so. . . .\n', 'You\'re irresistible when you blush.\n', 'Actions speak louder than words, and yours tell an incredible story.\n', 'Somehow you make time stop and fly at the same time.\n', 'When you make up your mind about something, nothing stands in your way.\n', 'You seem to really know who you are.\n', 'Any team would be lucky to have you on it.\n', 'In high school I bet you were voted “most likely to keep being awesome.”\n', 'I bet you do the crossword puzzle in ink.\n', 'Babies and small animals probably love you.\n', 'If you were a scented candle they\'d call it Perfectly Imperfect (and it would smell like summer).\n', 'There\'s ordinary, and then there\'s you.\n', 'You\'re someone\'s reason to smile.\n', 'You\'re even better than a unicorn, because you\'re real.\n', 'How do you keep being so funny and making everyone laugh?\n', 'You have a good head on your shoulders.\n', 'Has anyone ever told you that you have great posture?\n', 'The way you treasure your loved ones is incredible.\n', 'You\'re really something special.\n', 'You\'re a gift to those around you.']

def time_diff(prefix):
    global CURRENT_TIME
    print("{}: {}".format(prefix, time.time() - CURRENT_TIME))
    CURRENT_TIME = time.time()

def click_coordinates(predictions):
    if predictions is None:
        print("no cow found")
        return
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
    pyautogui.click(x=x_coord, y=y_coord, button='left', duration = 0.3)

    pyautogui.typewrite(COMPLIMENT_ARRAY[random.randint(0, len(COMPLIMENT_ARRAY) - 1)], interval=0.10)
    # MUAHAHAHAH
    # time.sleep(0.35)
    # im2=ImageGrab.grab(bbox=(x_coord-100, y_coord, x_coord + 50, y_coord + 100))
    # im2.save('cow_compliment_imgs/options.png')
    # MPx,MPy = click_walk_here()
    # pyautogui.click(x=x_coord, y=(y_coord + MPy + 10))

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
           "threshold": 0.1,
           "GPU": 1.0}

    tfnet2 = TFNet(options)

    tfnet2.load_from_ckpt()

    import pprint as pp
    import os

    # for i in range(10):
    while True:
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
        time.sleep(5)


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

 

