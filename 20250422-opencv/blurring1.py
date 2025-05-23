import cv2
import numpy as np
src = cv2.imread('rose.bmp',cv2.IMREAD_GRAYSCALE)

kernal = np.array([[1/9,1/9,1/9],
                   [1/9,1/9,1/9],
                   [1/9,1/9,1/9]])
dst = cv2.filter2D(src,-1,kernal)

cv2.imshow('dst',dst)
cv2.waitKey()

cv2.imshow('src',src)

for ksize in (3,5,7):
    dst = cv2.blur(src,(ksize,ksize))

    desc = 'Mean: {}x{}'.format(ksize,ksize)
    cv2.putText(dst,desc,(10,30),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                1.0,255,1,cv2.LINE_AA)
    
    cv2.imshow('dst',dst)
    cv2.waitKey()
cv2.destroyAllWindows()