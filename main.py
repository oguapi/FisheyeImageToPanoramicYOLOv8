import os

import cv2
from ultralytics import YOLO
import math
import numpy as np
#from cv_bridge import CvBridge #CvBridge is required to convert raw's messages to an open cv image


#photo_path= os.path.join('.','data','fisheyePhoto.jpg')
#photo_out_path= os.path.join('.','out.png')
photo_path= os.path.join('.','data','fisheyePhoto.jpg')
photo_out_path= os.path.join('.','out2.png')

imgfisheye= cv2.imread(photo_path)
size= imgfisheye.shape #(raw,column,3)
print(size)
cv2.imshow('Fisheye Photo', imgfisheye)
cv2.waitKey(0)
cv2.destroyAllWindows()

model= YOLO('yolov8n.pt') #Pre-trained model to Detection 'https://github.com/ultralytics/ultralytics/tree/main/ultralytics/models'

#the dimension of the data is width 600 and height 600, for second image
#we select the largest dimension por the radio
width = 353 #280 #Radio de barrido
Panorama= np.zeros((width, 4*width, 3), np.uint8)
for i in range(width):
    for j in range(4*width):
        radius= width - i
        theta= 2*math.pi*(j)/(4*width)

        x= int(size[0]/2) - int(round(radius * math.cos(theta)))
        y= int(size[1]/2) - int(round(radius * math.sin(theta)))

        if(x >= 0 and x< 2*width and y >= 0 and y < 2*width):
            if(x< size[0] and y< size[1]):
                Panorama[i][j]= imgfisheye[x][y]
            else:
                Panorama[i][j]= (0,0,0)

Panorama= cv2.flip(Panorama,0) #Use flip because the current image is upside down
cv2.imwrite(photo_out_path, Panorama) #Save the panoramic image
cv2.imshow('Panorama', Panorama)
cv2.waitKey(0)
cv2.destroyAllWindows()

results= model(Panorama)

for result in results:
    detections= []
    for r in result.boxes.data.tolist():
        print(r) #Show the detections