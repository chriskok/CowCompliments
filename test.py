from darkflow.net.build import TFNet
import cv2

# flow --imgdir sample_img/ --model cfg/yolov2.cfg --labels cfg/coco.names --load bin/yolov2.weights
options = {"model": "darkflow/cfg/yolov2.cfg", "load": "darkflow/bin/yolov2.weights", "threshold": 0.6, "labels": "darkflow/cfg/coco.names"}

tfnet = TFNet(options)

imgcv = cv2.imread("./darkflow/sample_img/sample_dog.jpg")

for i in range (30):
    result = tfnet.return_predict(imgcv)
    print(result)