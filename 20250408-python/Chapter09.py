# 모듈과 패키지 Pypi
# 모듈: 라이버러리 vs 스크립트
# 라이브러리: 모듈안에 실행구문 없을때
# 스크립트: 모듈안에 실행구문이 있을때
# math 모듈 주요 함수 설명 pi,e,trunc,factorial,degrees,radians,cos,acos,pow,sqrt,log,log10

# 패키지를 만드는법
# 패키지 이름으로 폴더를 생성 해당폴더안에 __init__.py 이름의 빈 스크립트 파일 생성(3.3)이후 의무 아님
# 패키지 > 모듈 > 클래스 > 함수
import os
import sys
os.getcwd()
sys.path
sys.path.append(os.getcwd())
sys.path
sys.path.remove(os.getcwd())
sys.path
os.getcwd()
os.chdir('c:\\Users\main')

import os   # 폴더 만들기, 위치 바꾸기 같은 기능을 쓰려면 os가 필요해요
import sys  # 파이썬이 파일이나 모듈을 찾는 경로를 관리할 수 있어요

# 지금 내가 작업하고 있는 폴더가 어디인지 알려줘요
print("현재 작업 폴더:", os.getcwd())

# 파이썬이 지금 작업 중인 폴더도 모듈을 찾는 경로에 추가해요
sys.path.append(os.getcwd())
print("경로 추가 후:", sys.path)

# 다시 추가했던 경로를 빼요 (연습해보는 거예요!)
sys.path.remove(os.getcwd())
print("경로 제거 후:", sys.path)

# 작업 폴더를 바꿔볼게요 (C 드라이브 안에 있는 Users/main 폴더로 이동)
os.chdir(r"C:\Users\main")
print("작업 폴더 변경됨:", os.getcwd())

# 새로운 폴더를 만들 경로를 준비해요 (예: MyFolder/SubFolder)
new_folder = os.path.join(os.getcwd(), "MyFolder", "SubFolder")

# 폴더를 실제로 만들어줘요! 중간 폴더도 없으면 같이 만들어줍니다.
os.makedirs(new_folder, exist_ok=True)  # 이미 있으면 에러 없이 그냥 넘어감

print("새 폴더가 만들어졌어요:", new_folder)

# 새로 만든 폴더 안에 hello.txt라는 파일을 만들고 글을 써볼게요
file_path = os.path.join(new_folder, "hello.txt")
with open(file_path, "w", encoding="utf-8") as f:
    f.write("이 파일은 파이썬으로 만든 거예요!\n자동으로 폴더도 만들었어요.")

print("파일도 만들었어요:", file_path)

