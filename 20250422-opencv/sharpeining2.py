import cv2
import numpy as np

src = cv2.imread('rose.bmp')
src_ycrcb = cv2.cvtColor(src,cv2.COLOR_BGR2YCrCb)
src_f = src_ycrcb[:,:,0].astype(np.float32)

blr = cv2.GaussianBlur(src_f,(0,0),2.0)
src_ycrcb[:,:,0] = np.clip(2. * src_f - blr,0, 255).astype(np.uint8)

dst = cv2.cvtColor(src_ycrcb ,cv2.COLOR_YCrCb2BGR)

src_ycrcb2 = cv2.cvtColor(src,cv2.COLOR_BGR2YCrCb)
src_ycrcb2[:,:,0] = cv2.equalizeHist(src_ycrcb[:,:,0])
dst2 = cv2.cvtColor(src_ycrcb,cv2.COLOR_YCrCb2BGR)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
cv2.waitKey()