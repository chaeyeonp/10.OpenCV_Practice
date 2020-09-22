import cv2
import matplotlib.pyplot as pyplot
import sys
import glob

#영상 불러오기, 
img1 = cv2.imread('imglist/cat.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('imglist/cat.jpg', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print("이미지 미 존재")

    sys.exit()


print(type(img1))
print(type(img2))


print('--------------')
print(img1)

print('--------------')
print(img1.shape, img1.ndim)
print(img2.shape, img2.ndim)


#영상 크기만 출력(h,w)
print(img2.shape[:2]) #(2470, 1853)