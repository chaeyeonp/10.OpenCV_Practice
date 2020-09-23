import numpy as np
import cv2

src = cv2.imread('imglist/cat.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('image 로딩 실패')
    sys.exit()

src = cv2.resize(src, (300,300))
dst = cv2.add(src, 100)

cv2.imshow('src',src)
cv2.imshow('dst',dst)

print("----컬러 영상 : RGB 고려 ----")
src = cv2.imread('imglist/cat.jpg')
src = cv2.resize(src,(300,300))


#BGR에 100씩 add, 밝기 조절
#add(,(4개의 값으로 구성된 튜플)
# dst = cv2.add(src,(100,100,100,0))

#clip 으로 연산 시 실수로 해야 정상 연산 후 부호정수 타입으로 변환해서 화면 출력
dst = np.clip(src+100, 0,255).astype((np.uint8))

cv2.imshow('src',src)
cv2.imshow('dst',dst)

src = cv2.imread('imglist/cat.jpg')
src = cv2.resize(src,(300,300))


cv2.waitKey()
cv2.destroyAllWindows()