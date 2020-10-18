# pip install Pillow
# pip install pytesseract

import requests
import os
from PIL import Image
import pytesseract

print(os.path.abspath('.'))

# 打开图片
im = Image.open('./cap.jpg')
im.show()

# 灰度处理
gray = im.convert('L')
gray.save('./c_gray2.jpg')
im.close()

# 二值化
threshold = 100
table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

out = gray.point(table, '1')
out.save('c_th.jpg')

th = Image.open('c_th.jpg')
print(pytesseract.image_to_string(th, lang='chi_sim+eng'))