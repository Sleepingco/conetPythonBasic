import sys
import numpy as np
import cv2

# 두 개의 동영상을 열어서 cap1, cap2로 지정
cap1 = cv2.VideoCapture('video1.mp4')  # 첫 번째 비디오 파일 열기
cap2 = cv2.VideoCapture('video2.mp4')  # 두 번째 비디오 파일 열기

# 비디오 파일 열기에 실패했는지 확인
if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed!')  # 열기에 실패한 경우 오류 메시지 출력
    sys.exit()  # 프로그램 종료

# 첫 번째, 두 번째 비디오의 총 프레임 수 가져오기
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))  # video1 전체 프레임 수
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))  # video2 전체 프레임 수
fps = cap1.get(cv2.CAP_PROP_FPS)  # video1의 FPS (video2도 같다고 가정)

# 전환 효과를 줄 프레임 수 (2초 동안 전환 효과 적용)
effect_frames = int(fps * 2)

# 디버깅용으로 정보 출력
print('frame_cnt1:', frame_cnt1)  # video1 프레임 수 출력
print('frame_cnt2:', frame_cnt2)  # video2 프레임 수 출력
print('FPS:', fps)  # FPS 출력

# waitKey용 딜레이 (ms 단위)
delay = int(1000 / fps)  # 프레임 간 시간 계산

# 비디오 해상도 가져오기
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))   # 프레임 너비
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 프레임 높이

# 저장할 비디오의 코덱 설정 (DIVX 사용)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # 코덱 설정

# 출력 비디오 객체 생성 ('output.avi'로 저장)
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

# -------------------------
# 1. video1 대부분을 그대로 복사
# -------------------------
for i in range(frame_cnt1 - effect_frames):  # 전환 구간 전까지 반복
    ret1, frame1 = cap1.read()  # video1에서 프레임 읽기

    if not ret1:  # 읽기 실패 시
        print('frame read error!')
        sys.exit()

    out.write(frame1)  # 프레임을 출력 비디오에 저장
    print('.', end='')  # 진행상태 출력

    cv2.imshow('output', frame1)  # 현재 프레임 화면에 표시
    cv2.waitKey(delay)  # 프레임 사이 딜레이

# -------------------------
# 2. 슬라이딩 전환 효과 구간
# -------------------------
for i in range(effect_frames):  # 전환 프레임 수만큼 반복
    ret1, frame1 = cap1.read()  # video1에서 프레임 읽기
    ret2, frame2 = cap2.read()  # video2에서 프레임 읽기

    if not ret1 or not ret2:  # 둘 중 하나라도 읽기 실패 시
        print('frame read error!')
        sys.exit()

    # 전환 효과를 위한 경계 위치 계산
    dx = int(w / effect_frames) * i  # 점점 넓어지게 계산

    # 새 프레임을 0으로 초기화 (검은 배경)
    frame = np.zeros((h, w, 3), dtype=np.uint8)

    # 왼쪽부터 dx까지는 video2의 프레임 복사
    frame[:, 0:dx, :] = frame2[:, 0:dx, :]

    # 나머지 오른쪽은 video1의 프레임 복사
    frame[:, dx:w, :] = frame1[:, dx:w, :]

    # (참고) 페이드 효과를 넣고 싶다면 아래 코드 사용 가능
    # alpha = i / effect_frames
    # frame = cv2.addWeighted(frame1, 1 - alpha, frame2, alpha, 0)

    out.write(frame)  # 합성된 프레임 저장
    print('.', end='')  # 진행상태 출력

    cv2.imshow('output', frame)  # 화면에 표시
    cv2.waitKey(delay)  # 프레임 간 딜레이

# -------------------------
# 3. video2 나머지 복사
# -------------------------
for i in range(effect_frames, frame_cnt2):  # video2 나머지 프레임 복사
    ret2, frame2 = cap2.read()  # video2에서 프레임 읽기

    if not ret2:
        print('frame read error!')  # 오류 발생 시 메시지 출력
        sys.exit()

    out.write(frame2)  # 프레임 저장
    print('.', end='')  # 진행상태 출력

    cv2.imshow('output', frame2)  # 화면에 표시
    cv2.waitKey(delay)  # 프레임 간 딜레이

# 완료 메시지 출력
print('\noutput.avi file is successfully generated!')

# 비디오 장치 및 창 해제/닫기
cap1.release()  # video1 닫기
cap2.release()  # video2 닫기
out.release()   # 출력 비디오 저장 마무리
cv2.destroyAllWindows()  # 모든 창 닫기
