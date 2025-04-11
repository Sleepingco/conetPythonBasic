import pandas as pd
import os
import seaborn as sns
import streamlit as st

import matplotlib.pyplot as plt #import안됨 해결 pip 인스톨

import folium
from streamlit_folium import st_folium

dirName = "C:\VisualStudio-WorkSpace\PythonBasic\python-practice\data-analyis"
sae_jong_data = pd.read_csv(dirName+"\소상공인시장진흥공단_상가(상권)정보_세종_202412.csv")
print(sae_jong_data.isnull().sum())

# 중요하지 않은 컬럼 제거
# drop_cols = ['지점명', '표준산업분류코드', '표준산업분류명', '지번본번지', '지번부번지',
#              '건물부번지', '건물명', '건물관리번호', '구우편번호', '동정보', '층정보', '호정보']
# sae_jong_data_clean = sae_jong_data.drop(columns=drop_cols)

# # 혹시 남은 결측치는 한 번 더 확인
# print(sae_jong_data_clean.isnull().sum())

# 폰트 설정 (한글 깨짐 방지)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# ▶ 예시용 데이터 준비
# 업종 Top 10
top10 = sae_jong_data['상권업종중분류명'].value_counts().head(10)


# 행정동별 업종 분포 → 피벗 테이블
grouped = sae_jong_data.groupby(['행정동명', '상권업종중분류명']).size().reset_index(name='점포수')
pivot_table = grouped.pivot(index='행정동명', columns='상권업종중분류명', values='점포수').fillna(0)


# 업종 전체 평균보다 점포 수가 적은 업종 → 기회로 간주 기존 추천 알고리즘이 너무 단순함 개선 필요
# industry_mean = pivot_table.mean()
# recommend = pivot_table.apply(lambda row: industry_mean[industry_mean > row].index.tolist(), axis=1)

# 전체 업종 순위 (세종시 전체 기준)
top_industries = sae_jong_data['상권업종중분류명'].value_counts().head(20).index
industry_mean = pivot_table.mean()
# 추천: 인기 업종 중에서 해당 동네에 적은 것만 필터링
recommend = pivot_table.apply(
    lambda row: [ind for ind in top_industries if row[ind] < industry_mean[ind]],
    axis=1
)

# 각 행정동마다 창업 유망 업종 리스트
for dong, items in recommend.items():
    print(f'📍 {dong} 창업 추천 업종: {", ".join(items[:3])}')

# 업종/행정동 상위만 추출 (너무 많으면 글씨 깨짐)
top10_cols = top10.index
top10_rows = pivot_table.sum(axis=1).sort_values(ascending=False).head(10).index
reduced = pivot_table.loc[top10_rows, top10_cols]

# --- 지도 생성 ---
st.title('📍 세종시 창업 추천 지도')

# 지도 기본 위치: 세종시 중심
map_center = [36.5, 127.3]
m = folium.Map(location=map_center, zoom_start=12)

# 동별 중심 위경도 (샘플값 / 필요시 직접 입력)
dong_coords = {
    '한솔동': [36.5023, 127.2591],
    '새롬동': [36.4842, 127.2653],
    '나성동': [36.4875, 127.2594],
    '다정동': [36.4867, 127.2516],
    '도담동': [36.5287, 127.2611],
    '어진동': [36.5045, 127.2598],
    '해밀동': [36.5183, 127.2500],
    '아름동': [36.5052, 127.2658],
    '종촌동': [36.4956, 127.2578],
    '고운동': [36.4999, 127.2484],
    '보람동': [36.4800, 127.2890],
    '대평동': [36.4805, 127.2975],
    '소담동': [36.4870, 127.2895],
    '반곡동': [36.5110, 127.2890],
}


# 추천 업종 마커 추가
for dong, items in recommend.items():
    if dong in dong_coords:
        popup_text = f"<b>{dong}</b><br>추천 업종: {', '.join(items[:3])}"
        folium.Marker(
            location=dong_coords[dong],
            popup=folium.Popup(popup_text, max_width=300),
            tooltip=dong,
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)


# 지도 표시
st_folium(m, width=800, height=600)

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
st.title("세종시 창업 상권 분석 대시보드")
st.markdown("""
이 대시보드는 세종시 행정동별 상권 정보를 분석하여 인기 업종과 창업 추천 업종을 제공합니다.
- **왼쪽 그래프**: 세종시에서 가장 점포 수가 많은 업종 TOP 10
- **오른쪽 히트맵**: 각 동별로 업종 분포를 색상으로 표현
- **지도**: 추천 업종 정보를 마커로 표시
""")
# ✅ Streamlit에 표시
st.pyplot(fig)  # 👈 이렇게!

# streamlit run .\data-analyis.py