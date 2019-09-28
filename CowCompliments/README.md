# Cow Compliments
Complimenting cows all over old school runescape with machine learning and python


## Installation
- git clone with submodules:
```
git clone --recurse-submodules https://github.com/chriskok/SillySoftware.git
```
- git add submodules after just cloning:
```
git clone https://github.com/chriskok/SillySoftware.git
git submodule update --init --recursive
```


## Usage
- Download this zip file and unzip in current folder: https://drive.google.com/open?id=1aOa6Pz8x73K6poHSY4v02irGl-3Ag2Ud
- Download the weights from https://github.com/thtrieu/darkflow and create a /bin folder to put it in. I downloaded yolov2.weights.
- Change the following in cow_compliments.py: X_START, Y_START, X_STOP, Y_STOP
- Run the following:
```
python cow_compliments.py
```


## Process For Retraining
1. Use Free Cam (https://www.freescreenrecording.com/) to capture a video of me walking amongst cows
2. Use VLC to split the photos into pictures of each frame
3. Use labelImg tool (after pip3 install labelImg) in the directory of the same name to label and create annotations for each image. The command is:
```
labelimg ..\Videos\Data data\predefined_classes.txt
```
4. Download training weights (put in /bin), create /ckpt and create custom cfg file (in /cfg)
5. Train the darkflow model with new annotations (python test_train.py)
6. To test prediction:
```
python darkflow\flow --model cfg/cow_custom_full.cfg --load -1 --demo Videos\CowData.wmv --labels .\classes.txt
```


## TODO
- Look into preprocessing images and maybe hyperparameter tuning for yolo? 


## Notes
- get images to label, inside google_images_download/google_images_download (python google_images_download.py --keywords "osrs cows" --limit 40 --format jpg)
- To save a video with predicted bounding box, add --saveVideo option.
- Use different version of ckpt saved models for different accuracy or to avoid overfitting
- CKPT 750 was loss of around 9, CKPT 1500 was around 2, CKPT 500 could have been like 25
- Very far from realtime on my Windows Intel i5 Processor, which makes sense (about 3.1 seconds to predict without anything else open)
- Even slower if free cam is running (3.8 seconds)