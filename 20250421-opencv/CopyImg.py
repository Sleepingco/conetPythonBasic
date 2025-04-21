import cv2
import matplotlib.pyplot as plt

img1 =  cv2.imread('HappyFish.jpg')
img2 = img1
img3 = img1.copy() # copy라 별도에 메모리에 있어서 영향을 안받음
print(id(img1),id(img2),id(img3))
img1.fill(255) 
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey()

plt.subplot(131)
plt.axis('off')
plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.axis('off')
plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.axis('off')
plt.imshow(cv2.cvtColor(img3,cv2.COLOR_BGR2RGB))

plt.show()

img1 =  cv2.imread('HappyFish.jpg')
img2 = img1[40:123,30:150]
img3 = img1[40:120,30:150].copy() # copy라 별도에 메모리에 있어서 영향을 안받음
img2.fill(0)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey()