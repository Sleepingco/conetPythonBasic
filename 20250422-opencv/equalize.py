import cv2
src = cv2.imread('field.bmp')
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# 0: Y, 1: Cr, 0: Cb, height, weight, y crcb
src_ycrcb[:,:,0] = cv2.equalizeHist(src_ycrcb[:,:,0])
dst = cv2.cvtColor(src_ycrcb,cv2.COLOR_YCrCb2BGR)

cv2.imshow('src',src)
cv2.imshow('dst', dst)
cv2.waitKey()