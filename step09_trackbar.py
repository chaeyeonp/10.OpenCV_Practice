import numpy as np
import cv2


def on_level_change(pos):
    print(pos)



img = np.zeros((480,640), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('level','image', 0,16,on_level_change)
cv2.imshow('image',img)

cv2.waitKey()
cv2.destroyAllWindows()