# numbers = [1, 2, 2, 3, 0, 4, 5]

# answer = []
# duplicateCnt = 0
# for i in range(numbers):
#     answer.append(numbers(i))
#     if answer(i) == numbers(i):
#         duplicateCnt +=1
#         if duplicateCnt>1:
#             continue
from collections import Counter

input1 = "Hello, I hope you're having a lovely day"
input1 = list(input1)
input1 = " ".join(input1).split()
counter1 = dict(Counter(input1))
dict1 = dict(sorted(counter1.items(), key=lambda x:x[1]))
dict1 =dict(filter(lambda elem: elem[1]>3, dict1.items()))

dict1 = list(dict1.items())

print(dict1[0])