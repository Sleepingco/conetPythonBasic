import cv2
# cv2.VideoCapture(index=0,apiPreference=None) # retval  -> cv2.VideioCapture 객체
# cv2.VideoCapture.open(index=0,apiPreference=None)
# cv2.VideoCapture(filename="",apiPreference=None)
# cv2.VideoCapture.open(filename="",apiPreference=None)

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame =  cap.read()

#     inversed = ~frame

#     cv2.imshow('frame',frame)
#     cv2.imshow('inversed',inversed)

#     if cv2.waitKey(10) == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()

cap = cv2.VideoCapture('video1.mp4')
fps =  round(cap.get(cv2.CAP_PROP_FPS))
print('fps:',fps)
delay = round(1000/fps)
while True:
    ret, frame =  cap.read()
    if not ret:
        print("can't read video")
    inversed = ~frame

    cv2.imshow('frame',frame)
    cv2.imshow('inversed',inversed)

    if cv2.waitKey(delay) == 27:
        break
cap.release()
cv2.destroyAllWindows()