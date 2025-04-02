from ultralytics import YOLO

# 모델불러오기 
model = YOLO("yolo11m.pt") #사전 학습된 yolo11n모델

# 이미지 목록에 대해 배치 추론 실행
results = model(["cat.jpg" , "women.jpg"]) # result 객체의 리스트 반환

# 결과 리스트 처리
for result in results:
    boxes = result.boxes # 경계 상자 출력에 대한 boxes 객체
    masks =result.masks # 세분화 마스크 출력에 개한 masks 객체
    keypoints = result.keypoints # 분류에 대한 키포인트 객체
    probs = result.probs #분류 출력에 대한 프롭 객체
    obb = result.obb #  출력게 대한 obb 객체
    result.show() #화면에 표시
    result.save(filename="result.jpg") # 디스크에 저장