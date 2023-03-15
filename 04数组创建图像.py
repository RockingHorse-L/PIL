import numpy as np
from PIL import Image

#data = np.array([255, 255, 255], ndmin=3)
data = np.array([[[0, 0, 0]]], dtype='u1')

print(data.shape)
print(data.dtype)

# 将矩阵转为图像
img = Image.fromarray(data)
img.show()