# 다양한 이미지 포맷 지원, 내부픽셀 데이터를 엑세스 하여 다양한 이미지 처리기능을 제공
# 이미지 읽고 쓰기
# 자르기 등등
#
from PIL import Image,ImageTk,ImageFilter
import tkinter as tk
window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()
# 파일열기
img = Image.open('./20250410-python/Lenna.png')
# 45도 회전
out = img.rotate(45, expand=True)
# 블러처리
out = img.filter(ImageFilter.BLUR)
# 영상을 tkinter 형식으로 변환한다
tk_img = ImageTk.PhotoImage(out)
# 영상을 tkinter에서 화면에 표시
canvas.create_image(250,250,image=tk_img)
window.mainloop()

