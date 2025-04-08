# myrect0.py
xpos, ypos = 0,0
"""
사격형의 넓이 와 면적과 위치를 get,set을 할수있음
"""
__doc__

def get_area(width, height): # 사각형 면적 계산
    area = width * height
    return area

def get_peri(width, height): # 사각형 둘레 계산
    peri = 2 * (width +height)
    return peri
def set_pos(x,y): # 위치 지정
    global xpos, ypos
    xpos, ypos = x,y
def get_pos():
    return xpos ,ypos