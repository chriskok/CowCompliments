import matplotlib.pyplot as plt
import numpy as np

from darkflow.net.build import TFNet
import cv2
# options = {"model": "darkflow/cfg/yolov2.cfg", "load": "darkflow/bin/yolov2.weights", "threshold": 0.6, "labels": "darkflow/cfg/coco.names"}

options = {"model": "darkflow/cfg/yolo_custom.cfg", 
           "load": "darkflow/bin/yolov2.weights",
           "batch": 8,
           "epoch": 150,
           "train": True,
           "annotation": "./cow_annotations/",
           "lr": 0.001,
           "gpu": 1.0,
        #    "labels": "./darkflow/labels.txt",
           "labels": "./classes.txt",
           "dataset": "./cow_images/"}


tfnet = TFNet(options)

tfnet.train()

# this line of code lets you save the built graph to a protobuf file (.pb)
# this step is unnecessary for this notebook
tfnet.savepb()