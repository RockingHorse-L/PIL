from PIL import Image

img = Image.open('test.jpeg')
# 其中PNG是四通道RGBA模式,
image = img.convert('jpg')
img.save('yangdi.png')
