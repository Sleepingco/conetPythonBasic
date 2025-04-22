import cv2
import numpy as np

src = cv2.imread('tekapo.bmp')
aff = np.array([[1,0,200], # x축 200 이동
               [0,1,100]],dtype=np.float32) # y축 100 이동

dst = cv2.warpAffine(src,aff,(0,0))

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()

# x' = 1x +0.5y + 0
# y' = 0x + 1y + 0
# [[1,0.5,0],[0,1,0]]
aff = np.array([[1,0.5,0],
               [0,1,0]],dtype=np.float32)
(h,w) = src.shape[:2] # (w, h, 3)
dst = cv2.warpAffine(src,aff,(w+int(h*0.5),h))
cv2.imshow('dst',dst)
cv2.waitKey()