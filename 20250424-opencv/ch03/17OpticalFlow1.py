# 옵티컬플로우(Optical flow)란?
# 연속하는 두 프레임(영상)에서 카메라 또는 객체의 움직임에 의해 나타나는 객체의 이동
# 정보 패턴

# OpenCV 옵티컬플로우 계산 함수
# 루카스-카나데 알고리즘(Lucas-Kanade algorithm)
# cv2.calcOpticalFlowPyrLK(...)
# (주로) Sparse points에 대한 이동 벡터 계산 (꽉차있지 않고 중간중간 비어있는 영상)
# → 특정 픽셀에서 옵티컬플로우 벡터 계산
# 파네백 알고리즘(Farneback's algorithm)
# cv2.calcOpticalFlowFarneback(...)
# Dense points에 대한 이동 벡터 계산 (꽉찬 비어있지 않은 영상)
# → 모든 픽셀에서 옵티컬플로우 벡터 계산

# 현재 특징점으로 이동했을때 나타나는 특징을 구해줌

import sys
import numpy as np
import cv2


src1 = cv2.imread('frame1.jpg')
src2 = cv2.imread('frame2.jpg')

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

gray1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)

pt1 = cv2.goodFeaturesToTrack(gray1, 50, 0.01, 10) # 특징점을 구함 맥스커노,퀄리티 레벨, 최소거리
pt2, status, err = cv2.calcOpticalFlowPyrLK(src1, src2, pt1, None) # 소스1,소스2,구한특징점

dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0) # 0.5,0.5로 합성ㄴ

for i in range(pt2.shape[0]):
    if status[i, 0] == 0:
        continue

    cv2.circle(dst, tuple(pt1[i, 0].astype(int)), 4, (0, 255, 255), 2, cv2.LINE_AA) # 이전영상에 대한 원
    cv2.circle(dst, tuple(pt2[i, 0].astype(int)), 4, (0, 0, 255), 2, cv2.LINE_AA) # 다음 영상에 대한원
    cv2.arrowedLine(dst, tuple(pt1[i, 0].astype(int)), tuple(pt2[i, 0].astype(int)), (0, 255, 0), 2) # 이전 영상에서 다음까지 선을 그어줌

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
