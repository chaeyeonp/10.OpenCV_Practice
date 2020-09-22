import sys
import numpy as np
import cv2

'''
x,y 좌표, 마우스 왼쪽 클릭 감지, 클릭 해제도 감지
선 긋기 시에는 기존 x,y좌표 값을 지속적으로 인식
질문 : x,y 좌표 인식 시점은 어떤 action 취할 때 시작?
    마우스 왼쪽 버튼 클릭/해제
'''

#마우스 움직임에 따라 그림 그릴 수 있는 사용자 정의 함수
def on_mouse(event, x,y, flags, param):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        print(x,y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON :
            cv2.line(img,(oldx,oldy),(x,y),(0,0,255),5)
            cv2.imshow('image',img)
            oldx,oldy = x,y


#도화지
img = np.ones((480,670,3),dtype=np.uint8) * 255

#영상에 개별 이름 설정b
cv2.namedWindow('image')
cv2.setMouseCallback('image',on_mouse, img)
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()