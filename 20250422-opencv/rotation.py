import cv2
import math
import numpy as np

src = cv2.imread('tekapo.bmp')

rad = 20 * math.pi /180
aff = np.array([[math.cos(rad),math.sin(rad),0],
               [-math.sin(rad),math.cos(rad),0]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0,0))

cp = (src.shape[1]/2,src.shape[0]/2) # shape (h,w,3)
rot  = cv2.getRotationMatrix2D(cp,20,1) # 영상의 회전 변환 행렬 구하기
dst2 =  cv2.warpAffine(src,rot,(0,0))
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
cv2.waitKey()