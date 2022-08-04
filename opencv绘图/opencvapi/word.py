import cv2
from typing import List, Tuple, AnyStr
from PIL import Image, ImageDraw, ImageFont
from .settings import FONTPATH
import numpy as np
from .funs import coordinate_converter, create_word_background, wordPillow_center, bgr2rgba_converter
import copy


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
        self.offsetCenter = kwargs.get('offsetCenter')
        kwargs.pop('china', None)
        self.process_args(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        if kwargs.pop('revolve', False):
            return super().__new__(PngWord)
        elif kwargs.pop('china', False):
            """
            表示这个word 是中文
            """
            return super().__new__(ChinaWord)
        return super().__new__(cls)

    def process_args(self, *args, **kwargs):
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
        if not self.offsetCenter:
            self.offsetCenter = False

    def add(self):
        res = self.canvas
        if hasattr(self, 'canvas'):
            """
            这里已经把画布传入
            """
            try:
                anchor = coordinate_converter(anchor=self.anchor, canvas=self.canvas, offsetCenter=self.offsetCenter)
                res = cv2.putText(self.canvas, text=self.word, org=anchor, fontFace=self.font,
                                  fontScale=self.size, color=self.color, thickness=self.thickness,
                                  lineType=cv2.LINE_AA, bottomLeftOrigin=self.bottomLeftOrigin)
            except Exception as err:
                print('绘制箭头直线参数错误', err)
        return res


class ChinaWord(Word):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.process_args(*args, **kwargs)
        self.font = FONTPATH if not kwargs.get('font') else kwargs.get('font')

    @staticmethod
    def put_china(canvas, word, anchor, size, font, color):
        # cv2读取图片
        cv2img = cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
        pill_img = Image.fromarray(cv2img)
        handle = ImageDraw.Draw(pill_img)
        china_font_obj = ImageFont.truetype(font, size, encoding='utf-8')
        handle.text(anchor, word, color, font=china_font_obj)
        # PIL图片转cv2 图片
        res = cv2.cvtColor(np.array(pill_img), cv2.COLOR_RGB2BGR)
        return res

    def add(self):
        # 中文对add 方法进行重写
        res = self.canvas
        if hasattr(self, 'canvas'):
            try:
                anchor = coordinate_converter(anchor=self.anchor, canvas=self.canvas, offsetCenter=self.offsetCenter)
                res = self.put_china(self.canvas, self.word, anchor, self.size, self.font, self.color)
            except Exception as err:
                print('绘制文字参数错误', err)
        return res


class PngWord(ChinaWord):
    """
    原生的方法并不能旋转字符，这里对word类进行包装重写
    生成背景透明的文字图片，旋转后再与 原生图片矩阵指定位置 值进行替换，即覆盖原图片
    原理：三维矩阵替换
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.revolve = kwargs.get('revolve') if kwargs.get('revolve') else 0
        print('revolve', self.revolve)

    def write_words(self):
        color = bgr2rgba_converter(self.color)
        # 中文字体对象
        china_fontObj = ImageFont.truetype(FONTPATH, size=self.size, encoding='utf-8')
        size = china_fontObj.getsize(self.word)

        word_width, word_height = size
        background, self.canvas_height, self.canvas_width = create_word_background(word_width, word_height)

        # cv2 图片转成 pillow 图片对象
        # 写入汉字
        # cv2和PIL中颜色的hex码的储存顺序不同,保持4通道
        cv2img = cv2.cvtColor(background, cv2.COLOR_BGRA2RGBA)
        pill_img = Image.fromarray(cv2img)
        handle = ImageDraw.Draw(pill_img)
        anchor = wordPillow_center(self.canvas_height, self.canvas_width, word_width, word_height)
        handle.text(anchor, self.word, color, font=china_fontObj)
        # PIL图片转cv2 图片
        res = cv2.cvtColor(np.array(pill_img), cv2.COLOR_RGBA2BGRA)

        cv2.imshow('r', res)
        cv2.waitKey(0)
        return res

    def revolve_word(self):
        # 获取cv2 四通道矩阵
        img = self.write_words()
        # 旋转角度
        revolve = self.revolve
        # 旋转中心
        center_x, center_y = self.canvas_width // 2 + 1, self.canvas_height // 2 + 1
        # 旋转，构建旋转角度
        m = cv2.getRotationMatrix2D((center_x, center_y), revolve, 1)
        dst = cv2.warpAffine(img, m, (self.canvas_width, self.canvas_height))
        cv2.imwrite('ce.png', dst)
        return dst

    def overlay_img(self):
        """
        图片 插入
        """
        dst = self.revolve_word()

        # 判断 定位的方式，转换文字图片应该定位的坐标
        p_left_b = coordinate_converter(self.anchor, self.canvas, self.offsetCenter)
        # 为了避免麻烦 ，文字图片的左下角为 定位的点
        p_left_t = (p_left_b[0], p_left_b[1] - self.canvas_height)
        # p_right_b = (p_left_b[0]+self.canvas_width , p_left_b[1])
        # p_right_t = (p_left_b[0]+self.canvas_width,p_left_b[1]-self.canvas_height)

        # 对 3 维度矩阵进行遍历
        # word 构成的是一个正方形
        dst_len = dst.shape[0]
        print(dst_len)

        canvas = copy.deepcopy(self.canvas)

        # 遍历 word图片 ，只需要透明度 = 255 的
        for row in range(dst_len):
            for col in range(dst_len):
                color = dst[row, col]
                if color[3] !=0:
                    # 同时需要找到 原本图片 需要插入的位置坐标，同步遍历并替换
                    canvas[p_left_t[0] + row, p_left_t[1] + col] = color[:3]

        self.canvas = cv2.cvtColor(canvas,cv2.COLOR_BGR2BGRA)
        self.canvas[:dst_len,:dst_len] = dst

        return self.canvas

    def add(self):
        res = self.canvas
        if hasattr(self, 'canvas'):
            res = self.overlay_img()
        return res


if __name__ == '__main__':
    a = PngWord()
    print(a.font)
