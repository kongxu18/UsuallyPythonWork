import math
import numpy as np


def coordinate_converter(anchor: any, canvas, offsetCenter=False):
    """
    坐标点转换
    （0，0）cv2 图片左上角
     数据（0，0）为图片的中心点
    """
    # print(canvas.shape)
    width, height = canvas.shape[1], canvas.shape[0]

    x, y = int(anchor[0]), int(anchor[1])
    if offsetCenter:
        x_offset = width // 2
        y_offset = height // 2

        return x + x_offset, -y + y_offset
    return x, y


def wordPillow_center(canvas_height, canvas_width, word_width, word_height):
    """
    pillow 文字定位在文字的左上角
    需要使得文字在背景图片自动居中显示
    计算出相对的中心点
    """
    # center
    x_center, y_center = canvas_width // 2 + 1 - word_width // 2, canvas_height // 2 + 1 - word_height // 2
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
    return background, canvas_width, canvas_height


def bgr2rgba_converter(color):
    """
    color : B G R
    return : R G B A
    """
    if len(color) == 3:
        return color[2], color[1], color[0], 255
