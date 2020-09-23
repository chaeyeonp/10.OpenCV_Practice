import numpy as np
import cv2

#np.clip(배열,최소값, 최대값)
def on_level_change(pos):
    print(img.shape,img.ndim)
    # value = 255/16 * pos
    value = pos * 16
    img[:, :] = np.clip(value,0,255) #최소 0~최대 255, 포화연산
    cv2.imshow('image',img)


img = np.zeros((500,640),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('level','image', 0, 16, on_level_change)
cv2.imshow('image',img)


def on_level_change(pos):
    print(pos)



img = np.zeros((480,640), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('level','image', 0,16,on_level_change)
cv2.imshow('image',img)

cv2.waitKey()
cv2.destroyAllWindows()