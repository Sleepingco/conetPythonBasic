import cv2
src= cv2.imread('lenna.bmp')
print(src.shape)

bgr =  cv2.split(src)
print(bgr)
dst1 = cv2.GaussianBlur(src,(0,0),5)
dst2 = cv2.bilateralFilter(src,-1,10,5)

cv2.imshow('src',src)
cv2.imshow('Gaussian',dst1)
cv2.imshow('bilateral',dst2)
cv2.waitKey()