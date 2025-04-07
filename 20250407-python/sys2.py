import sys # 스크립트를 실행할때 인자를 받기위해 SYS 모듈이 필요
args =sys.argv[1:] # 실행인자는 sys.argv에 저장 되어 있음 첫인자는 스크립트 파일이름이며 그 이후부터가 전달된 인자이다
for i in args:
    print(i.upper(),end=' ')
# python .\sys2.py life is too short, you need python