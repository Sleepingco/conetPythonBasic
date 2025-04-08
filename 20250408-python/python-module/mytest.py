# mycircle0
# myrect0

import mycircle0 as cir
import myrect0 as rec

from mycircle0 import get_area as circle_get_area
from mycircle0 import get_peri as circle_get_peri
from mycircle0 import set_pos as circle_set_pos

from myrect0 import get_area as rect_get_area
from myrect0 import get_peri as rect_get_peri
from myrect0 import set_pos as rect_set_pos
# 반지름이 5일 때의 면적, 둘레를 구하고 x, y 위치를 100,100으로 보냄
radius = 5
area = circle_get_area(radius)
peri = cir.get_peri(radius)
cir.set_pos(100,100)
print("반지름 5의 면적은 : ",area," 둘레는 ",peri)

# 너비가 3이고 높이가 4인 직사각형의 면적, 둘레를 구하고 x,y 위치를 200,200으로 설정하시오
width = 3
height = 4
rect_area = rec.get_area(3,4)
rect_peri =  rec.get_peri(3,4)
rec.set_pos(200,200)

rec_xpos, rec_ypos = rec.get_pos()
print("사각형의 넓이는", rect_area, "둘레는", rect_peri, "x는",rec_xpos," y는",rec_ypos)

import mysquare

square_area = mysquare.get_area(50)
print("한변의 길이가 50인 정사각형의 면적은 ",square_area)
print(mysquare.__doc__)
print(mysquare.get_area.__doc__)

import modl
from modl import *
from modl import sum,safe_sum as s,f
print(modl.sum(3,4))
print(modl.safe_sum(3,4))
print(modl.safe_sum(3,'a'))