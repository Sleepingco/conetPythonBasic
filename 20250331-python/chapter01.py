# 파이썬 개요,역사,컴파일러,인터프리터,정적,동적타이핑, 설명, 설치,환경변수
# 아나콘다 설치, 환경변수, 개요, 명령어(conda envlist, create -n myenv python=3.8,  init, activate myenv, decativate
# 명령프롬프트 간단 명령어 'mkdir,dir,cd,code .' , 
# 파이썬 스트링,따옴표 3개는 여러줄, 파워쉘, cmd에서 파이썬 파일 실행법, 주석처리 '#' ctrl + '/'

print("hello world")
txt1 = "강아지 이름은 '햇님' 이야"
print(txt1)
txt2 = '강아지 이름은 "햇님" 이야'
txt3 = "강아지 이름은 \"햇님\" 이야"
txt4 = 'Hello''World'
txt4 = "Hello""World"
txt5 = "Hello"+"World"
txt6 = 'banana\napple\norange'
print(txt6)
long_str = """사과는 
맛있어
맛있는건 바나나
긴건 기차"""
print(long_str)
long2 ="대한민국"
# long* = "대한민국" 변수명 특수문자는 _ 만 가능 빈칸은 허용안함 
# long% = "영국"
# 2day = "today" 변수명 맨앞에 숫자는 허용안함
Day2 = "111"
day2 = "222" # 대소문자 구분 가능

print("대한민국은 사계절이 뚜렷함")
# 특수 문자열 처리:이스케이프 코드, 개행 수평탭, 문자"\", 단일 인용 부호 ",' 캐리지리턴 폼피드 벨소리 백스페이스 널문자
str1 = 'life is too short\nyou need python'
print(str1)
# raw String
a1=r'\n'
# 문자열 더하기 곱하기
head = "python"
tail = "is fun"
result =head + tail *50

x=20
if x> 20:
    print('20보다 큼')
else:
    print("20보다 작거나 같음")

# 표현식
a= 20
a2 = 10**2
print(a)
print(a2)

a=4
a2= a**0.5

# 반지름을 넣었을때 원의 둘레, 넓이
"""

원의 반지름을 이용해서
원의 둘레와 면적을 구합니다

"""
radius = 4
circumfernce = 2*3.14*radius
area = 3.14*radius**2
print("반지름 = ",radius, "원의 호 = " ,circumfernce,"원의 넓이 = " ,area)
print('나의 이름은','홍길동')
print('나의 키는',179,'cm입니다')
print('10+20 = ',10+20)
# 리터럴, 변수, 상수
# stack , Heap 메모리, 리스트를 복사하면 내용을 복사하는게 아니라 주소를 복사하기 때문데 '=' 대입이 아니라 카피를 해야함
# 2 가지 정도 변수 명을 만드는 컨벤션(관습)
# 카멜케이스 낙토(혹)
# 앞글자를 소문자로 뒷글자를 대문자로 thanksGivingDay
# 두번째 방식(전통적인 방식) 오래된 방식_
# 단어의 구분을 언더스코어로 한다. thanks_giving_day
# db에서 컬럼을 정리할때 THANKS_GIVING_DAY
# 잘안쓰는 윈도우 프로그램 쓰던 방식 c c++ 헝가리안 표기법
# bName,iNum
# 배열일때 복수명을 쓸거냐
# name = ["이승권","홍길옹","이순신","나영석"]
# nameList = ["이승권","홍길옹","이순신","나영석"]
# 변수 삭제방법
del(radius)
# 다중 할당문, 동시 할당문
num1 = num2 = num3 = 300
num4 , num5 = 300, 400
# 파이썬 기본 자료구조 수,문자열,리스트,튜플,딕셔너리, 세트
# mutable,immutable
st="123"
st="456"
print(st[0:1])
# str[0] = '5'
str2 = '1' + st[1:]
print(st)
print(str2)
# 자료형 확인
print(type(str2))
# 수치 연산자 정리

# 문자열과 정수의 덧셈 연산
myage = 17
height = '177'
# print(myage + height)
print(myage + int(height))
d= 'abc'
e=222
f=d+str(e)
print("f=d+e",f)
# 부울식
a=100
b=200
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
# '> =' 빈칸있으면 오류남 '=<' 순서가 바뀌면 에러남
print((a==b)and(a!=b))
print((a==b)or(a!=b))
print(False or(a!=b))
print(False and(a!=b))
print(bool('aa'))
print(bool('100'))
print(bool(0))
print(bool(''))
print(bool([]))
print(bool(-1))
print(not(bool(-1)))
# 연산자 우선 순위
a = False
b = a or True==True
b = a and False == False
print(b)
# 부울대수 공식 분배 법칙 드몰간의 법칙
a=True
b=False
c=not(a or b)
d=(not a)or(not b) # 잘못됨 예제
d=(not a) and ( not b)
# 연습문제 평균 구하기, 홀수 짝수 구하기
k=80
e=75
m=55
avg = (k+e+m)/3
print(avg)
print((80+75+55)/3)
i = 13%2
if i == 1:
    print("홀수 입니다")
elif i==0:
    print("짝수입니다")
else:
    print("입력값이 잘못되었습니다")

# 문자열 인덱싱과 슬라이싱 맨 앞은 0부터 맨뒤는 -1 부터
a="Life if too short, You need Python"
print(a)
print(a[0],a[1],a[-1],a[-2])
# 문자열은 한번 지정하면 더이상 바꿀 수 없음
print(len(a))
print(a[0])
print(a[-1])
print(a[33])
print(a[0],a[0],a[1],a[2],a[3])
print(a[0:4])
print(a[4:0])
print(a[19:34])
print(a[:])
# [:] 처음부터 끝까지 전부
# [x:] x에서 끝까지
# [:y] 처음 부터 y-1 까지
# 문자열을 변경하려면 새로운 변수를 만들어서 슬라이싱
a="pithon"
a= a[:1] + 'y'+ a[2:]
print(a)
# 문자열 포맷팅
a= 3.141592
d= 3.145592
b=3.
c=5
print("파이는 %f 입니다" %a)
print("파이는 %5.2f 입니다" %a)
print("파이는 %5.02f 입니다" %b)
print(f"파이는{a}")
print("파이는{0} 입니다 그리고 {1}은 정수입니다".format(a,c))
print(f"파이는{a} 입니다")
print(f"파이는{d:5.2f} 입니다") # 반올림 해줌
# 문자열 관련 함수들
# a.count
# find  인덱스 반환 없으면 -1 반환
# index  없으면 오류발생
# join
# upper
# lower
# lstrip
# rstrip
# strip
# replace
# split 구분자가 있는 문자열을 배열로 나눌수 있음

aaa = "Life is short, Life is long"
bbb = aaa.replace("Life","stick")
print(bbb)
bbb = aaa.replace("Life","stick",1)
print(bbb)

str2 = "영어, 국어, 수학, 과학" # csv 형식
list2 = str2.split(",")
print(list2)

# 주민번호 슬라이싱
hongNum = "881120-1068234"
bDay = hongNum[0:6]
pDay = hongNum[7:len(hongNum)]
print("BirthDay: %s, postDay: %s" %(bDay,pDay))
pDay2 = hongNum[7:-1]
print(f"BirthDay: {bDay}, postDay: {pDay2}")
genderNo = hongNum[7:8]
print(genderNo)
# replace
string = "a:b:c:d"
string2 = string.replace(":","#")
print(string2)

# 연습문제
naver = "http://naver.com"
naver = naver[7:]
print(naver)
naver = naver[:naver.find(".")]
print(naver)
naver = naver[:3]+str(len(naver))+str(naver.count("e"))+"!"
print(naver)