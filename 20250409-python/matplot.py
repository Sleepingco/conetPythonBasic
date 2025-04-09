# %%
pip install matplotlib

# %%
import numpy as np
import matplotlib.pyplot as plt
def mandelbrot (h,w,maxit=20,r=2):
    """
        parameters:
        h(int) 이미지의 높이 픽셀단위
        h(int) 이미지의 너비 픽셀단위
        maxit(int) 각점에서 반복계산의 최대 횟수(defalut:20)

        return
        numpy.nbarray: mandelbort 프렉탈의 반복 횟수를 나타내는 2d배열
    """
    # 복소수 평면에서 y축과 x축의 좌표를 생성
    x = np.linspace(-2.6,1.5,4*h+1)
    y = np.linspace(-1.5,1.5,3*w+1)
    A, B = np.meshgrid(x,y)
    C = A+B*1j # 복소수 좌표생성
    z = np.zeros_like(C) # 초기z값은 c로 설정
    divtime = maxit + np.zeros(z.shape,dtype=int) # 각 점의 발산 시점을 저장할 배열

# mandelbort 집합계산
    for i in range(maxit):
        z = z**2 +C # z의 제곱에 c를 더함
        diverge = abs(z)>r # 발산 여부를 확인 (절댓값이 2를 초과하는 경우)
        div_now = diverge & (divtime == maxit) # 이번 반복에서 발산한점
        divtime[div_now] = i # 발산 시점을 기록
        z[diverge] = r# 발산한 점은 더이상 계산하지 않도록 설정
    return divtime # 발산시점 배열 변환
# mandelbort 프렉탈 시각화
# 400x400 크기의 이미지를 생성하고, 색상맵(cmap)을 hot로 설정
plt.imshow(mandelbrot(400,400),cmap='hot')
plt.colorbar() # 색상막대 추가
plt.title("Mandelbort Fractal")
# plt.clf()
plt.show()
# plt.imshow(mandelbrot(400,400))

# %%
import matplotlib.pyplot as plt
import numpy as np
a = np.linspace(0,1,20)
a = np.logspace(0.1,1,20)
print(a)
plt.plot(a,"o")
plt.show()

# %%
data = np.random.randn(10000)
plt.hist(data,bins=1000)
plt.show()

# %%
data = np.random.randint(-100,100,10000)
plt.hist(data,bins=10)
plt.show()

# %%
mean= 0
std = 1
a = np.random.normal(mean,std,(2,3))
print(a)
data = np.random.normal(0,1,10000)
plt.hist(data,bins=100)
plt.show()


