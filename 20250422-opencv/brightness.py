import cv2
import numpy as np

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
print(src.shape)
dst1 = cv2.add(src,100)
dst2 =src +100 # max를 넘어서 overflow가 발생해서 검은색이됨
# dst2 = np.clip(src+100.,0,255).astype(np.uint8)
cv2.imshow('orginal', src)
cv2.imshow('add',dst1)
cv2.imshow('plus 100',dst2)
cv2.waitKey()

