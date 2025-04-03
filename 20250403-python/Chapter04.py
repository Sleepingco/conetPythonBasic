# range 함수 응용
import numpy as np
a = list(range(1,101))
print(a)
b=list(range(2,101,2))
c=list(range(1,101,2))
d= list(range(-99,0,1))
e = list(range(0,-100,-1))

range(10)
range(0,10)
type(range(0,10))
type(list(range(0,10)))
list(range(0,10,2))
list(range(0,10,-3))
list(range(10,0,-3))
# list(range(0,19,0.5)) range는 int만 가능 float를 위해서는 numpy의 arange() 사용
type(np.arange(0,10,0.5)) # class = numpy.ndarray
# 파이썬 단점 라이브러리 의존성 관리가 힘듬 아나콘다는 무조건 씀
np.arange(10,0,-0.7)

# range() 예시
list(range(5))
list(range(0,5))
list(range(0,5,1))
list(range(0,5,2))
list(range(2,5))
list(range(0,10,2))
list(range(1,10,2))
list(range(-2,-10,-2))
for i in range (0,5,1):
    print(i,end=' ') # 줄바꿈 방지 가능

for i in range (0,5):
    print(i,end='/')

for i in range (-2,-10,-2):
    print(i,end='/')

test_list = ['one','two','three']
for i in test_list:
    print(i)

a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)
for t in a:
    print(t[0]+t[1])

marks = [90,25,67,45,80]
number = 0
for  mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격 입니다" %number)
    else:
        print("%d번 학생은 불합격입니다" %number)

number = 0
for  mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생은 합격 입니다 축하합니다" %number)

for i in range(len(marks)):
    if marks[i] < 60: continue
    print("%d번 학생은 합격" %(i+1))

for i in range(2,10):
    for j in range(1,10):
        print(i*j,end=" ")
    print(" ")

# for else for문이 끝까지 실행되었을때 else 실행 중간에 break되지 않으면 else 실행 도중에 중단되면 else 실행 안함
for i in range(3):
    print("i =",i)
else:
    print("END")

for j in range(3):
    if j == 2:
        break
    print("j = ", j)
else:
    print("END")

# for문 break, continue
for i in range(5):
    if i == 3: break
    print(i)
print("break")

for i in range(5):
    if i == 3: continue
    print(i)
print("continue")

list1 = list("ilovepython")
for i in range(len(list1)):
    if list1[i] == "p":
        print("we got 'p'",i)
        break
print(list1.index("p"))

def findIndex(list, find):
    for i in range(len(list)):
        if list[i] == find:
            print("we got %s"%find,"idx = ",i)
            break

findIndex(list1,"t")

# for를 while로 바꾸면
i = 0
while i<5:
    i+=1
    if i ==3:
        break
    print(i)
print("break")

i = 0
while i<5:
    i+=1
    if i ==3:
        continue
    print(i)
print("continue")

# 연습문제
for _ in range(5): # 언더스코어 루프 제어변수 변수를 안쓸때 '_' 대체함
    print("hi python")

list1 = [(0,0),(100,200),(300,400)]
for(_,y) in list1: #x좌표는 안쓰므로 '_'로 대체 가능
    print("y좌표는 %d"%y)

# for문 enumerate() 함수 iterator(반복자)를 지원하는 객체를 색인 값과 요소를 동시에 반환하는 객체
names = ["a","b","c"]
for x, name in enumerate(names):
    print(x, name)
# zip() 함수
names = ["a","b","c"]
scores = [70,80,90]
for (name,score) in zip(names,scores):
    print(name,scores)

# 다중 색인 반환
data1 = ["python","076923","yundaehee","x"]
data2 = ["파이썬","076923","윤대희"]
for i, (datum1, datum2) in enumerate(zip(data1,data2)): # zip()은 자동으로 튜플을 만듭니다.enumerate(zip(...))은 (인덱스, (값1, 값2)) 구조.괄호는 그 튜플을 2개 변수로 분해하는 문법입니다
    print(i,datum1,datum2)

# 제어변수 익명화
for _ in range(10):
    print("welcome")

# while문은 수행횟수를 정확히 모르지만 수행조건이 명확한 경우에 더 적합 반복횟수가 명확한 경우 for문이 적합

# list 내포
# list1 = list() 이러한 코드를
# for i in range(3,13,3):
#     list1.append(i)
# print(list1)

# [표현식 for 항목 in 반복가능객체 if 조건]
result =[num*3 for num in range(1,5)]
print(result)
# 짝수만 곱
result =[num*3 for num in range(1,5) if num %2 == 0]
print(result)

# 조금 복잡 하지만 for문을 두개 이상 사용할 수 도있다
result = [x*y for x in range(2,10) for y in range(1,10)]
print(result)

result = [(x,y) for x in range(2,10) for y in range(1,10)]
print(result) # 튜플을 넣은 리스트는 반환 가능하지만 그냥 튜플로 만드는건 불가

# 연습 문제
result = [x for x in range(1,101)]
print(result)
sum = 0
for  n in range(5,1001,5):
    sum+=n
print(sum)

# 학급의 평균값 구해보지
a =[70,60,55,75,95,90,80,80,85,100]
avg = 0
sum =0
for i in range(len(a)):
    sum += a[i]
    avg = sum/(len(a)+1)
print(avg)
print(len(a))

bloodType = [
    'a','b','a','ab','ab','o','a','b','o','b','ab'
]
aSum = 0
bSum = 0
oSum = 0
abSum = 0
for i in bloodType:
    if i =='a':
        aSum +=1
    if j =='b':
        bSum +=1
    if i =='o':
        oSum += 1
    if i == 'ab':
        abSum += 1
print('a형은:{%d} b형은{%d} o형은{%d} ab형은{%d}명 입니다'%(aSum,bSum,oSum,abSum))

# 그룹을 모른다는 전재하에는 SET을 씀 경우가 몇개여도 총합 가능 이건 꼭 쓰자
bloodGroup = list(set(bloodType))
print(bloodGroup)
sumGroup = [0 for x in bloodGroup]
print(sumGroup)
for bt in bloodType:
    for i in range(len(bloodGroup)):
        if(bt == bloodGroup[i]):
            sumGroup[i] += 1
for (bg,sumg) in zip(bloodGroup, sumGroup):
    print("혈액형",bg,'합은 ',sumg)

# 아래가 두개가 값은 결과지만 리스트 내포(list comprehension)으로편하게 만들 수 있다
numbers=[1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 ==1:
        result.append(n*2)
print(result)

result =  [n*2 for n in numbers if n%2 ==1]
print(result)

i = '100'
print(len(i))