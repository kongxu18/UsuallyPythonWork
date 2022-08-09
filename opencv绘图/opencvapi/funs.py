import math
import numpy as np
import cv2
from decimal import Decimal


def coordinate_converter(anchor: any, canvas, offsetCenter=False):
    """
    坐标点转换
    （0，0）cv2 图片左上角
     数据（0，0）为图片的中心点
    """
    # print(canvas.shape)
    width, height = canvas.shape[1], canvas.shape[0]

    x, y = int(Decimal(anchor[0]).quantize(0)), int(Decimal(anchor[1]).quantize(0))

    if offsetCenter:
        x_offset = int(Decimal(width // 2).quantize(0))
        y_offset = int(Decimal(height // 2).quantize(0))

        return x + x_offset, -y + y_offset
    return x, y


def wordPillow_offset(canvas_width, canvas_height, word_width, word_height, o_type, off=0):
    """
    pillow 文字定位在文字的左上角
    需要使得文字在背景图片自动居中显示
    计算出相对的中心点
    """
    if o_type == 'left':
        x_center, y_center = round_off(canvas_width / 2) + off, \
                             round_off(canvas_height / 2) - round_off(word_height / 2)

    elif o_type == 'right':

        x_center, y_center = round_off(canvas_width / 2) - word_width - off, \
                             round_off(canvas_height / 2) - round_off(word_height / 2)
    else:
        # center
        x_center, y_center = round_off(canvas_width / 2) - round_off(word_width / 2), \
                             round_off(canvas_height / 2) - round_off(word_height / 2)
    return x_center, y_center


def create_word_background(width, height):
    # 制作一个整除的画布,其实需要算对角线
    # 整体都是透明
    # cv2 最恶心的是 （0，0，0） 是黑色
    radius = int(math.sqrt(math.pow(width // 2, 2) + math.pow(height // 2, 2)))
    canvas_width, canvas_height = radius * 2 + 9, radius * 2 + 9
    background = np.zeros((canvas_height, canvas_width, 4), dtype=np.uint8)
    # background[background == 0] = 255
    # background[:, :, 3] = 0
    return background


def bgr2rgba_converter(color):
    """
    针对输入bgr的颜色进行改变，word 模块使用了不一样的rgb
    color : B G R
    return : R G B A
    """
    if len(color) == 3:
        return color[2], color[1], color[0], 255


def add_alpha_channel(img):
    """ 为jpg图像添加alpha通道 """

    b_channel, g_channel, r_channel = cv2.split(img)  # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255  # 创建Alpha通道
    img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))  # 融合通道
    return img_new


def round_off(num):
    """
    数学上的四舍五入
    """
    return int(Decimal(num).quantize(0))
