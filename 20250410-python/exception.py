# 예외처리

# # systaxerror
# def hanoi(n,start,end,temp):
#     if n =1:
#         mylist.append(start+'->'+end)
# # filenotfound
# myfile = open('samples.txt','r')
# # ArithmeticError,EOFError,Exception,FileExistsError,FileNotFoundError,ImportError,IndentationError,IndexError,KeyError,ModuleNotFoundError,NameError,OSError,SyntaxError
# # TypeError,ValueError,Warning,ZeroDivisionErrors
# # ZeroDivisionError
# 230 *2/(32-4*8)

# # Name Error
# mylist = [1,2,3]
# my_list
# # IndexError
# mylist[3]
days = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
date = True
while date:
    try:
        date = input('insert (mm dd)')
        mm, dd = date.split()
        mm, dd = int(mm),int(dd)
        if mm < 1 or mm > 12 : # 범위 오류시 ValueError 발생
            raise ValueError('월은 1에서 12 까 지 ')
        if dd < 1 or dd > days[mm-1]: # 범위 오류시 ValueError 발생
            raise ValueError('일은 1에서 %d 까 지 '%days[mm-1])
    except ValueError as e:
        print("insert error",e)
    else :
        print("%dm %dd"%(mm,dd))