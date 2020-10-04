#src_f = src_ycrcb[:,:,0] 이러한 문법이 이해가 되겠금
# 간단한 예제 구성
# numpy에 대한 test data 구성 -> 저문법으로 데이터 도출
import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

a = np.array([ [[1,2,3], [5,6,7]], [[11,21,31], [51,61,71]]])
print('a 출력')
print(a)
print('a shape')
print(a.shape)
print('b')
b = a[:, :]
print(b)


c = a[:, :, 0]
print('c')
print(c)