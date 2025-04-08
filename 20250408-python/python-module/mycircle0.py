# 외부 클래스 사용
import math
pi = math.pi
xpos, ypos =0,0
def get_area(radius): #원의 면적계산
    return (pi *radius**2) # 원의 둘레
def get_peri(radius):
    return(2*pi*radius)
def set_pos(x,y): # 위치 지정
    global xpos,ypos
    xpos , ypos =x,y