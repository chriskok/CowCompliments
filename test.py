import matplotlib.pyplot as plt
import numpy as np

from darkflow.net.build import TFNet
import cv2

# # flow --imgdir sample_img/ --model cfg/yolov2.cfg --labels cfg/coco.names --load bin/yolov2.weights
# options = {"model": "darkflow/cfg/yolov2.cfg", "load": "darkflow/bin/yolov2.weights", "threshold": 0.6, "labels": "darkflow/cfg/coco.names"}

# tfnet = TFNet(options)

# imgcv = cv2.imread("./darkflow/sample_img/sample_dog.jpg")

# for i in range (30):
#     result = tfnet.return_predict(imgcv)
#     print(result)

options = {"model": "./darkflow/cfg/yolo_custom.cfg",
           "load": -1,
           "labels": "./classes.txt",
           "gpu": 1.0}

tfnet2 = TFNet(options)

tfnet2.load_from_ckpt()

import pprint as pp
import os

pathname = './cow_images'

for filename in os.listdir(pathname): 

    original_img = cv2.imread(pathname + '/' + filename)
    original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
    results = tfnet2.return_predict(original_img)
    print(results)

    fig, ax = plt.subplots(figsize=(15, 15))
    ax.imshow(original_img)
    # plt.show()

    def boxing(original_img , predictions):
        newImage = np.copy(original_img)

        for result in predictions:
            top_x = result['topleft']['x']
            top_y = result['topleft']['y']

            btm_x = result['bottomright']['x']
            btm_y = result['bottomright']['y']

            confidence = result['confidence']
            label = result['label'] + " " + str(round(confidence, 3))
            
            if confidence > 0.3:
                newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (255,0,0), 3)
                newImage = cv2.putText(newImage, label, (top_x, top_y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.8, (0, 230, 0), 1, cv2.LINE_AA)
            
        return newImage

    fig, ax = plt.subplots(figsize=(20, 10))
    ax.imshow(boxing(original_img, results))
    # plt.show()