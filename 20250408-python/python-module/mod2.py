# mod2.py
PI = 3.141582
class Math:
    def solv(self, r):
        return PI*(r**2) # 여기까지가 클래스 정의

def sum(a,b):
    return a+b

# 매인이기에 먼저 실행함 이건 **"이 파일이 직접 실행된 경우에만 이 코드 블록을 실행하라"**는 뜻
# 다른 모듈에서 import 하면 실행안된다
if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI,4.4))
