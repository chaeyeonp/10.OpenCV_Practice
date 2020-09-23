import sys
import numpy as np
import cv2

#np.clip(배열,최소값, 최대값)
def on_level_change(pos):
    print(img.shape,img.ndim)
    print(pos)
    # value = 255/16 * pos
    value = pos * 16
    img[:, :] = np.clip(value,0,255) #최소 0~최대 255, 포화연산
    cv2.imshow('image',img)


img = np.zeros((500,640),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('level','image', 0, 16, on_level_change)
cv2.imshow('image',img)


'''
x,y 좌표, 마우스 왼쪽 클릭 감지, 클릭 해제도 감지
선 긋기 시에는 기존 x,y좌표 값을 지속적으로 인식
질문 : x,y 좌표 인식 시점은 어떤 action 취할 때 시작?
    마우스 왼쪽 버튼 클릭/해제
'''

oldx = oldy = -1

#마우스 움직임에 따라 그림 그릴 수 있는 사용자 정의 함수
#마우스를 클릭 상태에서 x,y 좌표가 두 번 변경된다는 건 두 번 이 함수 호출
#두 번째 클릭시에 x,y 좌표는 첫 번째 클릭한 x,y 좌표 값 공유 - 전역으로 선언 및 공유
# global  - 함수 내부에서 이미 선언된 일반 변수를 전역 변수화 하고자 할 때 사용

def on_mouse(event, x,y, flags, param):
    global oldx, oldy #공유하는 전역변수 활용 문법

    #마우스 왼쪽 버튼 클릭 시점인 시작점의 x,y 좌표값 대입 필수
    if event == cv2.EVENT_LBUTTONDOWN: #마우스 왼쪽 버튼이 눌러지는 것 감지
        '''
        마음대로 그리기
        oldx, oldy = x,y
        '''

        #직선으로 그리기
        print(x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        print(x,y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON : #마우스 왼쪽 버튼이 눌러지는 것 감지(ing)
            # cv2.line(img, start, end, color, thickness)
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