import cv2
src = cv2.imread('airplane.bmp',cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane.bmp',cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('field.bmp',cv2.IMREAD_COLOR)
# size : 640:400 width x height
# dst[mask>0] = src[mask>0] 이런 방식도 가능하다 마스크가 0(검은색) 보다 크면
cv2.copyTo(src,mask,dst)
cv2.imshow('dst',dst)
cv2.waitKey()

# mask = logo[:,:,3] == alpha 값만 꺼낸다
# loog = logo[:,:,:-1] == bgr을 꺼낸다

import cv2
import sys
# 알파 채널을 마스크 영상으로 이용
src = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)
print(src.shape)
logo = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
if src is None or logo is None:
    print('Image load failed!')
    sys.exit()
mask = logo[:, :, 3] # mask는 알파 채널로 만든 마스크 영상, 투명도면 가져온다
logo2 = logo[:, :, :-1] # logo는 b, g, r 3채널로 구성된 컬러 영상, bgr a bgr
h, w = mask.shape[:2] # (h,w,4)bgra
crop = src[10:10+h, 10:10+w] # logo, mask와 같은 크기의 부분 영상 추출
cv2.copyTo(logo2, mask, crop)
cv2.imshow('src', src) # cat.bmp
cv2.imshow('logo', logo) # rgba 있는 opencv
cv2.imshow('mask', mask) # 알파값으로 만든 masks
cv2.waitKey()
cv2.destroyAllWindows()