from PIL import Image

img = Image.open('yangdi.png')
image = img.resize((100, 100))
image.show()