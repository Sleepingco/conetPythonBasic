import cv2
import numpy as np

src = cv2.imread('namecard.jpg')

w,h =  720, 400

srcQuad = np.array([
    [222,95],[622,178],
    [547,416],[145,317]
    ],np.float32)
dstQuad = np.array([[0,0],[w-1,0],[w-1,h-1],[0,h-1]],np.float32)

pers = cv2.getPerspectiveTransform(srcQuad,dstQuad)
dst = cv2.warpPerspective(src,pers,(w,h))

cv2.imshow('dst',dst)
cv2.waitKey()