import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2
src = cv2.imread('imglist/cat.bmp', cv2.IMREAD_GRAYSCALE)
#(3,3) 픽셀 이내의 RGB값 평균하여 평균값으로 채움
dst = cv2.blur(src,(3,3))
# 가우시안 필터링
# sigmaX & Y : x,y 방향의 편차값
dst2 = cv2.GaussianBlur(src,(0,0),10)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
cv2.imshow('src',src)
cv2.waitKey()
cv2.destroyAllWindows()