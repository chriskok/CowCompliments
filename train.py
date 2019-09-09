import matplotlib.pyplot as plt
import numpy as np

from darkflow.net.build import TFNet
import cv2

options = {"model": "cfg/cow_custom_full.cfg", 
         #   "load": -1,
           "load": "bin/yolov2.weights",
           "batch": 8,
           "epoch": 1000,
           "train": True,
           "annotation": "./Videos/cow_annotations/",
           "lr": 0.00001,
           "gpu": 1.0,
           "labels": "./classes.txt",
           "dataset": "./Videos/Data/"}

tfnet = TFNet(options)

tfnet.train()

# this line of code lets you save the built graph to a protobuf file (.pb)
# this step is unnecessary for this notebook
# tfnet.savepb()