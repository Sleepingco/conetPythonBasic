# 함수는 기능만 자료는 없이 기능만 클래스는 자료와 기능 둘다 있음
# 오브젝트 오리엔티드 프로그래밍이 각광받던건 2000년대 초 예전 얘기
# Set 집합 키가 없는 딕셔너리, 중복 허용x, 순서가 없음(리스트 튜플은 순서가 있음)
from copy import copy
s1 = set([1,2,3])
print(type(s1))
s1 = {1,2,3}
s2 = set("hello") # 중복 허용안함 중복제거할때 사용 가능
print(s2)
s= set([1,2,3])
t= tuple(s)
print(type(t),UnicodeTranslateError)
seet0 = {} #이렇게 선언하면 딕셔너리가됨
set1 ={1,2,3,4}
n_tuple = (1,2,3,4)
set2 = set(n_tuple) # 튜플을 셋으로
n_list = [1,2,3,4]
set3 = set(n_list) #리스트를 셋으로
days_list = ['Mon','Tue','Wed','Thi','Fri','Sat,',"Sun"]
days_set = set(days_list)
print(type(days_set))
fruits_tuple = ('apple','orange')
fruits_set = set(fruits_tuple)
h_str= 'hello'
h_set = set(h_str)
# h_set[0] 순서가 없어서 인덱스가 없음

# 교집합, 합집합, 차집합 등등등 다양한 명령어 정리 아래 예시 외 에도 더 많음
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print(s1 & s2)
s1.intersection(s2)
s1|s2
s1.union(s2)
s1-s2
s1.difference(s2)
s2-s1
s2.difference(s1)
s1 ^ s2 # 대칭 차집합
#subset, superset,disjointset,symmetric_diffrence,discard
s1.add(7)
s1.update([8,9,10])
s1.discard(9)
s1.remove(10)
print(s1)
s={100,100,200,200,300,400}
s.add(500)
s.discard(100)
s.remove(200)
# 자료형에서 set은 마이너 리스트가 메이저 주로 쓰임
s=set(['a','b','c'])
a=[1,1,2,2,3,3,4,4,4,55,5]
s1 = set(a)
a= list(s)
s1 = set('abcde')
s2 = set('cdefg')
print(s1-s2)
a={'a','b','c'}
type(a)
a={}
a=set()
a=set('abc')
a.update('def')

# boolean
a= True
b = False
1==1
2<1
3 in (1,2,3)
3 in [1,2,3]
4 in [1,2,3]
bool('python')
bool('')
bool([1,2,3])
bool([])
bool(3)
bool(0)
True and True
True or False
not True
True & False
True | False
print('a' in 'abc')
a not in [1,2,3]

# 변수 메모리 주소를 가르키는 포인터
a=3
print(id(a))
b=a
print(id(b))
a is b
a=4
print(id(a))
print(id(b))
a=[1,2,3]
print(id(a))
b=a # 주소를 공유함
a is b
a[0] = 4
print(id(a))
print(id(b)) # 리스트는 a가 바뀌면 b 도 같이 바뀜 그냥 변수랑은 다름 자료형은 새로 할당하는게 아니라 기존 값을 변경하는 방식 일반 변수는 a를 새로 할당하면 메모리에 새로 할당함 자료가 무거운 자료구조는 주소를 복사함
# 만약 b의 값을 유지하고 싶으면 copy를 사용하면 됨 혹은 slice 리스트 b=[:]를 사용하면 값이 유지
a = [1,2,3]
b=a
a is b
a[0] = 4
# b의 값과 주소가 바뀜
b=a[:] # 새로 할당
a[0] = 5
print(a,b)
# copy
aa = [1,2,3]
id(aa)
bb = copy(aa)
id(bb)
aa is bb
aa[0]=4
print(aa,bb)
# 리스트 안에 리스트가 들어있으면 원본이 바뀌면 같이 바뀜
s=[1,2,3,[4,5,6]]
c = s[:]
c[3][0] = 'c'
print(s)
# 원본을 복사할때 원본에 영향을 미치지 말아야할 경우 deepcopy 사용
# s =  [1,2,3,[4,5,6]]
# c = copy.deepcopy(s)
# c[3][0] = "c"
# 만약 원본이 필요하면 꼭 deepcopy가 아니라도 파일/db에 저장하고 불러오면 된다.

# 변수를 만드는 여러가지 방법
a,b = ('python','life')
c = ('python')
(a,b) = 'python','life'
[a,b] = ['python' , 'life']
a = b= 'python'
a = 3
b=5
a,b=b,a
(a,b)=(b,a)
# 튜플을 사용하지 않으면
temp = a
a=b
b=temp

# 연습문제
a=[1,2,3]
b=[1,2,3]
print(a is b)
b=a
print(a is b)

a=b=[1,2,3]
a[1] = 4
print(b)

a=[1,2,3]
b=a[:]
a is b

a = [1,2,3]
a= a+[4,5]
a=[1,2,3]
a.extend([4,5]) # 둘다 결과는 같지만+는 주소가 새로 할당됨 extend는 주소가 유지되어 기존 주소에 값이 추가됨

a=[1,[2,3],4] # deepcopy 가 아니라 b의 값도 바뀜
b=a[:]
a[1][0] =5
print(a)
print(b)

# 제어문
age = 19
if age < 20:
    print('청소년 할인 입니다')
walk_count = 2000
if walk_count >=1000:
    print('목표 달성')
game_score = 800
if game_score>1000:
    print('고수')
else:
    print('평민')

num_a = 100
num_b=200
if num_a == num_b:
    print('두값이 일치합니다')

# while True:
#     str1 = input('정수를 입력하세요')
#     if str1 == "exit":
#         print("종료")
#         break
#     print("n=", str1)
#     try:
#         num = int(str1)
#     except ValueError:
#         print("error")
#         continue
#     if num % 2 == 0:
#         print(num, "은 짝수 입니다")
#     else:
#         print("홀 수 입니다")

num = 100
if num < 0:
    print("num", num," 은 음수 입니다.")
else:
    print("음수가 아닙니다")
    if num % 2 ==0:
        print("num", num," 은 짝수입니다")
    else:
        print("num", num,"은 짝수입니다")
# 파이썬은 들여쓰기가 블록이라 들여쓰기가 중요함!
a=10
b=13
if a%2==0 and b%2==0:
    print('두 수 모두 짝수')
elif a%2==0 or b%2==0:
    print("둘 중 하나만 짝수 입니다")

num =2 
if num >=1 and num<=3:
     print("3보다 작고 1보다 큼")

age = 10
if age > 10 and age <19:
    print("청소년 입니다")

score = int(input('tpye socre: '))
# if score >= 90:
#     print("A")
# if score >= 80 and 90>score:
#     print("B")
# if score >= 70 and score <80:
#     print("C")
# if score >=60 and score<70:
#     print("D")
# if score < 60:
#     print("F")

# if score >= 90:
#     print("A")
# else:
#     if score >= 80 and 90>score:
#         print("B")
#     else:
#         if score >= 70 and score <80:
#             print("C")
#         else:
#             if score >=60 and score<70:
#                 print("D")
#             else:
#                 if score < 60:
#                     print("F")

if score >= 90:
    print("A")
elif score >= 80 and 90>score:
    
    print("B")
elif score >= 70 and score <80:
    
    print("C")
elif score >=60 and score<70:
    
    print("D")
else:
    print("F")

# 브레이크 포인트로 코드의 어느지점에서 에러가 나는지 추적함, 리모트 디버깅도 있음
speed = int(input("당신의 자동자는 몇키로?"))

if speed >= 100:
    ret="고속"
elif speed > 60:
    ret = '중속'
else:
    ret = '저속'
print ('자동차의 속도는',ret,'입니다')

# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우 (조건부 표현식)

#연습문제
money = 5000
card = False
if card == True or money>4000:
    print('택시에 탑니다')

if card:
    canTakeRide = True
elif money>=4000:
    canTakeRide = True
else: 
    canTakeRide = False
if canTakeRide:
    print('택시탐')
else:
    print('내려!')

lucky_list = [1,9,23,46]
if 23 in lucky_list:
    print("야호")
else:
    print("꽝")

no = 132412341
if no % 2 == 0:
    print("even")
if no % 2  ==1:
    print("odd")

age = 30
height = 180
if age<30 and height>170:
    print("yes")
else:
    print("no")

a="life is too short, you need python"
if "wife" in a:
    print("wife")
elif "python" in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print("shirt")
elif 'need' in a:
    print('need')
else:
    print('none')

# while문
i = 0
while i<5:
    print('hi')
    i+=1

st = "programming"
for ch in st:
    if ch in ['a','e','i','o','u']:
        break
    print(ch)
print("the end")

for ch in st:
    if ch in ['a','e','i','o','u']:
        continue
    print(ch)
print("THE END")
# brak와 continue의 위험성 너무 많이 사용하면 흐름이 일관되지 못해 이해하기 어려워진다
tree = 10
def Hit():
    tree -1
    return 1
while tree>0:
    tree -= Hit()
    print("나무체력:",tree)
    if tree==0:
        print("나무가 쓰러졌습니다")
prompt = """
        1.add
        2.delete
        3.list
        4.quit"""
number = 0

while number !=4:
    print(prompt)
    number = int(input())

coffee = 3
while True:
    money = int(input("insert coin"))
    if money == 300:
        print("here is your coffee")
        coffee -=1
    elif money > 300:
        print("here's your change %d and here's your coffee"%(money-300))
        coffee -=1
    else:
        print("not enough money. coffee left %d" %coffee)
        print("we left %d coffee"%coffee)
    if not coffee:
        print("no more coffee")
        break

num = 100
sum =0

# 1 부터 100 예제
while(num>0):
    sum += num
    num -=1
print(sum)
# for n in range(1,1000):
#     sum = sum +n

# 1부터 100가지중 3의 배수의 합
sum2 = 0
for i in range(0,101,3):
    sum2 += i
print(sum2)

# 50점 이상의 총합
a = [20,55,67,82,45,33,90,87,100,25]
sum3 = 0
for i in a:
    if i>50:
        sum3 +=i
print(sum3)

# while 문으로 별 작성
star = 1
while star<5:
    print("*"*star)
    star +=1

numbers = [11,22,33,44,55,66]
for n in numbers:
    print(n, end=" ")

# 구구단
for i in range(2,10):
    for j in range (1,10):
        print("{0}*{1} = {2:2d}".format(i, j, i*j), end=' ')
    print()

# 앞으로 할 프로젝트 대략 설명 opencv, 칼만프레임 카큘레이터,바운딩박스 객체 탐지 기술, 욜로,객체지향 프로그래밍
# 주석 잘달기, 컴퓨터 비전,로보플로우, 데이터 셋부터 만들어야.., 예측방식:라이브러리(os,cv2,ultratics,torch,glob,numpy,math,time,threading,collections,ctypes),경광등을 통해 위험을 알릴수도 있음,
# 프레임 마다 검출및 위험도 계산,객체 검출(가중치, 거리 구분, 프레임 인덱스),욜로로 바운딩 박스 좌표값 받아서 욜로로 그려줌,라벨링, 
