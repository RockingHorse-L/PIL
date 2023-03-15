from PIL import Image
img = Image.open(r"test.jpeg")
# 格式
print(img.format)
# 尺寸
print(img.size)
# 是否只读
print(img.readonly)
# 模式
print(img.mode)
# 显示一张图片
img.show()