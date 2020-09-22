#영상의 생성, 복사, 부분 영상 추출의 사전 학습

import cv2
import matplotlib.pyplot as pyplot
import sys
import glob

img1 = cv2.imread('imglist/hsv.png')

img2 = img1 #img1과 img2 는 동일한 이미지객체 참조

img3 = img1.copy() #새로운 객체 생성

img3 = img1.copy()

img1.fill(255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey()
cv2.destroyAllWindows()