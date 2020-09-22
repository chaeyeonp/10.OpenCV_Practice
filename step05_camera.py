
import cv2
import matplotlib.pyplot as pyplot
import sys
import glob

cap = cv2.VideoCapture(0)

print(cap)

if cap.isOpened() == False:
    print("카메라 사용 불가")
    sys.exit()

while(True):
    ret, img_frame = cap.read()
    
    if ret == False:
        print("캡쳐 실패")

        break

    cv2.imshow('Color', img_frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()

cv2.destroyAllWindows()