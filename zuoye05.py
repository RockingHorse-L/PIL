from PIL import Image
def handleImgMethod02():
    img = Image.open('./bg_imgs/03.png')
    size = img.size
    # 切割
    w = size[0] // 2
    h = size[1] // 2
    # count = 0
    # print(w, h)
    imgDic = {}
    for i in range(2):
        for j in range(2):
            # count += 1
            box = (w * j, h * i, w * (j + 1), h * (i + 1))
            # 存在字典
            image = img.crop(box)
            imgDic[box] = image
            # image.save(f'./crop_img/{count}.png')
            image.show()
    print(imgDic)

    #合并
    bgImg = Image.new(mode="RGB", size=(size[0], size[1]))
    for box, img in imgDic.items():
        bgImg.paste(img, box=box)
    bgImg.show()

handleImgMethod02()