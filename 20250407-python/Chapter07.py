# 연습 문제
class EvenCounter:
    def __init__(self):
        self.n=0
    def __iter__(self):
        return self
    def __next__(self):
        t = self.n
        self.n =  t + 2
        return t

my_even = EvenCounter()
for i in range(0,5):
    print(my_even.__next__(), end = ' ')
print(" ")

class EvenCounter:
    def __init__(self):
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < 20:
            t = self.n
            self.n += 2
            return t
        else:
            raise StopIteration

for i in EvenCounter():
    print(i, end=' ')
print(" ")

class EvenNumber:
    def __init__(self,n):
        self.n = n
    def getN(self):
        return self.n
    
two = EvenNumber(2)
print(two.getN())
listn = list()
for i in range(0,21,2):
    listn.append(EvenNumber(i))

for x in listn:
    print(x.getN(), end = ' ')
print(" ")

# 객체를 만드는 예제
# class Person:
#     def __init__(self,name,age,height,weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight

# hong = Person("홍길동",27,180,73)

# 반복가능 객체를 위한 내장함수
# all()
l1 = [1,2,3,4]
l2 = [0,2,4,8]
l3 = [0,0,0,0]
all(l1) # True
all(l2) # False
all(l3) # False
# any()
any(l1) # True
any(l2) # True
any(l3) # False
# bool()
bool(l1) # True
bool(l2) # True
bool(l3) # True
l4 = []
bool(l4) # False 빈칸이어도 true 아무것도 없으면 false

# 문자열을 다양한 자료구조로
char_list = list('hello')
char_tuple = tuple('hello')
char_set = set('hello')
# 문자열 slice
words = 'python은     아름다은 \t \n언어입니다' # 개행문자 tab 다 무시
words_list = words.split()
print(words_list)
time_list = ['2019','02','21']
'.'.join(time_list)
','.join(time_list)

time_str = '25-04-07 09:49:20'
t1 = time_str.split()
(year,month,day) = t1[0].split('-')
(hour,min,sec) = t1[1].split(':')

txt = 'Welcome to busan Metropolitan City'
txt.split()

greet = 'Hello,My name is Dongmin,Good to see you again'
greet.split(',')

fruits = 'Apple|Banana||Mango'
print(fruits.split('|'))
print(fruits.split('||'))

# 난수 모듈
import random
print(random.random)
print(random.uniform(3.5,3.6)) # 3.5 와3.6사이에 랜덤
print(random.randrange(10)) # 0부터 9까지 정수
print(random.randrange(3,7)) # 3부터 6까지 정수
print(random.randint(5,9)) # 5부터 9까지 정수
# 목록 반환
L = [1,10,100,1000]
print(random.choice(L))
print(random.sample(L,2))
print(random.shuffle(L))
print(L)

# seed함수(암복호화에서 seed가 아니라 salt라고 쓴다)
random.seed(0)
state = random.getstate()

print(random.sample(range(10), k=5))
print(random.sample(range(10), k=5))
random.setstate(state)
print(random.sample(range(10), k=5))

# input() (항상 스트링으로 받음)
number = input("숫자를 입력하세요")
print(int(number))
# 다중 입력
num1,num2,num3 = input('숫자 3개를 입력').split()
print(num1,num2,num3)
l1 = list[num1,num2,num3]
l2 = list[int(num1),int(num2),int(num3)]
print(int(num1),int(num2),int(num3))
print(l1)
print(l2)
# 문자열 함수
'hello'.upper()
'HELLO'.lower()
'Guidi van Rossum'.split()
'Apple,Banana,Orange'.split(',')
'Apple|Banana|Orange|Kiwi'.split('|')
# eval()
# 인자로 들어로 값을 그대로 인터프리터로 실행 ** 주의가 필요함 파일삭제 이런것도 가능
eval('10+20')
eval('(5*20)/20')
# 유니코드 반환
chr(65)
ord('A')

def fun():
    print("my name is func() !!!")
re = eval(input('input anything'))

a=input('첫번째 숫자를 입력')
b =input('연산자 입력')
c = input('두번째 숫자입력')
print(eval(a+b+c))

cr=input('3명의 국어점수(예 51,57,,98)입력:')
k1,k2,k3=eval(cr)
print(k1,k2,k3,'합계:',k1+k2+k3)

xx = input('사용자가 입력한 수열을 받아 평균 출력 예)1,2,3')
zz = xx.split(',')
# while문
def cal(a):
    result = 0
    count = 0
    while a: # a리스트에 값이 있는동안
        mark = a.pop() #a리스트 가장 마지막 값 추출
        z=int(mark)
        result+=z
        count +=1
    avarage=result/count
    return(avarage)
print(cal(zz))
# for문
def cal(a):
    result = 0
    count = 0
    for x in a:
        result += int(x)
        count +=1
    avarage=result/count
    return(avarage)

# eval 함수
xx = input('사용자가 입력한 수열을 받아 평균 출력 예)1,2,3')
zz = eval(xx) #tuple zz = (100,200,300,400)

# casting

a = input('곱할숫자1')
b = input('곱할숫자2')
result = int(a) * float(b)
print("{0} * {1} = {2}".format(a,b,result))
print("{} * {} = {}".format(a,b,result))

# print,format
print("hello""python")
print("hello"+"python")
print("hello","python") # , 는 띄어쓰기

print('i like {} and {}'.format('python','java'))
print('i like {0} and {1}'.format('python','java'))
print('i like {1} and {0}'.format('python','java')) # 플레이스 홀더

print('{0},{0},{0}! Python'.format("hello"))
print('{0},{0},{0}! Python'.format("hello","Hi"))
print('{0}{1},{0}{1},{0}{1}! Python'.format("hello","python"))
print('{0}{1},{0}{1},{0}{1}'.format(100,200))
print("%s,%s,%s"%('hello','hello','hello'))
v = 'hello'
print(f"{v},{v},{v}")

greet = 'Hello'
print('{} world!'.format(greet))
name = 'Hong GilDong'
print('My Name is {}!'.format(name))
print(f'My Name is {name}!')

name = input("enter your name")
age = input("enter your age")
job = input("enter your job")
print("name:{} age{} job{}".format(name,age,job))
print(f"name:{name} age{age} job{job}")

name = input("이름: ")
age = input("나이: ")
job = input("직업: ")
live = input("사는곳: ")
print('당신의 이름은 {}, 나이는 {}살, 직업은{}, 사는곳은{}.'.format(name,age,job,live))
print('당신의 이름은 {0}, 나이는 {1}살, 직업은{2}, 사는곳은{3}.'.format(name,age,job,live))
print('당신의 이름은 %s, 나이는 %s살, 직업은%s, 사는곳은%s.'%(name,age,job,live))
for i in range(2,15,2):
    print('{0} {1} {2}'.format(i, i*i,i*i*i))
for i in range(2,15,2):
    print('{03d} {1:4d} {2:5d}'.format(i, i*i,i*i*i))

print('1/3 dms {:.3f}'.format(1/3))
print('{:,}'.format(1234567890))

print('위도:{lat},경도{long}'.format(long='129.07E',lat='35.17N'))

numbers = input("숫자를 입력하세요 예 1,2,3").split(',')
numbers = [int(i) for i in numbers]
print(sum(numbers))

numbers = input("숫자를 입력하세요 예 1,2,3").split(',')
sum = 0
for i in numbers:
    sum += int(i)
print(sum)