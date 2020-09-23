import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
'''
x,y 좌표, 마우스 왼쪽 클릭 감지, 클릭 해제도 감지
선 긋기시에는 기존 x,y 좌표값을 지속적으로 인식
질문 : x,y 좌표 인식 시점은 어떤 action 취할때 시작?
    마우스 왼쪽 버튼 클릭/해제   
'''
# 마우스 움직임에 따라 그림 그릴 수 있는 사용자 정의 함수
# 마우스 왼쪽 버튼 클릭 시점인 시작점의 x,y 좌표값 대입 필수
# 마우스를 클릭상태에서 x,y 좌표가 두번 변경된다는건 두번 이 함수 호출
# 두번째 클릭시 x,y 좌표는 첫번째 클릭한 x,y 좌표값 공유 - 전역으로 선언 및 공유
# global 함수 내부에서 이미 선언된 일반 변수를 전역 변수화 하고자 할때 사용
def on_mouse(event, x, y, flags, param):
    global oldx, oldy # 공유하는 전역변수
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        print(x,y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx,oldy), (x,y), (0,0,255), 5)
            cv2.line(img, (oldx,oldy), (x-20,y-20), (136,133,164), 2)
            cv2.line(img, (oldx,oldy), (x+20,y+20), (245,209,183), 2)
            cv2.imshow('image', img)
            oldx, oldy = x, y
# 도화지 : RGB값을 인식 할 수 있는 원색 배경
img = np.ones((480,670,3), dtype = np.uint8) * 255
#img = cv2.imread('jungho.jpg')
img = cv2.resize(img,(700,700))

while True:
# 영상에 개별 이름 설정
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', on_mouse, img)
    cv2.imshow('image', img)
    keyCode = cv2.waitKey()
    if keyCode == ord('i') or keyCode == ord('I'):
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    elif keyCode == 27:
        break

cv2.destroyAllWindows()