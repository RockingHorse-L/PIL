"""
    找到需要被缩放的图像目录
    orDir = xxxxx
    targetDir  xxxxx

    files = os.listdir()
    for file in files:


"""
import os
from PIL import Image
orDir = './xhr_imgs'
targetDir = './xhr_bak_imgs'
files = os.listdir(orDir)
for file in files:
    imgPath = orDir + '\\' + file
    targetDirPath = targetDir + '\\' + file
    img = Image.open(imgPath)
    image = img.resize((100, 100), box=(100, 100, 300, 300))
    image.show()
    image.save(targetDirPath)