import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

alpha = 1.0
dst = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

# opencv의 함수를 이용해 더 간단히 구현 가능
import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

src = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

gmin, gmax, _, _ = cv2.minMaxLoc(src)
dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX) # 정규화
#dst = ((src - gmin) * 255. / (gmax - gmin)).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('normalize', dst)
dst2 = cv2.equalizeHist(src) # 평활화
cv2.imshow('eqaulize', dst2)
cv2.waitKey()
srcHist = cv2.calcHist([src],[0],None,[256],[0,256])
dstHist = cv2.calcHist([dst],[0],None,[256],[0,256])
# plt.subplot(121)
# plt.plot(srcHist)
# plt.subplot(122)
# plt.plot(dstHist)
# plt.show()
plt.plot(srcHist, 'r', label=src); 
plt.plot(dstHist, 'b', label='dst'); 
plt.legend(); 
plt.show()
cv2.destroyAllWindows()


