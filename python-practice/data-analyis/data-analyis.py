import pandas as pd
import os
import seaborn as sns

import matplotlib.pyplot as plt #import안됨 해결

dirName = "C:\VisualStudio-WorkSpace\PythonBasic\python-practice\data-analyis"
sae_jong_data = pd.read_csv(dirName+"\소상공인시장진흥공단_상가(상권)정보_세종_202412.csv")
print(sae_jong_data.isnull().sum())

# 중요하지 않은 컬럼 제거
# drop_cols = ['지점명', '표준산업분류코드', '표준산업분류명', '지번본번지', '지번부번지',
#              '건물부번지', '건물명', '건물관리번호', '구우편번호', '동정보', '층정보', '호정보']
# sae_jong_data_clean = sae_jong_data.drop(columns=drop_cols)

# # 혹시 남은 결측치는 한 번 더 확인
# print(sae_jong_data_clean.isnull().sum())

# 한글 깨짐 해결
# plt.rcParams['font.family'] ='Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] =False
# print(sae_jong_data['상권업종중분류명'].value_counts().head(10))

# # 시각화
# top10 = sae_jong_data['상권업종중분류명'].value_counts().head(10)
# top10.plot(kind='barh', figsize=(10,6), title='세종시 인기 업종 Top 10')
# plt.xlabel('점포 수')
# plt.ylabel('업종명')
# plt.gca().invert_yaxis()
# plt.grid()
# plt.tight_layout()
# plt.show()

# grouped = sae_jong_data.groupby(['행정동명', '상권업종중분류명']).size().reset_index(name='점포수')
# pivot_table = grouped.pivot(index='행정동명', columns='상권업종중분류명', values='점포수').fillna(0)
# print(pivot_table.head())

# plt.figure(figsize=(12, 8))
# sns.heatmap(pivot_table, cmap='Blues', annot=False)
# plt.title('세종시 행정동별 업종 분포 히트맵')
# plt.xlabel('업종')
# plt.ylabel('행정동')
# plt.tight_layout()
# plt.show()

# 폰트 설정 (한글 깨짐 방지)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# ▶ 예시용 데이터 준비 (너가 만든 걸로 바꿔도 됨)
# 업종 Top 10
top10 = sae_jong_data['상권업종중분류명'].value_counts().head(10)


# 행정동별 업종 분포 → 피벗 테이블
grouped = sae_jong_data.groupby(['행정동명', '상권업종중분류명']).size().reset_index(name='점포수')
pivot_table = grouped.pivot(index='행정동명', columns='상권업종중분류명', values='점포수').fillna(0)


# 업종 전체 평균보다 점포 수가 적은 업종 → 기회로 간주
industry_mean = pivot_table.mean()
recommend = pivot_table.apply(lambda row: industry_mean[industry_mean > row].index.tolist(), axis=1)

# 각 행정동마다 창업 유망 업종 리스트
for dong, items in recommend.items():
    print(f'📍 {dong} 창업 추천 업종: {", ".join(items[:3])}')

# 업종/행정동 상위만 추출 (너무 많으면 글씨 깨짐)
top10_cols = top10.index
top10_rows = pivot_table.sum(axis=1).sort_values(ascending=False).head(10).index
reduced = pivot_table.loc[top10_rows, top10_cols]

# ▶ 시각화: 하나의 화면에 side-by-side 배치
fig, axes = plt.subplots(1, 2, figsize=(18, 6))

# ▶ 바 차트 (왼쪽)
top10.plot(kind='barh', ax=axes[0], color='skyblue')
axes[0].set_title('세종시 인기 업종 Top 10')
axes[0].set_xlabel('점포 수')
axes[0].invert_yaxis()
axes[0].grid(True)

# ▶ 히트맵 (오른쪽)
sns.heatmap(reduced, cmap='Blues', annot=True, fmt='.0f', ax=axes[1])
axes[1].set_title('행정동 vs 업종 히트맵')
axes[1].set_xlabel('업종')
axes[1].set_ylabel('행정동')

plt.tight_layout()
plt.show()
