"""
정사각형의 속성을 계산하는 모듈
get_area(length)
"""
xpos,ypos=0,0
def get_area(length):
    """
    한변의 길이가 lenght인 정사각형의 면적을 계산
    """
    return length**2
def get_peri(lenght):
    """
    한변의 길이가 length인 정사각형의 둘레를 계산
    """
    return lenght*4