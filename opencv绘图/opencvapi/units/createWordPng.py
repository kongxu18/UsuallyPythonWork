import numpy as np
import cv2
import math
from PIL import Image, ImageDraw, ImageFont
# 先判断文字大小
# size = cv2.getTextSize('hello world!', cv2.FONT_HERSHEY_SIMPLEX, 0.8, 1)
size = cv2.getTextSize('HHH', cv2.FONT_HERSHEY_SIMPLEX, 1, 1)
print(size)
width, height = size[0]
# 制作一个整除的画布,其实需要算对角线
radius = int(math.sqrt(math.pow(width // 2, 2) + math.pow(height // 2, 2)))
canvas_width, canvas_height = radius * 2 + 9, radius * 2 + 9

# center
x_center, y_center = canvas_width // 2 + 1 - width // 2, canvas_height // 2 + 1 + height // 2

# 旋转中心
trun_x, trun_y = canvas_width // 2 + 1, canvas_height // 2 + 1

img = np.zeros((canvas_height, canvas_width, 4), dtype=np.uint8)
# transparent_img[transparent_img == 0] = 255
# transparent_img[:, :, 3] = 0

cv2.putText(img, 'HHH', (x_center, y_center), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0, 255), 1)

cv2.line(img, (0, 0), (canvas_width, canvas_height), (0, 255, 0, 255))

m = cv2.getRotationMatrix2D((trun_x, trun_y), -45, 1)
dst = cv2.warpAffine(img, m, (canvas_width, canvas_height))

# 写入汉字
cv2img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)  # cv2和PIL中颜色的hex码的储存顺序不同
pill_img = Image.fromarray(cv2img)
handle = ImageDraw.Draw(pill_img)

china_font_obj = ImageFont.truetype('SimSun.ttf', 30,encoding='utf-8')

handle.text((0, 0), 'HHH',(0, 255, 33, 255) , font=china_font_obj)
# PIL图片转cv2 图片
res = cv2.cvtColor(np.array(pill_img), cv2.COLOR_RGB2BGR)

cv2.imshow('img', img)
cv2.imwrite('img.png', img)
cv2.imshow('img2', dst)
cv2.imwrite('img2.png', dst)

cv2.imshow('3',res)
cv2.waitKey(0)
