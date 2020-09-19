from PIL import Image
img = Image.open('C:\\Users\\Administrator\\Desktop\\girl2.jpg')
# img.show()
# w, h = img.size
# print(w, h)
# img.thumbnail(size=(w/2,h/2),resample=Image.BICUBIC)
# img.show()
# print(img.size)
# img.save('C:\\Users\\Administrator\\Desktop\\girl3.jpeg','jpeg')
new_img = Image.new('RGB',(1400,600),(0,0,255))
# new_img.show()
img = img.crop((50,50,400,400))
new_img.paste(img,(0,0))
new_img.show()

with open("text.txt", "w+") as f:
    f.write("0123456789abcdef")
    f.seek(9)
    print(f.tell()) # 9 (pointermoves to 9, next read starts from 9)
    print(f.read()) # 9abcdef