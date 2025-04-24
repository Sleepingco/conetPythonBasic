import sys
import numpy as np
import cv2

# 캠시프트(CamShift)란?
# Continuously Adaptive Mean Shift
# 추적하는 객체의 크기가 변하더라도 검색 윈도우의 크기가 고정되어 있는
# 평균 이동 알고리즘의 단점을 보완
# ■ 캠시프트 동작 방법
# 우선 평균 이동 알고리즘으로 이동 위치 계산
# 윈도우 크기를 조정
# 특징 공간을 가장 잘 표현하는 타원 검출
# 새로운 크기의 윈도우를 이용하여 다시 평균 이동 수행

# 비디오 파일 열기
cap = cv2.VideoCapture('camshift.avi')

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

# 초기 사각형 영역: (x, y, w, h)
x, y, w, h = 135, 220, 100, 100
rc = (x, y, w, h)

ret, frame = cap.read()

if not ret:
    print('frame read failed!')
    sys.exit()

roi = frame[y:y+h, x:x+w]
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# HS 히스토그램 계산
channels = [0, 1]
ranges = [0, 180, 0, 256]
hist = cv2.calcHist([roi_hsv], channels, None, [90, 128], ranges)

# CamShift 알고리즘 종료 기준
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

# 비디오 매 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # HS 히스토그램에 대한 역투영
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    backproj = cv2.calcBackProject([frame_hsv], channels, hist, ranges, 1)

    # CamShift
    ret, rc = cv2.CamShift(backproj, rc, term_crit)

    # 추적 결과 화면 출력
    cv2.rectangle(frame, rc, (0, 0, 255), 2)
    cv2.ellipse(frame, ret, (0, 255, 0), 2)
    cv2.imshow('frame', frame)

    if cv2.waitKey(60) == 27:
        break

cap.release()
cv2.destroyAllWindows()
