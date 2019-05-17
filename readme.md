## High-Speed(about 38 fps) face detector for python

This a python binding for libfacedetection([https://github.com/ShiqiYu/libfacedetection](https://github.com/ShiqiYu/libfacedetection)).

It is only tested on  raspberry pi 3B which can reach about 38 fps  even faster. Here is the [output](https://github.com/CharlieXie/libfacedetection-python-bindings/tree/master/results).

## How to use

1. You can just download the repo and run test.py which will find right lib according to default version of python in your system.

2. Or here is an example.

   ```python
   import cv2
   import numpy as np
   # import mat and libfcnn for python3
   from rbp_py3 import mat
   from rbp_py3 import libfcnn
   image = cv2.imread("yourimage.jpg")
   # you can scale down your image to speed up.
   # minimal face which can be detected is 12*12
   # image = cv2.resize(image,(0,0),fx=0.4,fy=0.4)
   rect = libfcnn.inference(mat.Mat.from_array(resized_frame),4)
   # rect is a list of [xmin,ymin,height,weight]
   # now this lib just returns coordinate of the biggest face in the image
   # if no face detected , rect is [0,0,0,0]
   if rect[2]!=0:
    cv2.rectangle(image,(xmin,ymin),(xmax, ymax),(255,0, 0),2)
    while 1:
     cv2.imshow("Frame",image)
     key = cv2.waitKey(1) & 0xFF
     if key == ord("q"):
       break
   ```


NOTE: Now this lib just returns coordinate of the biggest face in the image. I will finish this when I can spare some time.
