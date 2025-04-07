with open("C:/VisualStudio-WorkSpace/PythonBasic/20250407-python/score.csv",'r',encoding='utf-8') as file:
    korean = list()
    english = list()
    math = list()
    for line in file.readlines():
        line = line.strip()           # 줄 끝 \n 제거
        fields = line.split(",")      # 쉼표 기준으로 나누기
        (_,_,k,e,m) = fields
        korean.append(int(k))
        english.append(int(e))
        math.append(int(m))
    sum_k = 0
    sum_e = 0
    sum_m = 0
    for k in korean:
        sum_k += k
    for e in english:
        sum_e += e
    for m in math:
        sum_m += m
# print('국어 평균{},영어평균{},수학평균{}'%(sum_k/4,sum_e/4,sum_m/4))
print('국어 평균: {}, 영어 평균: {}, 수학 평균: {}'.format(sum_k/4,sum_e/4,sum_m/4))


with open("C:/VisualStudio-WorkSpace/PythonBasic/20250407-python/score.csv", 'r', encoding='utf-8') as file:
    korean = []
    english = []
    math = []

    for line in file.readlines():
        line = line.strip()  # 줄 끝 \n 제거
        fields = [f.strip() for f in line.split(",")]  # 공백 제거 포함

        if len(fields) == 5:
            _, _, k, e, m = fields
            korean.append(int(k))
            english.append(int(e))
            math.append(int(m))
        else:
            print("⚠️ 잘못된 줄:", line)

# 과목별 합계
sum_k = sum(korean)
sum_e = sum(english)
sum_m = sum(math)

# 평균 계산
avg_k = sum_k / len(korean)
avg_e = sum_e / len(english)
avg_m = sum_m / len(math)

# 출력
print('국어 평균: {}, 영어 평균: {}, 수학 평균: {}'.format(avg_k, avg_e, avg_m))
