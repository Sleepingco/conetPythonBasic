# 함수,인수,매개변수 개념 설명, 지역변수
from copy import copy
from math import ceil
from math import floor
import math
import random
def print_star():
    print("*************")
print_star()
def print_plus():
    print("++++++++++++++++")
print_plus()

def get_sum(a,b):
    """
    숫자를 보내세요
    """
    return a+b
print(get_sum(1,2))
sum2 = get_sum(100,200)
print("100과 200의 두 수의 합은 =",sum2)

# 함수의 결과 값은 언제나 하나이다 return이 두개면 튜플 하나로 리턴
# 함수는 return을 만나는 순간 결과값을 돌려준 다음 함수를 빠져 나간다
def sum_and_mul(a,b):
    if(b==0):
        return 0
    return a+b,a*b,a/b
result = sum_and_mul(3,4)
(sum1,mul,div) = sum_and_mul(3,4)
print(result,sum1,mul,div)

def get_root(a,b,c):
    r1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    return r1,r2
result1,result2 =get_root(1,2,-8)
print('해는',result1,'또는',result2)

# 함수이름 정하기 뭐하면 foo로 쓴다

# 함수와 매개변수
def div(a,b=2):
    return a/b # 나누기는 리턴이 float
print(div(4))
print(type(div(4,2)))

# 디폴트 값은 앞에 파라미터에는 설정 불가 출현순서상 맨뒤에서 부터 줘야함
# def div(a=2,b,c):
#     return a/b/c

#키워드 인자
print(get_root(c=-8,b=2,a=1))
# print(get_root(c=-8,b=2,1)) 이건 안됨 키워드 인자와 위치 인자를 섞어 쓸려면 반드시 위치인자가 먼저 나타나야함
# print(get_root(1,b=2,c=-8)) 
# 함수 인수의 법칙 뒤에 내용 포함 정리. 인수는 순서대로 대입됨, 파라미터에 인수를 지정 가능

# 가변인수, 입력값이 몇개일지 모를때는 가변인수 사용
def greet(*names):
    for name in names:
        print("안녕하세요",name, "씨")
greet('홍길동','이순신','강감찬')

def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(sum_many(1,2,3,4,5,6,7,8,9,10))

def sum_mul(choice,*args):
    if choice =="sum":
        result = 0
        for i in args:
            result +=i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

result = sum_mul("sum",1,2,3,4,5)
print(result)
result = sum_mul("mul",1,2,3,4,5)
print(result)

# 연습 문제
def sum_nums(*numbers):
    sum =0
    print(numbers)
    for number in numbers:
        sum +=number
    avg = sum/(len(numbers))
    print("합계",sum,"평균",avg)
sum_nums(1,2,3,4,5)

# 최솟값 구하기
def min_minus(*numbers):
    min = numbers[0]
    for number in numbers[1:]:
        if(min>number):
            min =number
    return min
print("최솟값은 %d"%min_minus(23,34,1,5))

# 키워드 인자 (딕셔너리로 저장되는 변수)
def func(**kwargs):
    print(kwargs)
func(a=1)
func(name="foo",age=3)

# 가변인수와, 키워드 인자를 혼용으로 사용가능 /사용법과, 주의점
def func(*args, **kwargs):
    print(args)
    print(kwargs)
func(1,2,3,4,5,name="hong",age=3)
# func(1,2,3,4,5,name="hong",age=3,4,5) 불가

# *args(Tuple), **kwargs(Dictionaey) /혼합 논리에 대한 설명 추가
def func(*data, **method):
    num = sum(data) *method["scale"]
    print(num,method["unit"]+"입니다")
func(3,4,5,scale=10,unit='개')

# *args(Tuple), **kwargs(Dictionaey),message /혼합 논리에 대한 설명 추가
def func(*data,message,**method):
    print(message)

    num = sum(data) * method["scale"]
    print(num,method["unit"]+"입니다")

func(3,4,5,message="계산된 값 입니다",scale=10,unit="개")

def func(message,*data,**method):
    print(message)

    num = sum(data) * method["scale"]
    print(num,method["unit"]+"입니다")

func("계산된 값 입니다",3,4,5,scale=10,unit="개")

def func(message1,message2,*data, **method):
    print(message1)
    print(message2)

    num = sum(data) * method["scale"]
    print(num, method["unit"]+"입니다")
func("계산된 값입니다","값이 10배 커집니다",3,4,5,scale=10,unit="개")

def say_myself(name,old,man=True):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d 살 입니다." %old)
    if man:
        print("남자입니다")
    else:
        print("여장입니다")
say_myself("박응용",27)
say_myself("김영희",24,False)

# 전역변수
def print_sum():
    a=100 # local variable
    b=200 # local variable
    result =0
    result=a+b #100+200
    print('print sum 내부:',a,'과',b,'의 합은',result,'입니다')
a=10
b=20
print_sum()
result = a+b #10+20
print('print_sum() 외부:',a,'과',b,' 의 합은',result,'입니다')

# 효력 범위
a = 1
def vartest(a):
    a= a+1
vartest(a)
print(a)

# 에러 케이스 / 설명추가/ 다양한 방법 각 방법별로 디테일한 설명
# a = 1
# def varest(b):
#     a= a+1
# varest(a)
# print(a)

a = 1
def vartest(c):
    c=c+1
    return c
a = vartest(a)
print(a)

a = 1
def vartest():
    global a
    a=a+1
a = vartest()
print(a)

# 글로벌 변수 수정 가능
def print_sum():
    global a,b
    a = 100
    b = 100
    result = 0
    result = a+b
    print('print_sum() 내부:',a,'과',b,'의 합은',result,'입니다')
a=10
b=20
print_sum()
print(a+b)

# 파이썬 내장함수 모음 + import 설명/ 추가로 작성 / 주석 작성
# min(200,300,1000)
# max(200,300,400)
# str1="Foo"
# len(str1)
# eval("100+200+300")
# sorted("EAVASDFGW")
# list1 = [200,100,300,500]
# sorted(list1)
# sorted(list1, reverse=True)
# bin(10)
# abs()
# divmod()
# pow()
# # 자주 사용되는 내장함수
# int() # 소수점 자름
# float() # 2=2.0으로 반환
# str() 
# str(0x100) # 16진수로도 표현가능
# list()
# tuple()
# len()
# range()
# min(200,300,1000)
# max(200,300,400)
# sorted("EAVASDFGW")
# type()
# copy()
# ceil(2.9) #올림
# floor(2.4)#내림
# round(2.5) #반올림
# math.factorial(6)
# math.pi
# math.sin
# random.random()
# int(random.random()*6+1)
# int(random.randint(1,6))
# import datetime
# today = datetime.datetime.now()
# today.year
# today.month
# today.day
# id() / 추가 설명 추가
a_str = "Hello Python"
id(a_str)
n=300
id(n)

a=(1,2,3)
b=list(a)
print('test',type(b))

class myClass:
    age=0
print(type(myClass))

# 함수와 메소드 차이 설명 추가 ex)객체지향 언어에서의 차이점
# 클래스에 대한 설명 car 라는 클래스의 속성(바퀴 4개, 기름통 50리터, 변속기 자동), 클래스에 메소드: 달린다 좌회전, 우회전 등등 묶어서 인스턴스1,인스턴스2가 있을때 클래스는 같지만 둘은 다른차다, 두 인스턴스는 각자의 속성을 참조해서 메모리에 서로 다른 공간에 있는 다른 객체이다

# 연습문제
def is_odd(num):
    if num%2 ==0:
        return True
    else:
        return False
print(is_odd(20))
print(is_odd(21))

def my_average(*numbers):
    my_sum = sum(numbers)
    return my_sum/len(numbers)

def times_table(n):
    for i in range(1,10):
        print("%dx%d=%d"%(n,i,n*i) ,end=' ')
    print()
times_table(4)
print(my_average(1,2,3,4,5))

a = [1,2,3]
b=a.copy()
a[0]=10
print(b,"test")