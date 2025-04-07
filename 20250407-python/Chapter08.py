# 파일 다루기 (인코딩을 맞춰야함),리눅스면 utf8 쓰는게 편해 근데 배포할 시스템이 윈도우면 euc-kr로 써도됨
f = open("c:/VisualStudio-WorkSpace/PythonBasic/20250407-python/새파일.txt", "w",encoding="UTF-8")
# 파일 열기 모드 r,w,a (읽기,쓰기,추가)
f.write("아름다운 이땅에 금수강산에\n")
for i in range(1,11):
    data = "%d번째 줄입니다.\n"%i
    f.write(data) # write시 데이터는 반드시 str이어야함
f.close()

f = open("c:/VisualStudio-WorkSpace/PythonBasic/20250407-python/새파일.txt", "r",encoding="UTF-8")
text =f.readline() # 파일의 한줄을 가져와 문자열로 반환
print(text)
text =f.readline() # 파일의 한줄을 가져와 문자열로 반환
print(text)
text =f.readline() # 파일의 한줄을 가져와 문자열로 반환
print(text)
text =f.readlines() #파일내용 전채를 가져와 리스트로 반환 각줄은 문자열 형태로
print(text)
text=f.read()
print(text)
while True:
    text = f.readline()
    if not text:  # 파일 끝이면 break
        break
    print(text, end='')  # 줄바꿈 방지를 위해 end=''
lines = f.readlines()
for line in lines:
    print(line)

data = f.read()
print(data)
f.close()

with open("c:/VisualStudio-WorkSpace/PythonBasic/20250407-python/새파일.txt", "r", encoding="utf-8") as file: # 블럭 끝나면 알아서 close()해줌
    content = list()

    while True:
        sentence = file.readline()

        if sentence:
            content.append(sentence)
        else:
            break
    print(content)
with open("c:/VisualStudio-WorkSpace/PythonBasic/20250407-python/새파일.txt", "r", encoding="utf-8") as file: # 블럭 끝나면 알아서 close()해줌
    content =list()
    for f in file:
        content.append(f)
    print(content)
    r = file.read()
    print(r)
f = open("c:/VisualStudio-WorkSpace/PythonBasic/20250407-python/새파일.txt", "a",encoding="UTF-8")
for i in range(11,20):
    data ="%d번째 줄입니다.\n" %i
    f.write(data)
f.close()
with open("c:/VisualStudio-WorkSpace/PythonBasic/20250407-python/새파일.txt", "a", encoding="utf-8") as file: # 블럭 끝나면 알아서 close()해줌
    words =  ["Python\n","Yundaehee\n"]
    file.write("Start\n")
    file.writelines(words)
    file.write("END")
    file.write("Hello")
f = open('c:/VisualStudio-WorkSpace/PythonBasic/20250407-python/myfile.txt','r',encoding="UTF-8")
while True:
    line = f.readline()
    if not line:break
    raw =  line.split(',')
    for i in range(0, len(raw)):
        raw[i] = raw[i].strip()
    print(raw)
f.close()
with open("c:/VisualStudio-WorkSpace/PythonBasic/20250407-python/tabseperated.txt","r",encoding="utf-8") as file:
    for line in file.readlines():
        print(line.strip().split('\t'))

# 연습문제
f1 = open("test.txt","w")
f1.write("Life is too short")
f1.close()

f2 = open("test.txt","r")
print(f2)

inputText = input("저장할 내용을 입력하세요")
with open('test.txt',"a",encoding="utf-8") as file:
    file.write(inputText+"\n")

with open('test.txt', "r", encoding="utf-8") as file:
    txt = file.read()

txt = txt.replace('java', 'python')  # ✔ 바뀐 내용을 다시 txt에 저장

with open('test.txt', "w", encoding="utf-8") as file:
    file.write(txt)

with open('sample.txt', "r", encoding="utf-8") as file:
    sum = 0
    cnt = 0
    for line in file.readlines():
        sum += int(line)
        cnt +=1
    average = sum / cnt
    with open("result.txt",'w') as file2:
        file2.write("avg ="+str(average))
