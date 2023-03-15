from PIL import Image

img = Image.open('./bg_imgs/03.png')
# 获取图片size
size = img.size
# 切割
w = size[0] // 3
h = size[1] // 3
print(w, h)
for i in range(3):
    for j in range(3):
        box = (w * j, h * i, w * (j + 1), h * (i + 1))
        image = img.crop(box)
        image.show()
