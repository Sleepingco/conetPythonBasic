import sys
import numpy as np
import cv2

cap = cv2.VideoCapture("vtest.avi")

if not cap.isOpened():
    print('Camera open failed!')
    sys.exit()

ret, frame1 = cap.read()

if not ret:
    print('frame read failed!')
    sys.exit()

gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

# frame.shape(199,800,3)
hsv = np.zeros_like(frame1) #(600,800,3)
hsv[..., 1] = 255 # 
# hsv[:,:,1] == hsv[..., 1] 맨뒤에 원소지정
while True:
    ret, frame2 = cap.read()

    if not ret:
        print('frame read failed!')
        sys.exit()

    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(gray1, gray2, None, 0.5, 3, 13, 3, 5, 1.1, 0) # (출력) 계산된 옵티컬플로우. np.ndarray. shape=(h, w, 2), dtype=np.float32.

    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1]) # 극 좌표계로 바꾼다 x,y == mag,ang
    hsv[..., 0] = ang*180/np.pi/2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow('frame', frame2)
    cv2.imshow('flow', bgr)
    if cv2.waitKey(20) == 27:
        break

    gray1 = gray2

cv2.destroyAllWindows()
