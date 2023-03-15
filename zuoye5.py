from PIL import Image

img = Image.open('./bg_imgs/03.png')
size = img.size
# 切割
w = size[0] // 2
h = size[1] // 2
count = 0
print(w, h)
for i in range(2):
    for j in range(2):
        count += 1
        box = (w * j, h * i, w * (j + 1), h * (i + 1))
        image = img.crop(box)
        image.save(f'./crop_img/{count}.png')
        image.show()

#合并

