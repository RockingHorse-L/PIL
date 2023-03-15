from PIL import Image
import os

img = Image.open('./bg_imgs/02.png')
im_crop1 = img.crop((0, 0, 829, 1108))
im_crop2 = img.crop((829, 0, 1659, 1108))
print(type(img.size))

im_crop1.show()
im_crop2.show()

# orDir = './bg_imgs'
# if not
# targetDir = './bg_bak_imgs'
# files = os.listdir(orDir)