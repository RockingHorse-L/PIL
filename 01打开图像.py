"""
    找到图像位置（路径）
    打开
    显示
"""
import numpy as np
from PIL import Image

img = Image.open('test.jpeg')

print(img.size)
# 转换成 Numpy 数组
imgData = np.asarray(img)
# w, h, c = imgData.shape
# 显示一张图片
img.show()
print(imgData)