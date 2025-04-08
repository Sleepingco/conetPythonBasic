# modl.py
def sum(a,b):
    return a+b
def safe_sum(a,b):
    if type(a) !=type(b):
        print("두수의 타입이 다릅니다")
    else: 
        result = sum(a,b)
        return result