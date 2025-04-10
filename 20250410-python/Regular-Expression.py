# 정규 표현식
# 필요한 경우(주민번호,비밀번호8자리이상 특수문자!@#$% 허용 대소문자,검색보통은 db에 의존함)
data = """
park 800905-1049118
kim 700905-1059119
"""
result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

import re

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))
# match(),search(),findall(),dinfiter()

p = re.compile('[a-z]+') # a to z more than 0
m= p.match("python")
m2= p.match("3 python")

print(m)
print(m2)
print(p)
m = p.match('stirng goes here')
if m:
    print("match found:",m.group())
else:
    print("no match")

m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

m=p.search("python")
print(m)
m=p.search("3 python")
print(m)
result = p.findall("life is too short")
print(result)

result = p.finditer("life is too short")
for r in result: print(r)

p = re.compile('a.b') # .은 줄바뀸 문자를 제외한 모든 문자와 매치는 규칙
m = p.match('a\nb')
print(m)

p = re.compile('a.b',re.DOTALL)
m=p.match("a\nb")
print(m)

p = re.compile('[a-z]+',re.IGNORECASE)
m=p.match("AxB")
print(m)

p = re.compile("^python\s\w+")
data = """python one
life is too short
python two
you need python
python three
"""

print(p.findall(data))
p = re.compile("^python\s\w+",re.MULTILINE)
print(p.findall(data))

charRef = re.compile(r"""
                     &[#]
                     (
                     0[0-7]+
                     |[0-9]+
                     |[0-9a-fA-F]+
                     )
                     ;
                     """,re.VERBOSE)

p = re.compile(r'\\section')

data = "\section"
print(p.findall(data))

import re
text = """이름 : 김철수
전화번호 " 010-1234-1234
나이 : 30
성별 : 남"""
print(re.findall("\d+",text))
print(re.findall("\D+",text))
print(re.findall("\W+",text))

import re
with open('./20250410-python/doremisong.txt','r') as doremi:
    mytext = doremi.read()
    exp1 = r'\s...\s'
    print('exp1: ', re.findall(exp1, mytext))
    exp2 = r'([a-zA-Z]+),'
    print('exp2: ',re.findall(exp2, mytext))

with open('./20250410-python/hunmin.txt','r', encoding="UTF-8") as hunmin:
    hantext = hunmin.read()
    exp1 = r'[가-힝]{5}'
    print('exp1: ', re.findall(exp1, hantext))
    exp2 = r'\s사[가-힝]*\s'
    print('exp2: ',re.findall(exp2, hantext))

p =re.compile('0[1-8][0-9]?-[0-9]{3,4}-[0-9]{4}')
p = re.compile('[a-zA-Z0-9_]+@([a-zA-Z0-9_]+.){1,3}[a-zA-Z0-9_]')
telNum = True
tel_exp = '0[1-8][0-9]?-[0-9]{3,4}-[0-9]{4}'
while telNum:
    try:
        telNum = input(["PhoneNumber >> "])
        if not telNum:
            raise Exception
        result = re.match(tel_exp,telNum)
    except:
        print("wrong num")
    else:
        if result:
            print("success")
        else:
            print("worng format")

text = "사과 딸기 바나나 수박 메론"
text = text.split(" ")
print(text)
text = "사과 딸기 바나나 수박 메론"

text = re.split(" ",text)
text = re.split(r",|\n",text)
print(text)