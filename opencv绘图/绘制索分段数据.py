import cv2 as cv
import numpy as np
import os
import base64
import openpyxl
import os
import math


def small(img, per):
    height, width = img.shape[:2]
    reSize = cv.resize(img, (int(width / per), int(height / per)),
                       interpolation=cv.INTER_AREA)
    return reSize


class CRect:
    def __init__(self, l, t, w, h):
        self.l = l
        self.r = l + w
        self.t = t
        self.b = t + h
        self.w = w
        self.h = h


class LabelLine(object):
    def __init__(self, img, pt1, pt2, color=(0, 0, 255)):
        self.img = img
        self.pt1 = pt1
        self.pt2 = pt2
        self.color = color
        self.line()

    def line(self):
        cv.line(self.img, self.pt1, self.pt2, self.color, 1)


def drawItem(canvas, pRect, pItem):
    canvas[pRect.t:pRect.b, pRect.l:pRect.r] = pItem


def drawLink(canvas, percent, isLeft):
    drawX = int(leftLockCenter[0] + percent * (rightLockCenter[0] - leftLockCenter[0]))
    drawRect = CRect(drawX - linkWidth // 2, leftLockCenter[1] - linkHeight // 2, linkWidth, linkHeight)
    drawItem(canvas, drawRect, linker_Limg if not isLeft else linker_Rimg)


def draw索夹(canvas, percent, color=(0, 0, 255)):
    drawX = int(leftLockCenter[0] + percent * (rightLockCenter[0] - leftLockCenter[0]))
    cv.circle(canvas, (drawX, leftLockCenter[1]), 6, color, -1)  # 圆，-1为向内填充
    cv.line(canvas, (drawX, leftLockCenter[1]), (drawX, leftLockCenter[1] - 20), color, 1)


defaultFont = cv.FONT_HERSHEY_SIMPLEX


def drawTextOn(canvas, text, drawX, drawY, color=(1), fontSize=0.5):
    t_size = cv.getTextSize(text, defaultFont, fontSize, thickness=1)[0]
    cv.putText(canvas, text, (drawX - t_size[0] // 2, drawY - t_size[1] // 2), defaultFont, fontSize, color, 1,
               cv.LINE_AA)


def getLineLocFromPercent(xPercent):
    return int(leftLockCenter[0] + xPercent * (rightLockCenter[0] - leftLockCenter[0]))


def drawRectangle(img, pt1, pt2, color=(1,)):
    cv.rectangle(img, pt1, pt2, color, 1)


canvas_height = 250
canvas_width = 1200
imgScale = 5
# 读取锁头
lockimg = cv.imread(r'lockhead.png')
temHeight, temWidth = lockimg.shape[:2]
lock_cx = 93.0 / temWidth
lock_cy = 158.0 / temHeight

lockimg_l = small(lockimg, imgScale)
row, col = lockimg_l.shape[:2]
leftLockRect = CRect(10, (canvas_height - row) // 2, col, row)
leftLockCenter = (int(leftLockRect.l + lock_cx * leftLockRect.w), int(leftLockRect.t + lock_cy * leftLockRect.h))

# 对锁头进行矩阵翻转
lockimg_r = np.flip(lockimg_l, axis=1)
rightLockRect = CRect(canvas_width - 10 - leftLockRect.w, leftLockRect.t, col, row)
rightLockCenter = (
    int(rightLockRect.l + (1 - lock_cx) * rightLockRect.w), int(rightLockRect.t + (1 - lock_cy) * rightLockRect.h))
# 读取链条
linker = cv.imread(r'linker_left2.png')
linker_Limg = small(linker, 7)
linkHeight, linkWidth = linker_Limg.shape[:2]
linker_Rimg = np.flip(linker_Limg, axis=1)

centerX = getLineLocFromPercent(0.5)
centerY = leftLockRect.t + (leftLockRect.b - leftLockRect.t) // 2


def china(img, word='hello', x=100, y=0):
    from PIL import Image, ImageDraw, ImageFont

    # cv2读取图片
    cv2img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
    pilimg = Image.fromarray(cv2img)

    # PIL图片上打印汉字
    draw = ImageDraw.Draw(pilimg)  # 图片上打印
    font = ImageFont.truetype("SimSun.ttf", 20, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
    # weight, height = draw.textsize(text='"Hi,我是诗shi"', font=font, spacing=4)
    draw.text((x, y), word, (0, 0, 0), font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体

    # PIL图片转cv2 图片
    cv2charimg = cv.cvtColor(np.array(pilimg), cv.COLOR_RGB2BGR)
    # cv2.imshow("图片", cv2charimg) # 汉字窗口标题显示乱码
    return cv2charimg


def 绘制索段(索段数据):
    # 画布
    canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)
    canvas[canvas == 0] = 255

    # 绘制文字

    cv.line(canvas, (0, 0), (canvas_width, 0), (0), 1)
    cv.line(canvas, (0, 0), (0, canvas_height), (0), 1)
    cv.line(canvas, (canvas_width - 1, 0), (canvas_width - 1, canvas_height), (0), 1)
    cv.line(canvas, (0, canvas_height - 1), (canvas_width, canvas_height - 1), (0), 1)

    cv.line(canvas, leftLockCenter, rightLockCenter, (0), 1)
    if 索段数据['段序号'] == 1:
        drawItem(canvas, leftLockRect, lockimg_l)
        drawTextOn(canvas, 'B', 20, centerY + 10, (0, 0, 255))
    else:
        drawLink(canvas, 0.02, True)
        drawX = getLineLocFromPercent(0.02)
        drawTextOn(canvas, 'B', 50, centerY + 10, (0, 0, 255))
    if 索段数据['段序号'] == 索段数据['段总数']:
        drawItem(canvas, rightLockRect, lockimg_r)
        drawTextOn(canvas, 'T', canvas_width - 20, centerY + 10, (0, 0, 255))
    else:
        drawLink(canvas, 1 - 0.02, False)
        drawX = getLineLocFromPercent(1 - 0.02)
        drawTextOn(canvas, 'T', canvas_width - 50, centerY + 10, (0, 0, 255))

    索段编号 = 索段数据['编号']
    索预张拉长度 = 索段数据['预张拉长度']
    # drawTextOn(canvas, 索段编号+'oo', getLineLocFromPercent(0.5), 50)
    prepercent = 0
    segIndex = 0
    segdata_arr = 索段数据['segdata_arr']
    segCount = len(segdata_arr)
    perSegPercent = 1 / segCount

    # if 分段序号 < len(分段data_arr):
    #     percent = (segIndex + len(segdata_arr)) * perSegPercent
    #     drawLink(canvas, percent)
    #     drawX = getLineLocFromPercent(percent)
    #     drawTextOn(canvas, 'T', drawX - 20, centerY + 10, (0, 0, 255))
    #     drawTextOn(canvas, 'B', drawX + 20, centerY + 10, (0, 0, 255))
    分段startP = 0
    RectangleXY = []
    Rectangle_num = []
    for segdata_i, segdata in enumerate(segdata_arr):

        if segdata_i == 0:
            分段startP = segIndex * perSegPercent
        segIndex += 1
        percent = segIndex * perSegPercent

        if segdata_i < len(segdata_arr) - 1:
            draw索夹(canvas, percent, (255, 0, 0) if segdata['是束索交点'] else (0, 0, 255))

            RectangleX = int(leftLockCenter[0] + percent * (rightLockCenter[0] - leftLockCenter[0]))
            RectangleY = leftLockCenter[1]

            RectangleXY.append((RectangleX, RectangleY))

        Rectangle_num.append(round(segdata['预张拉长度']))
        drawX = getLineLocFromPercent(prepercent + (percent - prepercent) * 0.5)

        drawTextOn(canvas, 'qw%d' % (round(segdata['预张拉长度'])), drawX, centerY + 40, 0.3)
        prepercent = percent

    def array_plus(array_input):
        plus_plus = []
        m = 0
        for i in range(len(array_input) - 1):
            m += array_input[i]
            plus_plus.append(m)
        return plus_plus

    Rectangle_arr = array_plus(Rectangle_num)
    print(Rectangle_num)
    print(Rectangle_arr)
    print(RectangleXY, '-----')
    for i in range(len(Rectangle_arr)):
        drawTextOn(canvas, '%d' % Rectangle_arr[i], RectangleXY[i][0], RectangleXY[i][1] - 19)

        drawRectangle(canvas, (RectangleXY[i][0] - 20, RectangleXY[i][1] - 40),
                      (RectangleXY[i][0] + 20, RectangleXY[i][1] - 19), (0, 0, 255))

    canvas = china(canvas, '数值为预张拉状态下索夹距离', 50, 50)
    savePath = os.path.join(r'suoimg', '%s.jpg' % (索段编号))
    cv.imwrite(savePath, canvas)
    return savePath
