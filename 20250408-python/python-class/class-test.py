# class 반복되는 변수 ,메소드(함수)를 미리 정하여 만들어 놓은 설계도
# 객체는 독립 즉 다른 객체의 변화가 다른 객체에 영향을 안줌
# 객체와 인스턴스의 차이:
# a = cookie() a는 객체 a는 cookie 인스턴스 객체이다
# 각 메소드의 첫번째 인수를 관례적으로 self라고 명시
# self는 메소드를 호출하는 자기자신을 뜻함
class User:
    phoneNumber = ''
    emailAddress = ''
    name = ''

    # 초기 initalize 함수 => 생성자 constructor
    def __init__(self, phoneNumber,emailAddress,name):
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.name = name
    def getPhoneNumber(self):
        return self.phoneNumber
    def getEmail(self):
        return self.emailAddress
    def getName(self):
        return self.name

# 객체 생성
user1 = User('010-1234-1234','papap@boe.com','kim')
print(user1.getPhoneNumber())
print(user1.getEmail())
print(user1.getName())

class Caculator: # 클래스 정의
    def __init__(self): #초기자
        self.result = 0
    def add(self,num): # 매서드
        self.result += num
        return self.result
cal1 = Caculator() # 둘은 같은 클래스지만 다른 인스턴스여서 결과값이 다름
cal2 = Caculator()
print(cal1.add(3)) # 3
print(cal1.add(4)) # 7
print(cal2.add(3)) # 3
print(cal2.add(7)) # 10