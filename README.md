# SillySoftware
Creating silly software for fun

## Process
1. Use Free Cam (https://www.freescreenrecording.com/) to capture a video of me walking amongst cows
2. Use VLC to split the photos into pictures of each frame
3. Use labelImg tool (after pip3 install labelImg) in the directory of the same name to label and create annotations for each image. The command is:
```
labelimg ..\Videos\Data data\predefined_classes.txt
```
4. Download training weights (put in /bin), create /ckpt and create custom cfg file (in /cfg)
5. Train the darkflow model with new annotations (python test_train.py)

## TODO
- create program to run and get output in runescape 

## Installation
- git clone with submodules:
```
git clone --recurse-submodules -j8 https://github.com/chriskok/SillySoftware.git
```

- git add submodules after just cloning:
```
git clone https://github.com/chriskok/SillySoftware.git
git submodule update --init --recursive
```

## Notes
- get images to label, inside google_images_download/google_images_download (python google_images_download.py --keywords "osrs cows" --limit 40 --format jpg)