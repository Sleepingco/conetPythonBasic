import cv2
import numpy as np

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

src_f = src.astype(np.float32)
blr = cv2.GaussianBlur(src_f, (0,0),2.0)
dst = np.clip(2. * src_f - blr,0, 255).astype(np.uint8)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()