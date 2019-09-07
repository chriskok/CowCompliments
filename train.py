import matplotlib.pyplot as plt
import numpy as np

from darkflow.net.build import TFNet
import cv2
# options = {"model": "darkflow/cfg/yolov2.cfg", "load": "darkflow/bin/yolov2.weights", "threshold": 0.6, "labels": "darkflow/cfg/coco.names"}

options = {"model": "darkflow/cfg/yolo_custom.cfg", 
           "load": "darkflow/bin/yolov2.weights",
           "batch": 8,
           "epoch": 30000,
           "train": True,
           "annotation": "./cow_anno_2/",
           "lr": 0.00001,
           "gpu": 1.0,
        #    "labels": "./darkflow/cfg/coco.names",
           "labels": "./classes.txt",
           "dataset": "./cow_images_2/"}


tfnet = TFNet(options)

tfnet.train()

# this line of code lets you save the built graph to a protobuf file (.pb)
# this step is unnecessary for this notebook
# tfnet.savepb()