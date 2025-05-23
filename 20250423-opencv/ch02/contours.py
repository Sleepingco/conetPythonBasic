import cv2
import random
import numpy as np
src = cv2.imread('contours.bmp',cv2.IMREAD_GRAYSCALE)

# contours, hier = cv2.findContours(src,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# contours, hier = cv2.findContours(src,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours, hier = cv2.findContours(src,cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# contours, hier = cv2.findContours(src,cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

idx = 0
while idx >= 0:
    c = (random.randint(0,255),
         random.randint(0,255),
         random.randint(0, 255))
    cv2.drawContours(dst,contours,idx,c,2,cv2.LINE_8,hier)
    idx = hier[0, idx, 0]
cv2.imshow('dst',dst)
cv2.waitKey()


