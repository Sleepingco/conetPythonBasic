# 히스토그램
# 영상의 픽셀 값 분포를 그래프의 형태로 표현한 것
# 예를 들어 그레이스케일 영상에서 각 그레이 스케일 값에 해당하는 픽셀의 개수를 구하고 이를 막대 그래프의 형태로 표현
# 정규화된 히스토그램
# 각 픽셀의 개수를 영상젠체 픽셀 개수로 나누어 준것
# 해당 그레이스케일 값을 갖는 픽셀이 나타랄 확률

import cv2
import matplotlib.pyplot as plt
# src =  cv2.imread('lenna.bmp',cv2.IMREAD_GRAYSCALE)

# hist = cv2. calcHist([src],[0],None,[256],[0,256])
# # calcHist([images:입력 영상 리스트,channels:히스토그램을 구할 채널을 나타내는 리스트,mask:마스크 영상 영상전체에서 히스토그램을 구하려면 None지정,histSize:히스토그램 각 차원의 크리(빈(bin)의 개수)를 나타내는 리스트,ranges:히스토그램 각 차원의 최솟값과 최댓값으로 구성된 리스트,hist:계산된 히스트그램(numpy.ndarray),accumulate:기존의 hist히스토그램에 누적하려면 True, 새로 만들려면 False)
# plt.plot(hist)
# plt.show()

src =  cv2.imread('lenna.bmp')
b = src[:, :, 0]
print(b.shape)      # (height, width)
print(b[100, 200])  # src[100, 200][0] 와 같음 (blue 값)

colors = ['b','g','r']
bgr_planes = cv2.split(src)
print(bgr_planes)
for (p,c) in zip(bgr_planes,colors):
    hist = cv2.calcHist([p],[0],None,[256],[0,256])
    plt.plot(hist, color=c)
plt.show()