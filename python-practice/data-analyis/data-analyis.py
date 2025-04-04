import pandas as pd
import os

dirName = "C:\VisualStudio-WorkSpace\PythonBasic\python-practice\data-analyis"
sae_jong_data = pd.read_csv(dirName+"\소상공인시장진흥공단_상가(상권)정보_세종_202412.csv")
print(sae_jong_data.isnull().sum())
# 중요하지 않은 컬럼 제거
drop_cols = ['지점명', '표준산업분류코드', '표준산업분류명', '지번본번지', '지번부번지',
             '건물부번지', '건물명', '건물관리번호', '구우편번호', '동정보', '층정보', '호정보']
sae_jong_data_clean = sae_jong_data.drop(columns=drop_cols)

# 혹시 남은 결측치는 한 번 더 확인
print(sae_jong_data_clean.isnull().sum())
