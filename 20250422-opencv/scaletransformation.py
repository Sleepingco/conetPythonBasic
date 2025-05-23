import sys
import numpy as np
import cv2


src = cv2.imread('rose.bmp') # src.shape=(320, 480)

if src is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (1920, 1280))  # cv2.INTER_LINEAR
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)
dst5 = cv2.flip(src,flipCode=-1,dst=None) # 좌우 상하 대칭 양수 = 좌우 0= 상하 대칭 -1 = 좌우 상하 대칭
cv2.imshow('dst5',dst5)
cv2.imshow('src', src)
cv2.imshow('dst1', dst1[500:900, 400:800])
affine = np.array([[4,0,0],[0,4,0]],dtype=np.float32)
dst2 = cv2.warpAffine(src,affine ,(480*4,320*4),borderMode=cv2.BORDER_REFLECT) # affine에서도 가능
cv2.imshow('dst2', dst2[500:900, 400:800])
cv2.imshow('dst3', dst3[500:900, 400:800])
cv2.imshow('dst4', dst4[500:900, 400:800])
cv2.waitKey()
cv2.destroyAllWindows()
