import test_package.say_hello, test_package.say_goodbye
from test_package import say_hello,say_goodbye
# 패키지 > 모듈 > 클래스 > 함수
test_package.say_hello.hello()
test_package.say_goodbye.goodbye()

import mod2
print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(mod2.sum(mod2.PI,4.4))

print('-------------------------------')
# c:/doit/mymod.py mtsum(3,4)
import sys
sys.path.append('c:/doit')
import mymod
print('mymod.mysum(3,4)',mymod.mysum(3,4))