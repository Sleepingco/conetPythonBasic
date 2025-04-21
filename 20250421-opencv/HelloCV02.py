import cv2
import matplotlib.pyplot as plt

# # 컬러 영상 출력
# imgBGR =  cv2.imread('cat.bmp')
# imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) # opencv 는 BRG 로 불러오기 때문에 matplot을 사용하려면 RGB로 변환이 필요함

# plt.axis('off')
# plt.imshow(imgRGB)
# plt.show()

# # 그레이 스케일 영상 출력
# imgGray =  cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

# plt.axis('off')
# plt.imshow(imgGray, cmap= 'gray') # 그레이 스케일은 변환 작업은 필요 없지만 cmap을 꼭 써야함
# plt.show()

# 컬러 영상 출력
imgBGR =  cv2.imread('cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) # opencv 는 BRG 로 불러오기 때문에 matplot을 사용하려면 RGB로 변환이 필요함
imgGray =  cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('on'), plt.imshow(imgGray, cmap='gray')
plt.show()