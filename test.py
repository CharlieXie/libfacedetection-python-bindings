import cv2
import numpy as np 
import time
from collections import deque
import sys
PY2 = sys.version_info[0] == 2
print(PY2)
PY3 = sys.version_info[0] == 3
print(PY3)
if PY2:
    path = "rbp_py2"
    sys.path.insert(0,path)
    import mat
    import libfcnn
elif PY3:
    from rbp_py3 import mat
    from rbp_py3 import libfcnn


vc = cv2.VideoCapture("videos/neck-exercise.mp4")
scaler = 8

# Setting video writer for RBP 3 model B. This may be slight different for different devices.
vid_out = cv2.VideoWriter("results/result.mp4",0x00000021,30.0,(720,720),isColor=1)

# Create deque to store frames. 300 here is total frames of neck-exercise, because I know it.
fra_que = deque([],300)
while 1:
    ts = time.time()
    ret,frame = vc.read()
    if ret:
        resized_frame = cv2.resize(frame,(0,0),fx=0.125,fy=0.125)
        a = libfcnn.inference(mat.Mat.from_array(resized_frame),4)
        if a[2] != 0:
            xmin = a[0]*scaler
            ymin = a[1]*scaler
            xmax = (a[0]+a[2])*scaler
            ymax = (a[1]+a[2])*scaler
            cv2.rectangle(frame, (xmin,ymin), (xmax, ymax), (255,0, 0), 2)

        fps = "FPS: "+str(1/(time.time()-ts))[:5]
        cv2.putText(frame,fps,(0,60),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        fra_que.append(frame)

        # cv2.imshow("Frame",frame)
        # key = cv2.waitKey(1) & 0xFF
        # if key == ord("q"):
        #     break

    else:
        while len(fra_que):
            poped_fra = fra_que.popleft()
            vid_out.write(poped_fra)
        vid_out.release()
        break

