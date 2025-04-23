import sys
import numpy as np
import cv2


# 입력 영상 불러오기
src = cv2.imread('nemo.jpg') # (w,h,3)

if src is None:
    print('Image load failed!')
    sys.exit()

# 사각형 지정을 통한 초기 분할
rc = cv2.selectROI(src)
mask = np.zeros(src.shape[:2], np.uint8) # 너비와 높이만 가지고 마스크를 만듬

cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)

# 0: cv2.GC_BGD, 2: cv2.GC_PR_BGD
mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8') # 0,2번만 백그라운드 이기때문에 배경은 날리고 포그라운드는 살리는 방법 
# mask 2 shape(w,h) 2개이기 때문에 newaxis로 차원을 늘림?
dst = src * mask2[:, :, np.newaxis]

# 초기 분할 결과 출력

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
