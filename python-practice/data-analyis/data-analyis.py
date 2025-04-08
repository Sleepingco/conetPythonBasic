import pandas as pd
import os
import seaborn as sns

import matplotlib.pyplot as plt #import안됨

dirName = "C:\VisualStudio-WorkSpace\PythonBasic\python-practice\data-analyis"
sae_jong_data = pd.read_csv(dirName+"\소상공인시장진흥공단_상가(상권)정보_세종_202412.csv")
print(sae_jong_data.isnull().sum())

# 중요하지 않은 컬럼 제거
# drop_cols = ['지점명', '표준산업분류코드', '표준산업분류명', '지번본번지', '지번부번지',
#              '건물부번지', '건물명', '건물관리번호', '구우편번호', '동정보', '층정보', '호정보']
# sae_jong_data_clean = sae_jong_data.drop(columns=drop_cols)

# # 혹시 남은 결측치는 한 번 더 확인
# print(sae_jong_data_clean.isnull().sum())

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False
print(sae_jong_data['상권업종중분류명'].value_counts().head(10))
# 시각화
top10 = sae_jong_data['상권업종중분류명'].value_counts().head(20)
top10.plot(kind='barh', figsize=(10,6), title='세종시 인기 업종 Top 10')
plt.xlabel('점포 수')
plt.ylabel('업종명')
plt.gca().invert_yaxis()
plt.grid()
plt.tight_layout()
plt.show()
# 한글 깨짐
grouped = sae_jong_data.groupby(['행정동명', '상권업종중분류명']).size().reset_index(name='점포수')
pivot_table = grouped.pivot(index='행정동명', columns='상권업종중분류명', values='점포수').fillna(0)
print(pivot_table.head())

plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, cmap='Blues', annot=False)
plt.title('세종시 행정동별 업종 분포 히트맵')
plt.xlabel('업종')
plt.ylabel('행정동')
plt.tight_layout()
plt.show()