# %%
import numpy as np
# 넘파이는 왜 성공했나
# 배열 프로그래밍 기능 덕분에 ai에서 인기를 누림
a = np.arange(15).reshape(3,5)
print(a)
print(a.shape) # 형태확인
print(a.dtype.name) #자료형 확인
print(a.itemsize)
print(a.size) #크기 확인

b = np.array([6,7,8])
# b = np.array[6,7,8] 소괄호 없으면 에러남
print(b)

c = np.array([1,'two',3,4]) # 자료형 섞어서도 가능
print(c)

a = np.array([1.21,3.4,5.1]) # 다양한형태의 원소 가능
print(a.dtype)

# 리스트는 크기가 가변적이고 어떤 원소 타임도 저장할 수 있음 대신 연산시 메모리를 많이 사용함
# 배열은 같은 타입의 원소만 저장함, 메모리를 훨씬 적게 씀
a=[2,4,5]
aa=np.array(a)
print(a[1])
print(aa[1])

# %%
import numpy as np

arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])
arr[5:8] =12
print(arr)

# %%
import numpy as np

arr_slice = arr[5:8]
arr_slice
arr_slice[1] = 12345
arr_slice
# arr_slice[:] =64 # 처음 부터 끝까지
arr_slice[:] =64 # 처음 부터 끝까지 5에서 7인덱스까지
arr

# %%
arr_slice_copy = arr[5:8].copy() # 하드 copy
arr_slice_copy
arr
arr_slice_copy[:] = 8 # 배열 슬라이스에서 기억해야하는 부분 [시작:끝]
arr_slice_copy
print(arr)

# %%
# 튜플
# zeros(), ones(), arange(), eye()
a2 = np.zeros(3) # 배열의 초기화 가능 이미지처리에서 흑색이 들어오면 0으로 초기화
a3 = np.ones(3) # 1로 초기화
a4 = np.arange(1,7,1) # 1부터 7미만까지 배열 생성 조건이 있는 배열 만들기
k1 = np.eye(3)
k1

# %%
# c = np.arange(1,5)
c = np.array([1,2,3,4])
c
c.shape= (2,2) # 2행2열 형태변환
c
c.shape=(4,) # 1행 4열 형태변환
c
c = np.full((2,2),3) # 특정 형태 배열을 특정 값 채우기
c

# %%
na = np.arange(1,9)
na.reshape(2,4)

# %%
a = na.reshape(2,4)
a[1,1]
a[1][1]

# %%
k =  np.random.random((2,2))
k

# %%
array = np.array([
    [[0,1,2,3],
    [4,5,6,7],
    [8,9,10,11]],
    [[0,1,2,3],
     [4,5,6,7],
     [8,9,10,11]]
])
array
# array = np.arange(1,25).reshape((2,3,4)) 자동으로 만드는법
# array
array.shape
array[1,1,2]

# %%
# 행렬 연산
# 같은 모양의 행렬만 가능 shape 이 다르면 안됨
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print(x+y," /")
print(np.add(x,y)," /")
print(x-y," /")
print(np.subtract(x,y)," /")
print(x*y," /")
print(np.multiply(x,y)," /")
print(x/y," /")
print(np.divide(x,y)," /")
print(np.sqrt(x))
# 수학에서의 완전 행렬 연산과는 다름 동일 위치에서의 곱셈

# %%
import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11,12])

print(v.dot(w))
print(np.dot(x,v))

print(x.dot(y))
print(np.dot(x,y))

print(x@y)

# %%
a = [1,2,3]
b = [3,4,5]
type(a) #list
2*a # a 두번 반복

a+b # 두 리스트 합쳐짐


# %%
import numpy as np
a = np.array([1,2,3])
b = np.array([3,4,5])
type(a) #nbarray
2*a # 각요소를 2 곱함
a+b # 각 요소를 더함

# %%
c = np.array([[1,2,3],
              [4,5,6]])
c
c.size # a의 원소갯수
c.shape # a의 형태
np.arange(10).reshape(2,5)
np.arange(2,3,0.1) # 2에서3까지 0.1씩 증가
np.linspace(1.0,4.0,6) # 1.0에서 4.0까지 등간격 6원소 배열 생성

# %%
import numpy as np
"""
    다양한 배열 초기화
"""
a =  np.zeros((2,2),int)
b =  np.zeros((2,2),float)
c =  np.ones((2,2))
d =  np.full((2,2),7)
e =  np.eye(2) # 단위행렬 identity matrix
f = np.random.random((2,2))

# %%
a = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ])
a[0, 0]       
# → 1
# 첫 번째 행, 첫 번째 열의 원소

a[0][0]       
# → 1
# 위와 같음 (비추 방식)

a[(0, 0)]     
# → 1
# 튜플로 지정한 것도 같음

a[1, 2]       
# → 7
# 두 번째 행, 세 번째 열

a[-1, -1] += 10  
# → a는 다음과 같이 바뀜:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 22]]
# 마지막 행, 마지막 열(12)에 10 더함 → 22

a[1, :]       
# → [5 6 7 8]
# 두 번째 행 전체

a[:, 1]       
# → [ 2  6 10]
# 모든 행의 두 번째 열

a[:2, :]      
# → [[1 2 3 4]
#     [5 6 7 8]]
# 0행, 1행 가져오기 (2미만)

a[:2, 1:3]    
# → [[2 3]
#     [6 7]]
# 0~1행, 열은 1~2번만

a[:, 0:3:2]   
# → [[ 1  3]
#     [ 5  7]
#     [ 9 11]]
# 모든 행, 열은 0, 2번만 (2칸씩 띄기)

a[:, -1:-4:-2]
# → [[ 4  2]
#     [ 8  6]
#     [22 10]]
# 모든 행, 마지막 열부터 거꾸로 -2 간격으로: 열 -1, -3 (즉 열 3,1)

a[:, [3, 0, 2, 1]]  
# → [[ 4  1  3  2]
#     [ 8  5  7  6]
#     [22  9 11 10]]
# 열 순서만 섞어서 추출

a[[0,1,2],[0,1,2]]  
# → [ 1  6 11]
# (0,0), (1,1), (2,2) 위치의 값들 = 대각선 요소

# a[row, column] 형태가 NumPy에서는 가장 일반적이야

# :는 “전체”, start:end:step는 파이썬 슬라이싱 규칙!

# -1은 항상 “마지막 원소”를 의미해 (뒤에서부터 세기


# %%
a
a >5
a[a>5]

b=a[:] # copy
b[b%2 == 0]

# %%
c = np.array([[1,2,3],[4,5,6]])
d = np.arange(11,17).reshape(2,3)
# 동일한 shape 끼리만 사칙 연산이 가능하다
c + d
c - d
c * d
c / d

# %%
c ** 2
np.sqrt(c)
np.dot(c,d.transpose())
np.dot(c.T,d)

# %%
array.mean() # 평균
array.sum() # 합계
array.max() # 최댓값
array.min() # 최솟값
array.var() # 분산
array.std() # 표준편차 데이터셋의 분산이 너무 크면 표준편차를 맞춰야함

list1 = [3,5.6,5,8,9.5]
array = np.array(list1)
array.var()

# %%
ar = np.array([1,2,3])
print('자료형', ar.dtype)
ar = np.array(['12','2','3'])
print('자료형', ar.dtype)
ar = np.array([1.2,2.2,3.3])
print('자료형', ar.dtype)

# %%
ar = np.array([1,2,3,'4'])
print(ar)
print('자료형', ar.dtype)


# %%
ar = np.array([False,True,False,False], dtype=np.int32)
print(ar)
print('자료형 type:',ar.dtype)
print(np.argmax(ar))
from numpy import argmax
print(argmax(ar))

# %%
# 실습 문제
# 1번 : 15에서 23까지 배열 선언후 3*3으로 만들어라
arr = np.arange(15,24)
arr.shape = (3,3)
print(arr)
# 2번 : 다음의 두 배열을 만들고 두 배열을 이용해서 다음 같은 값이 나오게 [Fasle,False,False,False]
arr1 = np.arange(1,5)
arr2 = np.arange(5,9)
print(arr1>arr2)

# 3번: 아래와 같이 3학생의 중간,기말,과제 점수가 있다 각 점수에 가중치(0.4,0.4,0.2)를 주고 기타 점수 5점을 준다 그리고 다음과 같은 조건을 출력(1.중간고사 평균 표준편차,2.1번 학생의 최종점수)
mid = np.array([15,100,45])
final =  np.array([78,25,90])
task = np.array([81,45,99])
all = np.array([mid,final,task], dtype=np.float64)
print(mid.mean())
print(mid.std())
all[0,:] *=0.4
all[1,:] *=0.4
all[2,:] *=0.2
all[:]
print(all)


print(all[:,0].sum() + 5)

# 강사님 답안
weight = np.array([0.4,0.4,0.2])
sum = mid * weight[0] + final * weight[1]+task*weight[2]+5
no1_sum = sum[0]
print(no1_sum)


# %%
arr = np.arange(10,31) *2

arr = np.arange(16)
arr.reshape(4,4)

arr = np.arange(1,21)
arr2 = arr[arr%2==0] # 자주씀
arr2

# randit 무작위로 추출하지만 int로 추출
# axis = 1 행 axis=0열
# axis=0 → 행 방향으로 더함 → 각 열의 합
# axis=1 → 열 방향으로 더함 → 각 행의 합
arr = np.random.randint(1, 11, size=(3, 3)) 
print(arr)
print(arr[0].sum())
print(arr[1].sum())
print(arr[2].sum())
print(arr[0].mean())
print(arr[1].mean())
print(arr[2].mean())
row_sum = arr.sum(axis =0)
col_sum = arr.sum(axis =1)

arr1 = np.eye(3)
arr2 = np.eye(3)
print(arr1@arr)
print(arr1*arr)


# %%
import numpy as np
import matplotlib.pyplot as plt

# 1부터 25까지의 숫자로 이루어진 배열
# 배열의 각값을 0과 1 사이로 정규화(normalization)
# 정규화란 주로 0에서 1사이의 범위로 데이터를 변환하는 작업
# 정규화 공식: (x-min)/(max-min)
arr =  np.arange(26,dtype=np.float64)
print(arr)
for i in range(len(arr)):
    min = arr.min()
    max = arr.max()
    arr[i] = (arr[i]-min)/(max-min)
print(arr)
plt.plot(arr,"o")
plt.show()

# %%
# 5*5 크기의 배열을 생성하고 배열의 값은 0에서 50 사이의 랜덤 정수로 구성됨.
# 생성한 배열에서 30보다 큰값만 필터링하여 새배열 만드세요
# 필터링된 배열의 값 중 최대값, 최솟값,평균값 계산
arr = np.random.randint(0,50, size=(5,5)) 
arr2 = arr[arr>30]
arr2.mean()
arr2.max()
arr2.min()
print(arr2.max(),arr2.min(),arr2.mean())
arr3 =list([arr2.min(),arr2.mean(),arr2.max()])
plt.plot(arr3,"o")
plt.show()

# %%
# 숫자 1부터 50까지의 배열을 생성
# 배열에서 짝수만 추출해 새로운 배열 만들기
# 원본 배열과 추출한 배열을 막대 그래프로 시각화
arr = np.arange(51)
arr2 = arr[arr%2==0]
# 시각화
import numpy as np
import matplotlib.pyplot as plt

# 1~50 배열 생성
arr = np.arange(1, 51)

# 짝수만 추출
arr_even = arr[arr % 2 == 0]

# 짝수 그대로 높이로 사용
heights = arr_even  # 막대 높이를 숫자 자체로!

plt.figure(figsize=(12, 5))

# 막대 그리기 (짝수 숫자가 x축, 높이도 그 숫자)
bars = plt.bar(arr_even, heights, color='royalblue', alpha=0.8, label='짝수')

# 막대 위에 숫자 표시
for bar in bars:
    height = bar.get_height()
    x = bar.get_x() + bar.get_width() / 2
    plt.text(x, height + 1, str(int(height)), ha='center', va='bottom', fontsize=9)

# 제목 및 꾸미기
plt.title("짝수 값 크기에 따른 막대 그래프")
plt.xlabel("숫자 (짝수)")
plt.ylabel("값 (막대 높이)")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()



