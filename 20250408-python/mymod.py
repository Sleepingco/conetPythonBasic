def mysum(a,b):
    return a+b
# print(mysum(3,7))

if __name__ == "__main__":
    print(mysum(3,7))

# 인터렉티브 모드 다른 폴더에서 엑세스
# import sys  
# >>> sys.path
# >>> sys.path.append('c:/doit')
# >>> from mymod import mysum
# >>> mysum(1,2)
# 3
# >>> import sys  
# >>> sys.path.append('c:/doit') 
# 10      # 3번줄 print문으로 인해 다른 함수를 호출 안해도 mysum이 프린트됨

# C:\>cd doit
# C:\doit>python mymod.py 
# 10