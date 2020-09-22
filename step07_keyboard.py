# 마우스를 이용한 그리기
#

import cv2
import matplotlib.pyplot as pyplot
import sys
import glob

#i or I를 입력시에 이미지가 반전
# ~틸트: 반전 연산자

img = cv2.imread('imglist/cat.bmp',cv2.IMREAD_GRAYSCALE)

if img is None:
    print('image 로딩 실패')
    sys.exit()

cv2.imshow('image',img)

while True:
    keycode = cv2.waitKey()
    if keycode == ord('i') or keycode == ord('I'):
        img = ~img
        cv2.imshow('image',img)


    elif keycode == 27:
        break


cv2.destroyAllWindows()
