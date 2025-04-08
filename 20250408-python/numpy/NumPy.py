import numpy
# csv_data = numpy.loadtxt('./data.csv', delimiter=',')
# print(csv_data[0][0])
# print(csv_data)

# 데이터 사이언스를 위한 패키지 sympy,scipy,pandas, matploblib,saaborn tensorflow,keras

import pandas
csv_data = pandas.read_csv('data.csv',header=0)
# print(csv_data[0][0])
# 전체 데이터 출력
print("전체 데이터:\n", csv_data)