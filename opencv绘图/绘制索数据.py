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


class ArrowLine(LabelLine):
    def __init__(self, img, pt1, pt2):
        super().__init__(img, pt1, pt2)
        self.line()

    def line(self):
        # arrowedLine(img, pt1, pt2, color[, thickness[, line_type[, shift[, tipLength]]]])
        cv.arrowedLine(self.img, self.pt1, self.pt2, color=(1))


def drawItem(canvas, pRect, pItem):
    canvas[pRect.t:pRect.b, pRect.l:pRect.r] = pItem


def drawLink(canvas, percent):
    drawX = int(leftLockCenter[0] + percent * (rightLockCenter[0] - leftLockCenter[0]))
    drawRect = CRect(drawX - linkWidth // 2, leftLockCenter[1] - linkHeight // 2, linkWidth, linkHeight)
    drawItem(canvas, drawRect, linkerimg)

    def draw_label():
        left_vertical_line = LabelLine(canvas, leftLockCenter, (leftLockCenter[0], leftLockCenter[1] + 100))
        right_vertical_line = LabelLine(canvas, rightLockCenter, (rightLockCenter[0], rightLockCenter[1] + 100))

        center_vertical_line = LabelLine(canvas, (drawX, leftLockCenter[1]), (drawX, leftLockCenter[1] + 100))

        left_label = LabelLine(canvas, (leftLockCenter[0], leftLockCenter[1] + 80), (drawX, leftLockCenter[1] + 80))
        right_label = LabelLine(canvas, (drawX, leftLockCenter[1] + 80), (rightLockCenter[0], leftLockCenter[1] + 80))

    draw_label()


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
# linker = cv.cvtColor(linker,cv.C)
# print(lockimg[0][0])
# print(linker[0][0],print(linker.shape))
linkerimg = small(linker, 10)
linkHeight, linkWidth = linkerimg.shape[:2]

centerX = getLineLocFromPercent(0.5)
centerY = leftLockRect.t + (leftLockRect.b - leftLockRect.t) // 2


def china(img, word='hello', x=100, y=0,size=5,weight=2,rotation=0,color=(0,0,0)):
    import matplotlib.pyplot as plt
    w, h = img.shape[1], img.shape[0]
    dpi = 300

    # create a frameless mpl figure

    fig, axes = plt.subplots(figsize=(w / dpi, h / dpi), dpi=dpi)
    axes.axis('off')
    fig.subplots_adjust(bottom=0, top=1.0, left=0, right=1)
    axes.matshow(img)

    # set custom font
    import matplotlib.font_manager as fm
    ttf_fname = 'SimSun.ttf'
    prop = fm.FontProperties(fname=ttf_fname, size=size, weight=weight)

    # annotate something
    axes.annotate(word, xy=(x, y), rotation=rotation, fontproperties=prop, color=color)
    # plt.show()
    # get fig image data and read it back to numpy array
    fig.canvas.draw()

    Imvals = np.fromstring(fig.canvas.tostring_rgb(), dtype='uint8')
    ImArray = Imvals.reshape((h, w, 3))
    return ImArray


def 绘制索(索数据):
    # 画布
    canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

    canvas[canvas == 0] = 255

    # 绘制文字

    cv.line(canvas, (0, 0), (canvas_width, 0), (0), 1)
    cv.line(canvas, (0, 0), (0, canvas_height), (0), 1)
    cv.line(canvas, (canvas_width - 1, 0), (canvas_width - 1, canvas_height), (0), 1)
    cv.line(canvas, (0, canvas_height - 1), (canvas_width, canvas_height - 1), (0), 1)

    cv.line(canvas, leftLockCenter, rightLockCenter, (0), 1)
    drawItem(canvas, leftLockRect, lockimg_l)
    drawItem(canvas, rightLockRect, lockimg_r)

    drawTextOn(canvas, 'B', 20, centerY + 10, (0, 0, 255))
    drawTextOn(canvas, 'T', canvas_width - 20, centerY + 10, (0, 0, 255))

    索编号 = 索数据['编号']
    索预张拉长度 = 索数据['预张拉长度']
    drawTextOn(canvas, 索编号, getLineLocFromPercent(0.5), 50)
    分段data_arr = 索数据['分段data_arr']
    prepercent = 0
    束索交点_arr = 索数据.get('束索交点_arr')
    segCount = 0
    segIndex = 0
    seg累计len = 0
    for 分段data in 分段data_arr:
        segCount += len(分段data['segdata_arr'])
    perSegPercent = 1 / segCount
    for 分段data in 分段data_arr:
        分段序号 = 分段data['序号']
        分段预张拉长度 = 分段data['预张拉长度']
        segdata_arr = 分段data['segdata_arr']
        if 分段序号 < len(分段data_arr):
            percent = (segIndex + len(segdata_arr)) * perSegPercent
            drawLink(canvas, percent)
            drawX = getLineLocFromPercent(percent)
            drawTextOn(canvas, 'T', drawX - 20, centerY + 10, (0, 0, 255))
            drawTextOn(canvas, 'B', drawX + 20, centerY + 10, (0, 0, 255))
        分段startP = 0
        for segdata_i, segdata in enumerate(segdata_arr):
            if segdata_i == 0:
                分段startP = segIndex * perSegPercent
            segIndex += 1
            seg累计len += segdata['预张拉长度']
            percent = segIndex * perSegPercent

            if segdata_i < len(segdata_arr) - 1:
                b是束索交点 = False
                for 束索交点 in 束索交点_arr:
                    if abs(束索交点 - seg累计len) < 10:
                        b是束索交点 = True
                        break
                draw索夹(canvas, percent, (255, 0, 0) if b是束索交点 else (0, 0, 255))
            drawX = getLineLocFromPercent(prepercent + (percent - prepercent) * 0.5)
            drawTextOn(canvas, '%d' % (round(segdata['预张拉长度'])), drawX, centerY + 40, 0.3)
            prepercent = percent
        if len(分段data_arr) > 1:
            分段标识 = '%s%s' % (索编号, chr(64 + 分段序号))
            drawX = getLineLocFromPercent(分段startP + (percent - 分段startP) * 0.5)
            drawTextOn(canvas, 分段标识, drawX, centerY + 80)
            drawTextOn(canvas, '%.1f' % (分段data['预张拉长度']), drawX, centerY + 100, 0.3)

    # def ndarray2b64(img, format='rgb'):
    #     if format == 'rgb':
    #         _, enc = cv.imencode('.jpg', img)
    #     elif format == 'bgr':
    #         _, enc = cv.imencode('.jpg', img)
    #     b64 = base64.urlsafe_b64encode(enc.tobytes())
    #     return b64

    # enc = cv.imencode('.jpg', canvas)

    # img = openpyxl.drawing.image.Image(enc)
    # image_b64 = str(ndarray2b64(canvas), encoding='utf-8')
    # pd_canvas.iloc[51:448, 366:985] = pd_link

    # 为了演示，建窗口显示出来
    # cv.namedWindow('image', cv.WINDOW_NORMAL)
    # cv.resizeWindow('image', canvas_width, canvas_height)  # 定义frame的大小
    # cv.imshow('image', canvas)

    # cv.waitKey(0)
    # cv.destroyAllWindows()
    canvas = china(canvas, '数值为预张拉状态下索夹距离', 50, 50)
    savePath = os.path.join(r'suoimg', '%s.jpg' % (索编号))
    cv.imwrite(savePath, canvas)
    return savePath
