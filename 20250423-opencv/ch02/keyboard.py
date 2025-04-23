import cv2

src = cv2.imread('keyboard.bmp',cv2.IMREAD_GRAYSCALE)

th, src_bin = cv2.threshold(src,0,255, cv2.THRESH_OTSU) # threshhold값이 첫번째 리턴
print(th)
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for i in range(1,cnt):
    (x,y,w,h,area) = stats[i]
    print(area)
    if area < 20:
        continue
    cv2.rectangle(dst, (x,y,w,h), (0,255,255))

cv2.imshow('src',src)
cv2.imshow('src_bin',src_bin)
cv2.imshow('dst',dst)
cv2.waitKey()