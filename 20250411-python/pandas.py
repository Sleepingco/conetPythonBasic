# %% [markdown]
# 결측 데이터 처리와 필터링 \n
# 데이터 추가와 삭제 \n
# 열데이터의 정렬과 다양한 데이터 조자 \n
# 리스트,딕셔너리,넘파이 배열을 데이터 프레임으로 손쉽게변환 \n
# 각데이터 프레임 열에서 결측값의 개수와 정상값의 수를 게산 \n
# matplorlib과 잘 결합되어 손쉽게 데이터를 시각화 \n
# 한 데이터 프레임을 특정한 기준에 따라 여러 개의 데이터 프레임으로 분할 \n
# 두 데이터프레임을 결합하고 다시 인덱싱 하는 능력 등 여러가지 \n
# 
# 기능 : mean(),corr(),count(),sort_values(),groupby(),데이터 정제
# 
# 옛날에는 sam 많이씀 요즈은 csv도 쓰는데 더 많이쓰는 json

# %%
import numpy as np
import pandas as pd

se = pd.Series([1,2,np.nan,4],index=['a','b','c','d'])
se
se.isna()
print(se)
print(se['a'],se['b'],se[2],se[3])

# %%
income = {"1월":9500,"2월":6200,"3월":6050,"4월":7000}
income_se = pd.Series(income)
print(income)
print("동윤이네 상점수익")
print(income_se)

# %%
from pandas import Series,DataFrame
k=Series([100,101,102,103,104,105])
print(k)

# %% [markdown]
# Series(data = mydata,index=miyndex)
# 

# %%
income = {"1월":9500,"2월":6200,"3월":6050,"4월":7000}
income_se = pd.Series(income)

for date in income_se.index:
    print(date)
for money in income_se.values:
    print(money)
print(income_se)
print(income_se[0],income_se[1])
print(income_se['1월'],income_se['2월'])

# %% [markdown]
# 같은 인덱스 끼리 더하기

# %%
from pandas import Series,DataFrame
mine = Series([10,20,30], index=['naver','sk','kt'])
friend = Series([10,30,20],index = ['kt','naver','sk'])
merge = mine +friend
print(merge)

# %%
import numpy as np
import pandas as pd
nparray1 = np.array([[1,2,3],[4,5,6]])
display(pd.DataFrame(nparray1))
dictionary1 = {"a":["1","3"],"b":["1","2"],"c":["2","4"],}
display(pd.DataFrame(dictionary1))

# %%
from pandas import Series,DataFrame
daeshin = {
    'open' : [11650, 11100, 11200, 11100, 11000],
    'high' : [12100, 11800, 11200, 11100, 11150],
    'low'  : [11600, 11050, 10900, 10950, 10900],
    'close': [11900, 11600, 11000, 11100, 11050]
}
daeshin_day = DataFrame(daeshin)
date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)
print(daeshin_day)

print(daeshin_day.columns)
print(daeshin_day.index)
close = daeshin_day['close']
print(close)
# print(daeshin_day['16.02.24']) 에러 이건 불가
day_data =daeshin_day.loc['16.02.24']
print(day_data)

# %%
dataframe1 = pd.DataFrame(data=[4,5,6,7],index=range(0,4),columns=['S'])
display(pd.DataFrame(dataframe1))

# %%
df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]),columns=[10,11,12])
print(df)
print(len(df)) # 행의 갯수
df.columns = ['a','b','c'] # 컬럼명 바꾸기
print(df)
print(df["b"][0:2]) # 컬럼 b 중 0~1 인덱스 선택
print(df.iloc[0])
print(df.iloc[0:2])
print(df.loc[0:2]) # loc: 명치기반 인덱싱 iloc:위치기반 하지만 loc[0:2]sms 0에서 2까지임 주의!!!!!!

print(df.iloc[0:2]['b'])

# %% [markdown]
# 데이터 삭제

# %%
df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
df
df.loc[3] = [10,11,12] # 행추가 (iloc는 추가가 안됨)
display(df)
df2 = pd.DataFrame(np.array([[10,11,12]]))
# df =  df.append([[10,11,12]],ignore_index=True) # ignore_index=False의 경우 index 는 0으로 셋팅 append는 없어짐 concat()권장
df =  pd.concat([df,df2],ignore_index=True)
df
df.columns = list("ABC") #컬럼명 변경
df["D"] = list("ddddd") # 컬럼명으로 추가
display(df)
df[4] = [4]*5 #컬럼명으로추가
df[7] = [7]*5 #컬럼명으로추가
display(df)

# %% [markdown]
# 데이터 삭제

# %%
df=df.drop(7,axis=1) # 컬럼 삭제
display(df)
df=df.drop([4,"D"],axis=1) # 다중 컬럼 삭제 axis=1열 0은 행 "columns" , "index"도가능
display(df)
df=df.drop(4,axis=0) # 행 삭제
display(df)
df=df.drop([2,3],axis=0) # 다중 행 삭제
display(df)

# %% [markdown]
# 데이터 변경

# %%
df.loc[0][0] = 100 # label기준 (불일치시 index기준)
display(df)
df.loc[0]["B"] = 100
display(df)

df.iloc[1][1] = 100 # index 기준(불일치시 label 기준)변경
display(df)

df.iloc[1]["C"] = 100
display(df)

df.iloc[0][0:2] = [1,2] # 다중 데이터 변경
display(df)

df["C"] = [3,6]
display(df)

df["A"][0] = 1 # pandas에서 추천하는 방법
df["B"][0] = 2 # pandas에서 추천하는 방법
display(df)
df["C"] = [77,11]
display(df)


# %%
df = pd.DataFrame({"cluster":[1,1,2,1,2,3],"org":['a','a','h','c','d','w'],"time":[8,6,34,23,74,6]})
display(df)
df =  df.sort_values(["time"] ,ascending=[False]) # time기준으로 내림차순
display(df)
df = df.reset_index(drop=True) # index 정리
display(df)

# %% [markdown]
# 함수

# %%
df = pd.DataFrame({"cluster":[1,1,2,1,2,3],"org":['a','a','h','c','d','w'],"time":[8,6,34,23,74,6]})
df.describe() # 기초통계량
df.head(2) # 데이터 head부분만 보여줌
df.tail(2) # 데이터 tail만 보여줌
df.T # 행열을 바꿈
df.time # time 컬럼데이터
df[df.time<10] # time이 10 미만인 데이터




