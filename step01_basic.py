#이미지 슬라이드쇼
import cv2
import matplotlib.pyplot as pyplot
import sys
import glob


img_files = glob.glob('imglist\\*.png')

print(img_files)

if not img_files:
    print("file 무")

    sys.exit()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cnt = len(img_files)
idx = 0

#존재하는 모든 이미지를 일정 시간 동안 자동으로 슬라이드 되게 개발

while True:

    img = cv2.imread(img_files[idx])

    if img is None:
        print("이미지 미존재")
        break

    cv2.imshow('image',img)

    if cv2.waitKey(1000) >= 0:
        break

    cv2.imshow('image',img)

    if cv2.waitKey(1000) >=0: #1초를 이상, 즉 esc를 클릭하지 않으면 false 반환, 지속적으로 반ㅁ복
        break

    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()
    # for i in range(cnt):
    #     img = cv2.imread(img_files[i])
    #     cv2.imshow('img',img)
    #     cv2.destroyAllWindows()