import numpy as np
import cv2
import matplotlib.pyplot as plt

np1 = np.empty((2,2),np.uint8)
print(np1)
np2 = np.zeros((2,2),np.uint8)
print(np2)
np3 = np.ones((2,2),np.uint8)
print(np3)
np4 = np.full((2,2),255,np.uint8)
print(np4)

img1 = np.empty((480,640),dtype=np.uint8)
img2 = np.zeros((480,640,3),dtype=np.uint8)
img3 = np.ones((480,640),dtype=np.uint8) * 255
img4 = np.full((480,640,3),(0,255,255),dtype=np.uint8)

cv2.namedWindow('image1')
cv2.imshow('image1',img1)
cv2.namedWindow('image2')
cv2.imshow('image2',img2)
cv2.namedWindow('image3')
cv2.imshow('image3',img3)
cv2.namedWindow('image4')
cv2.imshow('image4',img4)
cv2.waitKey() == 13
cv2.destroyAllWindows()