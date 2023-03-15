import numpy as np
from PIL import Image

img = Image.open("jige.jpg")
imgData = np.array(img,dtype=np.uint8)
print(img.size)

w, h = img.size
imgData[:20, :700] = [32, 37, 241]
imgData[:700, :20] = [32, 37, 241]
imgData[:, 700:] = [255, 0, 0]
imgData[700:, :] = [255, 0, 0]
img = Image.fromarray(imgData)
img.show()

