from PIL import Image

img = Image.open('jige.jpg')
r, g, b = img.split()
img_new = Image.merge("RGB", (g, r, b))
# r.show()
# g.show()
# b.show()
img_new.show()