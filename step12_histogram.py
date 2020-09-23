import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2


#step03 - 컬러 영상의 히스토그램 평활화
'''
입력 영상이 컬러인 경우 일반 형활화 작업시에 색이 연하지 않는 형태도 구성되기도 함
해결책
    YCrCb 형태로 변환해서 작업
    밝기 정보만 보유 따라서 밝기로만 분할 즉 색감은 유지된 상태로 명암비만 조절
    명암비(콘트리스트)
    히스토그램이 영상 전체 구간에서 균일한 분포로 나타나도록 변경작업이 명암비 조절
'''
src = cv2.imread('imglist/field.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
ycrcb_planes = cv2.split(src_ycrcb) #각 색상 즉 채널 분리

# 밝기 성분에 대해서만 히스토그램 평활화 수행
ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0])

dst_ycrcb = cv2.merge(ycrcb_planes)
dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

# step02 - 그레이스케일 영상의 히스토그램 평활화
# src = cv2.imread('imglist/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

# if src is None:
#     print('Image load failed!')
#     sys.exit()

# dst = cv2.equalizeHist(src)

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()

# cv2.destroyAllWindows()



#step01 - 단순 그래프 확인
# 그레이스케일 영상의 히스토그램
# src = cv2.imread('imglist/lenna.bmp', cv2.IMREAD_GRAYSCALE)

# if src is None:
#     print('Image load failed!')
#     sys.exit()

# hist = cv2.calcHist([src], [0], None, [256], [0, 256])

# cv2.imshow('src', src)
# cv2.waitKey(1)

# plt.plot(hist)
# plt.show()

# # 컬러 영상의 히스토그램
# src = cv2.imread('imglist/lenna.bmp')

# if src is None:
#     print('Image load failed!')
#     sys.exit()

# colors = ['b', 'g', 'r']
# bgr_planes = cv2.split(src)

# for (p, c) in zip(bgr_planes, colors):
#     hist = cv2.calcHist([p], [0], None, [256], [0, 256])
#     plt.plot(hist, color=c)

# cv2.imshow('src', src)
# cv2.waitKey(1)

# plt.show()

# cv2.destroyAllWindows()
