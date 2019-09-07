# SillySoftware
Creating silly software for fun

## Process

## TODO
- get images to label, inside google_images_download/google_images_download (python google_images_download.py --keywords "osrs cows" --limit 40 --format jpg)
- label images for annotations (python3 labelImg/labelImg.py cow_images)
- train darkflow model with the new annotations ( python test_train.py )
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
