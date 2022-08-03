import cv2
from typing import List, Tuple, AnyStr
from PIL import Image, ImageDraw, ImageFont
from .settings import FONTPATH
import numpy as np
from .base import Canvas
import matplotlib.pyplot as plt
from matplotlib import font_manager


class Word(object):
    def __init__(self, *args, **kwargs):
        self.canvas = None
        self.word: AnyStr = kwargs.get('word')
        self.anchor: Tuple[int] = kwargs.get('anchor')

        self.color: Tuple[int] = kwargs.get('color')

        # 图像数据圆点的位置，默认位于左上角。若参数选择True, 则原点位于左下角
        self.bottomLeftOrigin: bool = kwargs.get('bottomLeftOrigin')

        # 位置传参数,字体大小
        self.size: float = kwargs.get('size')
        # 字体粗细
        self.thickness: float = kwargs.get('thickness')
        self.font = kwargs.get('font')
        kwargs.pop('china', None)
        self._process_args(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        if kwargs.pop('china', False):
            """
            表示这个word 是中文
            """
            return super().__new__(ChinaWord)
        return super().__new__(cls)

    def _process_args(self, *args, **kwargs):
        if args:
            for arg in args:
                if isinstance(arg, tuple):
                    if len(arg) == 2:
                        self.anchor = arg
                    elif len(arg) == 3:
                        self.color = arg
                elif isinstance(arg, str):
                    self.word = arg
                elif isinstance(arg, bool):
                    self.bottomLeftOrigin = arg
        if not self.font:
            self.font = cv2.FONT_HERSHEY_SIMPLEX

    def add(self):
        res = self.canvas
        if hasattr(self, 'canvas'):
            """
            这里已经把画布传入
            """
            try:
                print(self.word, 'word')
                res = cv2.putText(self.canvas, text=self.word, org=self.anchor, fontFace=self.font,
                                  fontScale=self.size, color=self.color, thickness=self.thickness,
                                  lineType=cv2.LINE_AA, bottomLeftOrigin=self.bottomLeftOrigin)
            except Exception as err:
                print('绘制箭头直线参数错误', err)
        return res


class ChinaWord(Word):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font = FONTPATH if not kwargs.get('font') else kwargs.get('font')

    def add(self):
        # 中文对add 方法进行重写
        res = self.canvas
        if hasattr(self, 'canvas'):
            try:
                # cv2读取图片
                cv2img = cv2.cvtColor(self.canvas, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
                pill_img = Image.fromarray(cv2img)
                handle = ImageDraw.Draw(pill_img)
                font = ImageFont.truetype(self.font, self.size, encoding='utf-8')
                handle.text(self.anchor, self.word, self.color, font=font)
                # PIL图片转cv2 图片
                res = cv2.cvtColor(np.array(pill_img), cv2.COLOR_RGB2BGR)

            except Exception as err:

                print('绘制文字参数错误', err)
        return res

    # def __new__(cls, *args, **kwargs):


class PngWord(object):
    """
    原生的方法并不能旋转字符，这里对word类进行包装重写
    生成背景透明的文字图片，旋转后再与 原生图片矩阵指定位置 值进行替换，即覆盖原图片
    原理：三维矩阵替换
    """
