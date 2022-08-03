import cv2
from .settings import FONT

# 操作的画布的实例化对象
DrawLiving = None
CANVAS = getattr(DrawLiving, 'background', None)


def add_title(text, font_scale, thickness, anchor, font=None):
    font = FONT if not font else font
    text_size = cv2.getTextSize(text=text, fontFace=font, fontScale=font_scale, thickness=thickness)
    text_w, text_h, y_bottom = text_size[0][0], text_size[0][1], text_size[1]

    fun_word = getattr(DrawLiving, 'add_word', None)
    fun_word(word=text, anchor=anchor, size=font_scale, thickness=thickness, color=(0, 0, 0))

    fun_rectangle = getattr(DrawLiving, 'add_rectangle', None)

    # 矩形,定位2个对角点，左上到右下角
    left_up = anchor[0]-5, anchor[1] - text_h-5

    right_down = anchor[0] + text_w+5, anchor[1]+5
    fun_rectangle(anchor=(left_up, right_down), color=(0, 0, 0), thickness=1)



def add_rotation_angle_word(text,font_scale, thickness, anchor, font=None):
    ...