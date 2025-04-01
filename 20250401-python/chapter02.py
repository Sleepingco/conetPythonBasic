# 파이썬 5가지 자료 구조, 변수유형 수(정수,float,complex,double...),문자열,리스트(업데이트 가능),튜플(업데이트 불가, 단 리스트로 값을 옮긴뒤 값을 옮긴후 다시 튜플로 변환하면 가능),딕셔너리(키:밸류,해시테이블 타입)
# arr = [1,"2",3,'4',[5,6,7]]
# for i in arr:
    # print(i)
    # if i==(arr)

fruits = ['banana','apple','orange','kiwi']
print(fruits,type(fruits))

mixed_list = [100,200,400,'apple']
print(mixed_list)

# 다양한 자료구조 선언법
list1 = list()
list2 = []
list3 = list((1,2,3))
list4 = list(range(1,10)) # 1부터 9까지 맨 끝 값 포함 x 
list5 = list('abcdef')
tuple1 = (1,2)
list1 = list(tuple1)
print(list1,list2,list3,list4,list5)

# range()함수를 이용하여 1~10 중에 짝수 출력
even_list1 = list(range(2,11,2))
even_list2 = list(range(1,6))
for i in range (len(even_list2)):
    even_list2[i] = even_list2[i] *2

print(even_list1,even_list2)

friend = ['길동','철수','은지','지은','영민']
string = list('XYZ') # 리스트가 따로 생성됨

n_list = [11,22,33,44,55,66]
print(n_list[-1])
print(n_list[-2])
print(n_list[-3])
print(n_list[-2:])

# 2부터 10까지 수중에 소수 출력
prime_list = [2,3,5,7]
print(f'prime List의 첫 원소: {prime_list[0]}')
print('prime List의 첫 원소: %d' %prime_list[0])
print('prime List의 첫 원소: {0}'.format(prime_list[0]))
print('prime List의 마지막 원소: {0}'.format(prime_list[3]))
print('prime List의 마지막 원소: {0}'.format(prime_list[-1]))

# primeList = list(range(2,11))
# for i in range(2,prime_list):
#         for j in range(2,primeList-1):
#             if i%j == 0:
#                 print()
#             else:
#                 print("pnum",i)


# nations 리스트의 인덱싱 별 출력
nations = ["korea",'china','russia','malaysia']
print("nations first index value is ", nations[0])
print("nations last index value is ", nations[-1])
print("nations last index value is ", nations[len(nations)-1]) # 인덱스 길이의 마지막 원소

# 리스트의 슬라이싱은 문자열의 슬라이싱과 동일함, 슬라이싱 할때 마지막 콜론은 인덱스 리스트에 포함되지 않는다는것
a_list = list(range(10,81,10))
print(a_list[1:5])
print(a_list[0:1])
print(a_list[0:2])
print(a_list[0:5])
print(a_list[1:])
print(a_list[:5])
print(a_list[:-2])
print(a_list[-2:])
print(a_list[::-1])
print(a_list[1::-1]) # 처음 두개항목한 슬라이싱

# 리스트 슬라이싱
n_list = list(range(15))
s_list1 = n_list[:6]
s_list2 = n_list[5:11]
s_list3 = n_list[11:]
s_list4 = n_list[2:11:2]
s_list5 = n_list[10:5:-1]
s_list6 = n_list[10:1:-2]
r_list = n_list[::-1]
s_list6 = r_list[4:13:2]

# 리스트 연산자
a= [1,2,3]
b=[4,5,6]
print(a+b,a*3,str(a)+'hi')
list1 = [1,2,3,4]
list2 =[10,20,30]
# list1 * list2 리스트 끼리는 곱셈 불가
list3 = [1,2,3,4]
list4 = [4,1,2,3]
print(list1==list3,list1==list4)

# 리스트 비교 연산자는 사전적 순서를 비교함
list5 = [2,3,3,4]
print(list1>list5,list1<list5)

# 리스트의 수정, 변경과 삭제
a=[1,2,3]
a[1]=4
a=[1,2,3]
a[1] = ['a','b','c'] # 배열이 그대로 들어감
print(a)
a=[1,2,3]
a[1:2] = ['a','b','c'] # 범위를 지정하면 배열이 풀려서 값이 들어감
print(a)
a = [1,2,3]
a[1:3] =[] # [1]만 남음
a = [1,2,3]
a[2] = [] # [1,2,[]]
a = [1,2,3]
del a[1:3] #[1] 만 남음

nList = list(range(11,67,11))
del nList[4] # 인덱스 지정 값을 지정해서 삭제 불가
print(nList)

a = [1,2,5]
a.append(4)
# a.append([5,4,3,68,9])
print(a)

a.sort()
print(a)
a=['이순신','감강찬','을지문덕']
a.sort()
print(a)
a.reverse()
print(a)
a = [1,2,5,4,7,0,9]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# 위치반환(index)
a = [1,2,5]
a.index(2)
a.index(5)
# a.index(4) # 없는 값은 에러가 나옴

# insert, remove
a = [1,2,5]
a.insert(0,4)
print(a)
a.insert(3,6)
print(a)
a.remove(1) # remove는 값을 찾아 삭제 값을 줘야함ㄴ
print(a)

# pop
a = [1,2,3]
a.pop(0) #remove와 다르게 값을 반환 인덱스를 넣어서 삭제
print(a)

# extend 와 append 차이 append는 엘리먼트를 추가하는 원리로 인해 만약 배열을 append 하면 리스트 자체가 추가됨 하지만 extend 하면 리스트가 풀려서 값이 들어감
a = [1,2,5]
a.extend([4,5])
a.append(6)
a.append([7])
print(a)

# pop와 remove 차이
a = ['a','b','c','d']
list1.pop() # 마지막 값 반환
list1.pop(1) # 인덱스 값 반환
a = ['a','b','c','d']
a.remove(a[-1]) # pop 와 비슷하지만 리턴 값이 없음

# 리스트 메소드 의 응용
a= [1,2,3]
b=[10,20,30]
a.extend(b)
print(a)
a= [1,2,3]
a.append(b)
print(a)
nlist = list(range(0,11))
nlist.insert(0,0)
nlist.reverse()
# nlist = nlist[::-1] reverse 와 동일
el = nlist.pop()
print(el,nlist)

a= ['life','is','too','short','you','need','python']
print(a[4],a[2])
# strlist = a[0] +' '+a[1]+' '+a[2]+' '+a[3]+' '+a[4] 비효율
strlist = ' '.join(a[0:4])
print(strlist)
print(len(a))
a=[1,2,3,4]
a.append([4,5])
print(a)
a.extend([4,5])
print(a)
a=[1,2,3,4]
a.sort(reverse=True)
print(a)
a=[1,2,3,4,5]
a.pop(1)
a.pop(2)
print(a)
a=[1,2,3,4,5]
a.remove(2)
a.remove(4)
print(a)
a= ['life','is','too','short','you','need','python']
a.index('is')
try:
    a.index('hello')
except:
    print('error')
# Tuple immutable 변경불가
t =(1)
print(type(t))
t=(1,)
print(type(t))
t= 1,2,3
print(type(t))
t = (1,2,3)
print(type(t))
t=('a','b','c',('a','b'))
print(t)
t=(0,1,2)
# t[0] =2 에러남
# 튜플의 장단점 데이터 공간이나 내용 크기가 달라지지 않아 생성 과정이 간단, 데이터가 오염 x(상수과 같은 이유) 효율적인 데이터 공간, 위도 경도 좌표, tgb 색상등 고정괸 값을 나타내기 편리 딕셔너리 자료형에 키값에 사용가능
t1 = (1,2,'a','b')
# del t1[1] 삭제 불가
# t1[1] = 'c' 변경불가
t1 = ('a','b',1,2) # 새로 할당은 가능

# 다양한 생성방법
tuple0=()
tuple1=(1,)
tuple2=(1,2,3,4)
tuple3=1,2,3,4
n_list = [1,2,3,4]
tuple4=tuple(n_list)

# 튜플 값 바꾸기
list4 = list(tuple4)
list4[0] = 0
tuple4 = tuple(list4)
# 하나의 요소만 넣으면 튜플이 아니라 정수형이 선언된다 그러므로 반드시 숫자나 문자뒤에 "," 를 넣어야 한다

# packing, unpacking (js의 언스트럭쳐)
a= (1,2) # packing
c = (3,4)
d ,e = c # unpacking

# Swap
a=100
b=200
temp = a
a=b
b=temp
print(a,b)
a,b = b,a # 코드가 휠씬 간결함
print(a,b)

# 인덱싱 슬라이싱
t1 = ('a','b',1,2) 
print(t1[0],t1[3])
t1[:]
t1[::-1]
# 튜플 연산자
t0=(10,20,30)
t1=t0+t0
t2=t0*3
t4 = t0 +(40,) # 엘리먼트가 맨뒤에 append 처럼 추가됨 
a=((1,2),(3,4),(5,9))
print(a[2])

# tuple 변환
t1=tuple([1,2,3,4,5])
t2=tuple("abcde")
'a' in ('a','b','c')
'5' in ('a','b','c')
'5' not in ('a','b','c')

# 1부터 100까지 더한 합을 구하시오
list1 = list(range(1,101))
sum = 0
for i in list1:
    sum += i
print(sum)

# 튜플의 최대값 구하기
tuple1 = (1,23,2,36,247,2457,66,89,979,5,5033333350,33453)
max = 0
for i in tuple1:
    if i>max:
        max = i
print(tuple1,max)

# 튜플은 변경 불가라 sort(),append() 같은 메서드를 사용이 불가함
tuple1 = tuple('abcdef')
tuple1.index('e')
tuple1.count('b')
t = (10,20,30,20,20,10,50)
t.count(10)
t.count(20)
t.index(30)
t.index(50)

# 튜플을 리스트로 변환하여 항목을 변환하고 다시 튜플로 만들어서 출력
t_fruits = ('apple','kiwi','banana','watermelon')
l_fruits = list(t_fruits)
l_fruits[0]='grape'
t_fruits = tuple(l_fruits)
print(t_fruits)
# 3 만을 가진 튜플
t = tuple([3])
# 튜플 변경 불가 에러가 나오는 이유 설명하시오
a=(1,2,3)
# a[0] = 4

# 다른 방법
a = (a[0],4,a[2])

# 튜플 추가 문제
a= (1,2,3)
a= a+(4,)
print(a)

# 딕셔너리 키:벨류 한쌍을 갖는 자료형이고 순차적으로 해동 요소를 구하지 않음 -> index가 없음
board1 = {
    "post_id": 15,
    "title": "Python Tips",
    "author": "coding_girl",
    "tags": ["python", "tips", "dev"],
    "comments": [
        {
            "user": "dev123",
            "text": "Great tips!",
            "likes": 12
        },
        {
            "user": "ai_boy",
            "text": "Thanks for sharing.",
            "likes": 7
        }
    ]
}

print(board1)
print(board1['post_id'])
board1['post_id']=16
board1['likes'] = 100
print(board1['post_id'])
del board1['tags']
print(board1)
board1[1] = '가나다라'
print(board1)
del board1[1]
print(board1)

# 튜플은 인덱스가 아니라 키값으로 찾는다
grade = {'pey':10,'juliet':99}
print(grade['pey'])
# 키에는 리스트를 쓸 수 없지만 튜플은 쓸 수 있다
# a= {[1,2]:'ji'}
a= {(1,2):'ji'}
a={'name':'pey','phone':'01099992222','birth':"1118"}
print(a.keys())
print(a.values())
print(a.items()) # 키벨류 값 다 얻기
print(a.get('name')) # 값이 없으면 None이 발생함
print(a['name']) # 없으면에러가 발생함 
print(a.get('address')) # 값이 없으면 None이 발생함
# print(a['address']) # 없으면에러가 발생함 
print(a.get('address','x')) # 값이 없을때 x를 대신 출력


a.clear()


#다음의 딕셔너리를 키와 벨류로 예쁘게 찍어보자
dic = {'이름':'홍길동','나이':26,'몸무게':82,'직업':'율도국의 왕','주소':'경상북도 울릉군 울릉읍'}

# dictionary.items 로 (key,value) 의 리스트로 가져와서 찍어보자
dic_items = dic.items()
for item in dic_items:
    (key, value) = item # 언패킹
    print("%10s %15s" %(key, value))

# 딕셔너리에서도 in을 쓸 수 잇음

# 딕셔너리 추가
a={"one":'하나','two':'둘','three':'셋'}
a['four'] = '넷'
a.update({'five':'다섯','six':'여섯'}) # 다수의 요소 추가 가능
print(a)
a.setdefault('one','하나라니까') # 이미 값이 없으면 안바뀜
print(a)
del a['three']
print(a)
a.pop('one')
a.popitem()
print(a)
list1 = list(a.keys())
print(list1)
list2 = list(a.items())
print(list2)
# lst = [11,22,33,44,55]

# 딕셔너리의 항복 삭제와 변화 여부
dic = {0:11,1:22,2:33,2:44,4:55}
print('pop(0)이전' ,dic.items)
print('pop(0)이전 dic[1]' ,dic[1])
dic.pop(0)
# print('pop(0)이후 dic[0]' ,dic[2])
print('pop(0)이후 dic[1]' ,dic[1])
a['name']='python'
a[('a',)] = 'python'
# a[[1]] ='python' # 리스트는 변경이 가능해서 키 값으로 쓸 수 없다
a[250] = 'python'

a={'A':90,'B':80,'C':70}
# b= a['B']
# del a['B'] 둘다 가능
b = a.pop('B')
print(b)
a= {'A':90, 'B':80}
# a['C']
a.get('C' , 70)
a={'A':90,'B':80,'C':70}
val = a.values()
print(val)
min = 100
for i in val:
    if min>i:
        min = i
print('최솟값',min)

print(a.items())

# 연습문제
fruits_dic = {'apple':2000,'melon':4000}
print(list(fruits_dic.keys()))
print(list(fruits_dic.values()))
print(len(fruits_dic))
# 애플이 fruits_dic에 있는지 프린트
if 'apple' in fruits_dic.keys():
    print('apple is in fruits_dic')
else:
    print("no apple in fruits_dic")
if 'mangon' in fruits_dic.keys():
    print('mago!')
else:
    print('no mango')