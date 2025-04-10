from PIL import Image,ImageFilter

img = Image.open('june.png') # 이미지 파일열기
print(img.format,img.size,img.mode) #format,size,mode 확인
img.show()

box = (76,3,156,183)
crop_img = img.crop(box)
crop_img.save('june_torch.png')
print(crop_img.format,crop_img.size,crop_img.mode)
crop_img.show()

# 첫번째 예제
img = Image.open('june.png')
box = box = (76,3,156,183)
crop_img1 = img.crop(box)

drop = (0,3,80,183)
img.paste(crop_img1,drop)

# 두번째 예제
img2 = Image.open('june.png')
crop_img2 = crop_img.resize((40,90))
crop_img2.save("40x90.png")
drop = (20,40,60,130)
img2.paste(crop_img2,drop)

box = (80,3,180,103)
crop_img3=img2.crop(box).rotate(90)
drop=(220,0,320,100)
img2.paste(crop_img3,drop)
img2.show()

img4 = Image.open('june.png')
box=(76,3,156,333)
crop4 = img4.crop(box)
crop_img4 = crop4.transpose(Image.FLIP_LEFT_RIGHT)
drop = (0,3,80,333)
img4.paste(crop_img4,drop)
img4 = img4.transpose(Image.FLIP_LEFT_RIGHT)
img4.save('june_04.png')
img4.show()

img5 = img.filter(ImageFilter.CONTOUR)
img5.save('june_contour.png')
img6=img.filter(ImageFilter.EMBOSS)
img6.save('june_emboss.png')
img7=img.filter(ImageFilter.SMOOTH_MORE)
img7.save('june_smooth_more.png')

rgb = img.split()
r,g,b = rgb[0],rgb[1],rgb[2]
img8=Image.merge("RGB",(b,b,g))
img8.save('june_bbg.png')
img9 = Image.merge('RGB',(b,r,g))
img9.save('june_brg.png')