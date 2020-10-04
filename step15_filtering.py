import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2
src = cv2.imread('imglist/cat.jpg')
if src is None:
    print('이미지 로딩 실패')
    sys.exit()

print(src)
print('------')

#[색상의 밝기 정보, x좌표, y좌표]
src_ycrcb = cv2.cvtColor(src,cv2.COLOR_BGR2YCrCb)

src_f = src_ycrcb[:,:,0] #차원의 데이터 중 0번째 해당하는 색상 밝기 값만 변환
blr = cv2.GaussianBlur(src_f,(0,0),2.0)
dst = np.clip(src_f * 2.0 - blr, 0 ,255).astype(np.uint8)

#?
src_ycrcb[:,:,0]

print(src_f)



src = cv2.resize(src,(480,640))
# 밝기 정보, x , y로 이루어진 배열 YCRCB
src_ycr = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
cv2.imshow('src_ycr',src_ycr[:,:,0])
cv2.waitKey()
cv2.destroyAllWindows()
