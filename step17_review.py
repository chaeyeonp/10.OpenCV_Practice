import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2
def onMouse(x) :
    pass
cv2.namedWindow('Blur')
img = cv2.imread('imglist/1/1.jpg')
img = cv2.resize(img, (480,640))
cv2.createTrackbar('Blur_M','Blur',0, 2 , onMouse)
cv2.createTrackbar('Blur_L','Blur',0, 5, onMouse)
cv2.setTrackbarPos('Blur_M', 'Blur', 0)
cv2.setTrackbarPos('Blur_L', 'Blur', 0)
while True :
    blur_mode = cv2.getTrackbarPos('Blur_M','Blur')
    blur_level = cv2.getTrackbarPos('Blur_L','Blur')
    blur_level = blur_level * 2 + 1
    if blur_mode == 0 :
        blur = cv2.blur(img, (blur_level,blur_level))
        cv2.imshow('Blur',blur)
    elif blur_mode == 1 :
        blur = cv2.GaussianBlur(img, (blur_level,blur_level),0)
        cv2.imshow('Blur',blur)
    else :
        blur = cv2.medianBlur(img, blur_level)
        cv2.imshow('Blur',blur)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()