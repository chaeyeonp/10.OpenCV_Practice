import sys
import numpy as np
import cv2

# clip(): float 데이터 연산, 최대 ~ 최소 즉 값 한정 함수

src = cv2.imread('imglist/cat.bmp', cv2.IMREAD_GRAYSCALE)

print(src)
print(src.shape)
print(src.ndim)

if src is None:
    print('이미지 로딩 실패')
    sys.exit()

# 가우시안 블러링 후 샤프닝 필터링
blr = cv2.GaussianBlur(src,(0,0),2)

#clip() : float 데이터 연산, 최대 ~ 최소 즉 값 한정 함수

dst = np.clip(src * 2.0 -blr,0,255).astype(np.uint8)


cv2.imshow('src', src)
cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()