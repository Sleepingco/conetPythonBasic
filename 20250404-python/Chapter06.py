# 람다 함수, 문법, 장점 추가
sum = lambda a,b: a+b
myList = [lambda a,b:a+b, lambda a,b: a*b]
myList[0](3,4)
myList[1](3,4)

f = lambda:1
f()

g = lambda x,y:x+y
g(1,2)
(lambda x: x**x)(3)

def add(x,y):
    return x+y
add =  lambda x,y: x+y
print('100과 200의 합:', add(100,200))
print('100과 200의 합:', (lambda x,y:x+y)(300,100))

# 다중 입력
f = lambda *x: max(x) *2 # 가변인자를 받아서 가장 큰 수 곱
print(f(1,3,7))

# 다중 반환
f = [lambda x: x+1,lambda x:x+2, lambda x:x+3]
print(f[0](1))
print(f[1](1))
print(f[2](1))

# 딕셔너리 활용
dic1 = {'add': lambda x,y:x+y,'sub':lambda x,y: x-y, 'mul':lambda x,y:x*y,'div': lambda x,y :x/y}
print(dic1['add'](3,4))

# 일반 함수와 람다 함수
def sub(x,y):
    return x-y
sub(3,4)

f = lambda x,y:x-y
f(3,4)

# filter 함수 / 구조 filter(함수, 범위)
f = lambda x: x>0
print(list(filter(f, range(-5,5))))

list1 = [1,2,3,4,5,6,7]
f = lambda x:x%2==0
print(list(filter(f,list1))) # 리스트 또는 셋 구문을 추가 하지 않으면 filterobject 등의 iterator 형태로 출력됩니다.

# filter는 값을 조작하는게 아니라 true false만 확인 하기 때문에 리스트 값을 그대로 출력함
def func(x):
    if x>0:
        return x
    else:
        return x-100
print(list(filter(func,range(-5,5))))

def adult_func(n):
    if n>=19:
        return True
    else:
        return False
ages = [34,39,20,18,13,54]
print('성년 리스트 :')

# 같은 코드 두개지만 쓰기 나름
a = list(filter(adult_func, ages))
print(a)
for a in filter(adult_func,ages):
    print(a, end =' ')
print('\n')

# 람다 함수를 이용해서 간략하게 작성
ages = [34,39,20,18,13,54]
print('성년 리스트')
for a in filter(lambda x:x>=19,ages):
    print(a, end =' ')
print('\n')

# 음수 값을 추출하는 함수
def minus_func(n):
    if n<0:
        return True
    else:
        return False
nList = [-30,45,-5,-90,20,53,77,-36]
minusList = []
for n in filter(minus_func,nList):
    minusList.append(n)
print("음수 리스트",minusList)

# for문도 필요 없음
minusList = list(filter(lambda x: x<0, nList))
print(minusList)

nList = [1,2,3,4,5,6,7,8,9,10]
evneList = list(filter(lambda x:x%2==0, nList))
oddList = list(filter(lambda x:x%2==1, nList))
print("짝수 리스트:",evneList)
print("홀수 리스트:",oddList)

newList =[]
for a in filter(lambda x:x%2==0,nList):
    newList.append(a)
print("append를 이용한 리스트 짝수", newList)

oddList = []
for o in filter(lambda x:x%2==1, nList):
    oddList.append(o)
print("oddLsit =",oddList)

# 한줄에 몰아 넣기
print(list(filter(lambda x: x%2==1, nList)))

# 맵 함수
a= [1,2,3,4,5,6,7]
square_a = []
for n in a:
    square_a.append(n**2)
print(square_a)

# map(적용시킬 함수, 반복 가능 객체)
def square(x):
    return x**2
a=[1,2,3,4,5,6,7]
square_a = list(map(square,a))
print(square_a)
# 람다식 이용
a=[1,2,3,4,5,6,7]
square_a = list(map(lambda x:x**2,a))
print(square_a)

# 대문자 반환
aList  = ['a','b','c','d']
def toUpper(a):
    return a.upper()
upperAList = list(map(toUpper,aList))
print(upperAList)
# 함수를 람다식으로 변환
upperAList = []
upperAList = list(map(lambda x:x.upper(), aList))
print(upperAList)

# 두배 세배 문제
nList = [10,20,30]
def twice(x):
    return x*2
def triple(x):
    return x*3
twice = list(map(twice,nList))
triple = list(map(triple,nList))
print(twice,triple)
twice = list(map(lambda x: x*2,nList))
triple = list(map(lambda x: x*3,nList))
print(twice,triple)

# 람다 함수 장단점 축약된 표현 때문에 코드가 간결해진다 일반함수는 재사용을 위해 메모리 할당이 필요하지만 람다는 별도의 공간을 할당하지 않기 때문에 메모리 효율적 한번사용하는 익명 함수이기 때문에 사용후 힙메모리에서 사라짐, 코드가 길어지면 가독성이 떨어진다

# zip()함수
a="yun"
b =  [1,2,3]
c= ('하나','둘','셋')
print(list(zip(a,b,c)))
print(set(zip(a,b,c)))
print(dict(zip(a,b)))
# dict는 키,밸류라 3개를 묶을 수 없음

L1 = ['a','b','c','d']
L2 = ['가','나','다','라']
for i,j in zip(L1,L2):
    print(i,j, end = ' ')

# unpacking, packing
# 반복 가능한 객체에 *(Asterisk)를 함께 사용하면 언패킹 되어 묶여있던 객체들이 나눠지게 된다. 즉 2차원 리스트는 1차원 리스트 만큼 나눠서 반환 하게 된다. 이때 zip함수를 사용하여 다시 패킹하면 각원소마다 묶기 때문에 여러 반복문을 구성하지 않아도 다시 패킹 할 수 있다 zip(*n차원 객체)는 zip(n-1차원 객체,n-1차원객체2,.. )로 볼 수있다 그러므로 반복 가능한 객체의 원소들을 대상으로 새로운 데이터를 구현 할 수 있다
# zip말고 사용처가 뭐가 더 있을까?
numbers = [[1,2,3],[4,5,6]]

print(numbers)
print(*numbers)
print(list(zip(*numbers)))
print(list(zip([1,2,3],[4,5,6])))

# reduce()함수 설명 추가해줘
from functools import reduce
a=[1,2,3,4]
n = reduce(lambda x,y:x+y,a)
# (((1+2)+3)+4) 재귀 함수 비슷
print(n)
n = reduce(lambda x,y:x*y,a)
print(n)
a= range(1,101)
n = reduce(lambda x,y:x+y,a)
print(n)
a= range(1,10)
n = reduce(lambda x,y:x*y,a)
print(n)

# list comprehension
L =[i ** 2 for i in range(10)]
print(L)
tuple_list = [(x, x*2) for x in range (1,10)]
L1 = [i**2 for i in range(10) if (i>5)]
L2 = [i**2 for i in range(10) if (i>5) and (i%2 == 0)]
L3 = [i**2 if i<5 else i for i in range(10)] # 5보다 작으면 제곱
print(L3)

# 맵과 람다 이용한 리스트 제곱
a=[1,2,3,4,5,6,7]
a=list(map(lambda x:x**3,a))
print(a)
# 리스트 축약
a=[1,2,3,4,5,6,7]
a=[x**2 for x in a]
print(a)
# 리스트 축약 표현식과 range를 이용한 리스트의 제곱
a = [x**2 for x in range(1,8)]
print(a)

st = 'Hello World'
# s_list  = list(map(toUpper, st))

s_list  = [x.upper() for x in st]
print(s_list)

# tuple은 소괄호로 간소화 생성하며 generator expression 이므로 생성자로 한번더 괄호안에 넣어야 한다.
data = [0,7,6,9,2,3]
T = tuple((i for i in data))
print(T)
# set
text = "YUNDAEHEE"
S1 = set([i for i in text])
print(S1)
# set은 가능
S2 = { i for i in text}
print(S2)

text = "cheese"
D = {i:text.count(i) for i in text}

cubic = [x**3 for x in range(1,11)]
print(cubic)

a=['Welcome','to','the','python','world']
first_a=[x[0] for x in a]
print(first_a)
ages =[34,39,20,18,13,54]
adult_ages = list(filter(lambda x:x>=19, ages))
print(adult_ages)
adult_ages = [x for x in ages if x>19]
print(adult_ages)
# adult_ages = [x if x>=19 else pass for x in ages]
n_list = [-30,45,-5,-90,20,53,77,-36]
minus_list = list(filter(lambda x:x < 0, n_list))
print(minus_list)
minus_list = [x for x in n_list if x<0]
# 필터링에 의한 조건식
s = input('정수 5개를 입력하세요:').split()
lst = [int(x) for x in s]
[int(x) for x in input ('정수를 여러개 입력하세요:').split()]
product_xy = []
for x in [1,2,3]:
    for y in [2,4,6]:
        product_xy.append(x*y)
print(product_xy)

product_xy = [x * y for x in [1,2,3] for y in [2,4,6]]
print(product_xy)

[n for n in range(1,31) if n %2==0 if n%3==0]
[n for n in range(1,31) if n % 2 == 0 if n%3==0 if n % 5 == 0]
cubic = [x**3 for i in range(1, 11) if x**3 <=500]
st = "Hello 1234 python"
list1 = [x for x in st if x.isdigit()]
str2 = ''.join(list1)
print(type(str2))

import numpy as np
_str = iter("1234")
_tuple = iter((1,2,3,4))
_list = iter([1,2,3,4])
_dict =  iter({'a':1,'b':2,'c':3,'d':4})
_set = iter((1,2,3,4))
_array = iter(np.array([[1,2],[3,4]]))

print(next(_str))
print(next(_str))
print(next(_str))

try:
    i = [10,20,30]
    iterator = iter(i)
except TypeError:
    print('list는 iterable 객체가 아닙니다')
else:
    print('list는 iterable 객체입니다')
try:
    t = ('홍길동', 22,72.7)
    iterator = iter(t)
except TypeError:
    print('tuple 은 Iterable 객체가 아닙니다')
else:
    print('tuple 은 iterable 객체 입니다')
    # 반복 가능객체인지 검사
try:
    n=100
    iterator = iter(n)
except TypeError:
    print('n은 iterator 객체가 아닙니다')
else:
    print('n은 iterator 객체 입니다')
