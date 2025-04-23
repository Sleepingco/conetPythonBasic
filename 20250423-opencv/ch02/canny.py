import cv2

src = cv2.imread('building.jpg',cv2.IMREAD_GRAYSCALE)

dst = cv2.Canny(src,50,150) # 입력영상, 하단임계값, 상단임계값

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()