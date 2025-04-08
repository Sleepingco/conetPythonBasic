class FourCal:
    count = 0 # 클래스 변수
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        FourCal.count += 1
        return result
a = FourCal() # a.에 a개 self를 뜻함
a.setdata(4,2)
print(a.first) # 4
print(a.second) # 2
FourCal.setdata(a,7,8) # 다른 호출 방법
print(a.first) # 7
print(a.second) # 8

# 클래스 변수와 인스턴스 변수 설명 추가

for i in range(1,10):
    result = a.sum()

    print("결과는",result,"count는",a.count)
b =FourCal()
b.setdata(7,8) #b.first = 7 b.secont = 8
print(b.sum()) # 15
print(FourCal.count) #2
print(a.sum()) # 6
print(FourCal.count) #3
print(b.sum()) # 15
print(FourCal.count) #4
print(a.count) # Four.count 4
print(b.count) # Four.count 4

# 클래스 변수가 변경되면 모든 객체들에게도 변경된 내용이 적용됨
# 반대로 객체 변수가 변경 되었다고 해서, 클래스변수가 변경되지는 않음

class 클래스명:
    def __init__(self, 매개변수):
        self.인스턴스변수 = 매개변수

class Daeheeyun:
    class_value = 0
    def __init__(self):
        self.instance_value = 0
    def set_class_value(self):
        Daeheeyun.class_value =10
    def set_instance_value(self):
        self.class_value = 20
instance1 = Daeheeyun()
instance2 = Daeheeyun()
print("클래스 속성 변경")
instance1.set_class_value() # class_value = 10
print(instance1.class_value,instance2.class_value) # 10 10
print("클래스 속성 변경")
instance1.set_instance_value() # instance1_value = 20
print(instance1.class_value,instance2.class_value)
print("속성(Attribute)출력")
print(instance1.__dict__)
print(instance2.__dict__)

# 안햇갈릴려면
# 클래스 변수 는 class이름.class변수
# 인스턴스 변수는 intance이름.인스턴스변수
# 이런식으로 통일하면 혼동을 덜함

# __dict__ 속성 설명
# 초기 생성자 initializer 설명 추가
class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def sum (self):
        result = self.first + self.second
        return result
    def __mul(self):
        result = self.first * self.second
        return result
a = FourCal(4,2) # a.first = 4, a.second =2
print('a.first: ', a.first) #4
print('a.second: ', a.second) #2
print('a.sum: ', a.sum()) #6
# print('a.mul: ',a.__mul()) # 없다고 나옴 private

# 파이썬 언더스코어 용도 1. 인터프리터내 마지막 저장값, 값을무시, 한모듈내부에서 private 클래스/함수/변수/메서드를 선언 사용하는 컨밴션 from module import *시_로 시작하는 것들은 무시 ex__init__
# a = 3
# _ + 5
# _ *10
x,_,y = (10,2,5)
# x,_,y = (10,2,2,4,5,6,7,8,9,5)
for _ in range(10):
    print('x',end='')
print('')

# 클래스의 상속 (inhetitance)
# 어떤 클래스르 만들대 다른 클래스의 기능을 물려받을 수 있게 만드는것
# 라이브러리 형태이거나 수정이 불가하면 반드시 상속이 필요함

class MoreFourCal(FourCal): # 부모에게 first와 second가 이미 있으므로 내꺼
    def pow(self):
        result = self.first ** self.second
        return result
m = MoreFourCal(4,2) # 인스턴스 생성
print(m.pow()) # 현재 클래스 메소드 실행
print(m.sum()) # 부모 클래스 메소드 실행
print(m.first)

class Calculator: # 부모 클래스
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second
class Scientific_calculator(Calculator): # 자식 클래스
    pass
sc = Scientific_calculator(4,2)
print(sc.add())
print(sc.mul())
print(sc.sub())
print(sc.div())

# 메소드 오버라이딩
class BaseClass: # 부모클래스
    def myfunc(self):
        print("BaseClass myfunc")
class InhClass: # 자식 클래스
    def myfunc(self):
        print("InhClass myfunc")

ex1 = BaseClass()
ex2 = InhClass()
ex1.myfunc()
ex2.myfunc()

# 다중상속
# class 새로운클래스(베이스클래스1,베이스클래스2):
# 다중 상속시 상속 받을 클래스의 이름이 앞쪽에 있는 클래스가 우선권을 얻음
#즉 클래스1과 클래스2 클래스 3에 동일한 메소드가 있다면 클래스1의 매소드를 상속해야함
class Base1:
    def myfunc(self):
        print("base1")
class Base2:
    number1 = 100
    number2 = 200
    def myfunc2(self,a,b):
        print(a**b)
class Base3:
    def myfunc2(self,a,b):
        print(a+b)
class InhClass(Base1,Base2,Base3):
    number3 = 300

ex1 = InhClass()
ex1.myfunc() # Base1
ex1.myfunc2(ex1.number1,ex1.number3) # 100 + 300 = 400

# 다중상속시 mro 설명 추가
class A:
    def greeting(self):
        print("A")
class B(A):
    def greeting(self):
        print("B")
class C(A):
    def greeting(self):
        print("C")
class D(B,C):
    pass
x=D()
x.greeting()
print(D.mro)

# Overring 오버라이딩
class Person:
    def greeting(slef):
        print("안녕하세요 부모입니다")
class Student(Person):
    def greeting(slef):
        super().greeting() # 부모의 메소드도 쓰고 싶음 super()
        print('자식은 파이썬 코딩중 입니다')
x = Student()
y = Person()
y.greeting()
x.greeting()
# 예제
class Data:
    def __init__(self, data):
        tmp = data.split("|")
        self.name = tmp[0]
        self.age = tmp[1]
        self.grade = tmp[2]
    def print_age(self):
        print(self.age)
    def print_grade(self):
        print("%s님 당신의 점수는 %s입니다."%(self.name,self.grade))
data =  Data("홍길동|42|A")
data.print_age()
data.print_grade()

class Calculator:
    def __init__(self):
        self.value = 0
    def add(self,val):
        self.value += val
cal = Calculator()
cal.add(4)
cal.add(3)
print(cal.value)