import sys
import numpy as np
import cv2

#마우스 움직임에 따라 그림 그릴 수 있는 사용자 정의 함수
def on_mouse(event, x,y, flags, param):
    print(x,y,flags)


#도화지
img = np.ones((480,670,3),dtype=np.uint8) * 255

#영상에 개별 이름 설정
cv2.namedWindow('image')
cv2.setMouseCallback('image',on_mouse, img)
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()