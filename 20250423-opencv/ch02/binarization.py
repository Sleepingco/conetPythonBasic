# 영상의 이진화
import cv2
import numpy as np
src = cv2.imread('rice.png', cv2.IMREAD_GRAYSCALE)

th1, dst1 = cv2.threshold(src,0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#지역 이진화 4x4 = 16개 나누어서 이진화
dst2 = np.zeros(src.shape,np.uint8)

bw = src.shape[1] // 4 # 너비 width
bh = src.shape[0] // 4 # 높이 height

for y in range(4):
    for x in range(4):
        src_ = src[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        dst_ = dst2[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        cv2.threshold(src_,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU,dst_)
cv2.imshow('src',src)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.waitKey()