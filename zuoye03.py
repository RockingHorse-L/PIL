"""
    分析:
        先取出文件里的信息
            按照空格进行分裂
            再读取列表里的元素
        把dataInfo[0]添加到字典的图片里，并采用字典里的坐标
"""
import json

from PIL import Image


file = open('labels.txt', 'r', encoding='utf-8')
fileInfo = file.readlines()
datasInfo = []
# 读取文件里的信息保存为列表
for info in fileInfo:
    # print(type(info))
    dataInfo = info.strip().split('\t')
    datasInfo.append(dataInfo)
# print(datasInfo)
# 读取小黄人图片
# ['01.png', '[{"img": "01.png", "point": [100, 120, 200, 220] }]']
# ['02.png', '[{"img": "02.png", "point": [150, 100, 250, 200] }]']
# ['03.png', '[{"img": "03.png", "point": [120, 200, 220, 300] }]']
# ['04.png', '[{"img": "04.png", "point": [130, 100, 230, 200] }]']
# ['05.png', '[{"img": "05.png", "point": [110, 200, 210, 300] }]']
# ['06.png', '[{"img": "06.png", "point": [100, 110, 200, 210] }]']
for data in datasInfo:
    # print(data)
    img_copy = Image.open(f'./xhr_imgs/{data[0]}')
    img_copy_new = img_copy.resize((100, 100))
    datas = json.loads(data[1])
    imgDic = datas[0]
    # 读取字典里的图片和坐标
    img = imgDic['img']
    point = imgDic['point']
    image = Image.open(f'./bg_imgs/{img}')
    image.paste(img_copy_new, box=point)
    image.show()
file.close()
