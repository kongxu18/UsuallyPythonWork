# 画布
import cv2
import os,sys
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

CANVAS = None
CANVAS_HEIGHT = 720
CANVAS_WIDTH = 1260

BACKGROUND_HEIGHT = 720
BACKGROUND_WIDTH = 1260

# 读取图片的模式
IMREAD_COLOR = cv2.IMREAD_COLOR
IMREAD_GRAYSCALE = cv2.IMREAD_GRAYSCALE
IMREAD_UNCHANGED = cv2.IMREAD_UNCHANGED

FONTPATH = os.path.join(CURRENT_PATH,'msyhl.ttc')
FONT = cv2.FONT_HERSHEY_SIMPLEX

# cv2 字体 和汉子字体大小比例
SCALE_OF_CV2_SIMSUN = 32


class Colour:
    BLACK = (0, 0, 0)
    BLUE = (255, 0, 0)
    GREEN = (0, 255, 0)
    RED = (0, 0, 255)
    WHITE = (255, 255, 255)
