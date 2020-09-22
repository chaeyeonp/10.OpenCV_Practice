import cv2
import matplotlib.pyplot as pyplot
import sys
import glob

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("카메라 사용 불가")
    sys.exit()


ret, img_frame = cap.read()

if ret==False:
    print("캡쳐 실패")
    exit(1)
    
#코덱 - 데이터 스트림 또는 신호에 대해 인코딩 또는 디코딩 혹은 둘 다 다룰 수 있는
#적용 가능한 코덱 DIVX, XVID, MJPG, ...
#동영상 파일을 위한 코덱 설정

#cv2.VideoWriter_fourcc(*'MJPG')
codec = cv2.VideoWriter_fourcc('M','J','P','G')

#프레임 레이터 디스플레이 장치가 화면 하나에 데이터를 표시하는 속도

fps = 30.0
h,w = img_frame.shape[:2]

writer = cv2.VideoWriter('playdata.avi', codec, fps, (w, h))

if writer.isOpened() == False:
    print("동영상 파일 준비 불가")
    exit(1)

while True:
    ret, img_frame = cap.read()
    if ret == False:
        print('영상 read 실패')
        break

    writer.write(img_frame)
    cv2.imshow('Color',img_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

# 자원 해제

cap.release()
writer.release()
cv2.destroyAllWindows()