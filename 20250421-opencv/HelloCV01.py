import sys
import cv2

print('Hello OpenCV',cv2.__version__)

img = cv2.imread('cat.bmp')
if img is None:
    print("Image load failed!")
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image',img)
while True:
    if cv2.waitKey() == 13:
        break

cv2.destroyAllWindows()

