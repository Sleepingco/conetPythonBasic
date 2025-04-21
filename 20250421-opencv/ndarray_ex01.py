import cv2
import matplotlib.pyplot as plt
# OpenCV는 영상 데이터를 numpy.ndarray로 표현
img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

print("img ndim: {} , shape: {} , size: {}, dtype: {}".format(img1.ndim,img1.shape,img1.size,img1.dtype))
print("img ndim: {} , shape: {} , size: {}, dtype: {}".format(img2.ndim,img2.shape,img2.size,img2.dtype))
print('type(img1):', type(img1))
print('img1.shpate:',img1.shape)
print('img2.shape:',img2.shape)
print('img2.dtype:',img2.dtype)

h,w = img2.shape[:2] #(640, 480) h=640, w=480
print('img2 size:{} x {}'.format(w,h))

if len(img1.shape) == 2: # 흑백 사진은 가로 세로 값만 있으므로 len이 2개
    print('img1 is a grayscale image')
elif len(img1.shape) == 3: # 컬러 사진은 3개
    print('img1 is truecolor image')

for y in range(h): # for문으로 픽셀값을 변경하는 작업은 매우 느리므로, 픽셀값 참조 방법만 확인하고 실제로는 사용 금지
    for x in range(w):
        img1[y,x] = 255 # white
        img2[y,x] = [0,0,255] # BGR Color
# img1[:,:] = 255
# img2[:,:] = (0,0,255)

cv2.namedWindow('img1')
cv2.namedWindow('img2')
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.waitKey()
cv2.destroyAllWindows()
