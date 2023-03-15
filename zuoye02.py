"""
    分析:
        先读取图片的大小
        随机坐标

        再进行复制粘贴
"""
import random
from PIL import Image

# 读取图片
img_copy = Image.open('./xhr_bak_imgs/06.png')
img = Image.open('./bg_imgs/02.png')
# 读取图片的大小
imgSize = img.size
img_copySize = img_copy.size
# box = (random.randint(6))
# 左上角
x = random.randint(0, imgSize[0])
y = random.randint(0, imgSize[1])
# 右下角
x1 = x + img_copySize[0]
y1 = y + img_copySize[1]
if x1 <= imgSize[0] and y1 <= imgSize[1]:
    box = (x, y ,x1 ,y1)
print(box)
img.paste(img_copy, box=box)
img.show()
