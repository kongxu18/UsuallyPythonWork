import cv2
from typing import List, Tuple, AnyStr
from PIL import Image, ImageDraw, ImageFont
from .settings import FONTPATH
import numpy as np
from .funs import coordinate_converter, create_word_background, \
    wordPillow_offset, bgr2rgba_converter, add_alpha_channel, round_off
import copy


class Word(object):
    def __init__(self, *args, **kwargs):
        self.canvas = None
        self.word: AnyStr = kwargs.get('word')
        self.anchor: Tuple[int] = kwargs.get('anchor')

        self.color: Tuple[int] = kwargs.get('color')

        # 位置传参数,字体大小
        self.size: float = kwargs.get('size')
        # 字体粗细
        self.thickness: float = kwargs.get('thickness')
        self.font = kwargs.get('font')
        self.offsetCenter = kwargs.get('offsetCenter')

        # 对齐方式 center left right
        self.alignment_type = kwargs.get('alignment_type')
        # 与锚点的直线距离
        self.alignment_spacing = kwargs.get('alignment_spacing')

        # 不对外使用参数
        self.word_width, self.word_height = None, None

        kwargs.pop('china', None)
        self.process_args(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        if kwargs.pop('revolve', False) or kwargs.pop('china', False):
            """
            表示这个word 是中文
            """
            return super().__new__(PngWord)
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
        if not self.font:
            self.font = cv2.FONT_HERSHEY_SIMPLEX
        if not self.offsetCenter:
            self.offsetCenter = False

    def get_word_size(self, *args):
        """
        这里是文字的size
        """
        size = cv2.getTextSize(self.word, self.font, self.size, self.thickness)
        try:
            self.word_width, self.word_height = size[0][0], size[0][1]
        except Exception as err:
            raise ValueError('不可识别文字错误：', err)
        return self.word_width, self.word_height

    def alignment(self):
        if not self.alignment_type:
            self.alignment_type = 'center'
        if not self.alignment_spacing:
            self.alignment_spacing = 7

        # 得到文字的长度和宽度并赋值操作
        word_width, word_height = self.get_word_size()

        # 针对写文字的布局，跟定的anchor 默认为文字的中心点
        # left ：文字左边界
        # right：文字右边界
        anchor = coordinate_converter(anchor=self.anchor, canvas=self.canvas, offsetCenter=self.offsetCenter)
        if self.alignment_type == 'center':
            # 计算应该绘制文字的坐标
            try:
                anchor = anchor[0] - round_off(word_width / 2), anchor[1] + round_off(word_height / 2)
                return anchor
            except Exception as err:
                raise ValueError('给定的坐标无法修正:', err)
        elif self.alignment_type == 'left':
            # 计算应该绘制文字的坐标
            try:
                anchor = anchor[0] + self.alignment_spacing, anchor[1] + round_off(word_height / 2)
                return anchor
            except Exception as err:
                raise ValueError('给定的坐标无法修正:', err)
        elif self.alignment_type == 'right':
            # 计算应该绘制文字的坐标
            try:
                anchor = anchor[0] - self.alignment_spacing - word_width, \
                         anchor[1] + round_off(word_height / 2)
                return anchor
            except Exception as err:
                raise ValueError('给定的坐标无法修正:', err)
        else:
            raise ValueError('alignment_type 不是期望的值')

    def add(self):
        res = self.canvas
        if hasattr(self, 'canvas'):
            """
            这里已经把画布传入
            """
            try:
                anchor = self.alignment()

                res = cv2.putText(self.canvas, text=self.word, org=anchor, fontFace=self.font,
                                  fontScale=self.size, color=self.color, thickness=self.thickness,
                                  lineType=cv2.LINE_AA, bottomLeftOrigin=False)
            except Exception as err:
                print('Word 绘制错误', err)
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
        china_fontObj = ImageFont.truetype(font, size, encoding='utf-8')

        size = china_fontObj.getsize(word)
        word_width, word_height = size
        anchor = anchor[0] - (word_width // 2), anchor[1] - (word_height // 2)
        handle.text(anchor, word, color, font=china_fontObj)
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
        self.color = bgr2rgba_converter(self.color)
        self.background = None

    def get_word_size(self, *args):
        # 中文字体对象
        self.font = ImageFont.truetype(FONTPATH, size=self.size, encoding='utf-8')
        size = self.font.getsize(self.word)
        try:
            self.word_width, self.word_height = size
        except Exception as err:
            raise ValueError('不可识别文字错误：', err)
        return self.word_width, self.word_height

    def alignment(self):
        if not self.alignment_type:
            self.alignment_type = 'center'
        if not self.alignment_spacing:
            self.alignment_spacing = 7

        # left ：文字左边界
        # right：文字右边界
        # anchor = coordinate_converter(anchor=self.anchor, canvas=self.canvas, offsetCenter=self.offsetCenter)
        word_width, word_height = self.get_word_size()
        background = create_word_background((word_width + self.alignment_spacing) * 2, word_height)
        self.wordPng_height, self.wordPng_width = background.shape[0], background.shape[1]
        word_anchor = None
        try:
            if self.alignment_type == 'center':
                # 计算应该绘制文字的坐标
                background = create_word_background(word_width, word_height)
                self.wordPng_height, self.wordPng_width = background.shape[0], background.shape[1]
                # pillow put 以文字的左上角作为标点，需要换算出绘制在背景上的坐标
                word_anchor = wordPillow_offset(self.wordPng_width, self.wordPng_height, word_width, word_height,
                                                'center', self.alignment_spacing)

            elif self.alignment_type == 'left':

                word_anchor = wordPillow_offset(self.wordPng_width, self.wordPng_height, word_width, word_height,
                                                'left', self.alignment_spacing)

            elif self.alignment_type == 'right':

                word_anchor = wordPillow_offset(self.wordPng_width, self.wordPng_height, word_width, word_height,
                                                'right', self.alignment_spacing)

        except Exception as err:
            raise ValueError('alignment_type 不是期望的值', err)

        self.background = background
        return word_anchor

    def write_words(self):

        anchor = self.alignment()
        # 测试用的基准线，注释
        # cv2.line(self.background,(0,0),(self.wordPng_width,self.wordPng_height),(255,35,35,255))
        # cv2.line(self.background, (0, self.wordPng_height), (self.wordPng_width, 0), (255, 35, 35,255))
        # cv2 图片转成 pillow 图片对象
        # 写入汉字
        # cv2和PIL中颜色的hex码的储存顺序不同,保持4通道
        cv2img = cv2.cvtColor(self.background, cv2.COLOR_BGRA2RGBA)
        pill_img = Image.fromarray(cv2img)
        handle = ImageDraw.Draw(pill_img)
        handle.text(anchor, self.word, self.color, font=self.font)
        # PIL图片转cv2 图片
        res = cv2.cvtColor(np.array(pill_img), cv2.COLOR_RGBA2BGRA)
        # cv2.imshow('a', res)
        # cv2.waitKey(0)

        return res

    def revolve_word(self):
        # 获取cv2 四通道矩阵
        img = self.write_words()
        # 旋转角度
        revolve = self.revolve
        # 旋转中心 始终是图片的中心
        center_x, center_y = round_off(self.wordPng_width / 2), round_off(self.wordPng_height / 2)
        # 旋转，构建旋转角度
        m = cv2.getRotationMatrix2D((center_x, center_y), revolve, 1)
        dst = cv2.warpAffine(img, m, (self.wordPng_width, self.wordPng_height))
        # cv2.imshow('a', dst)
        # cv2.waitKey(0)
        return dst

    @staticmethod
    def coordinate_correct(pt1, pt2, png_shape, jpg_shape):
        '''
        当叠加图像时，可能因为叠加位置设置不当，导致png图像的边界超过背景jpg图像，而程序报错
        这里设定一系列叠加位置的限制，可以满足png图像超出jpg图像范围时，依然可以正常叠加
        '''
        x1, y1 = pt1
        x2, y2 = pt2
        yy1 = 0
        yy2 = png_shape[0]
        xx1 = 0
        xx2 = png_shape[1]
        if x1 < 0:
            xx1 = -x1
            x1 = 0
        if y1 < 0:
            yy1 = - y1
            y1 = 0
        if x2 > jpg_shape[1]:
            xx2 = png_shape[1] - (x2 - jpg_shape[1])
            x2 = jpg_shape[1]
        if y2 > jpg_shape[0]:
            yy2 = png_shape[0] - (y2 - jpg_shape[0])
            y2 = jpg_shape[0]
        return x1, y1, x2, y2, xx1, xx2, yy1, yy2

    def overlay_img(self):
        """
        图片 插入
        """
        png_img = self.revolve_word()

        # 把图片的中心 跟 输入的anchor 进行重合叠加
        anchor = coordinate_converter(anchor=self.anchor, canvas=self.canvas, offsetCenter=self.offsetCenter)

        # 进行偏移 计算正确的图片左上角坐标

        p_left_t = anchor[0]-round_off(self.wordPng_width/2),anchor[1]-round_off(self.wordPng_height/2)
        # 右下角坐标
        p_right_b = (p_left_t[0] + self.wordPng_width, p_left_t[1] + self.wordPng_height)

        canvas = copy.deepcopy(self.canvas)

        # 判断jpg图像是否已经为4通道
        if canvas.shape[2] == 3:
            canvas = add_alpha_channel(canvas)

        x1, y1, x2, y2, xx1, xx2, yy1, yy2 = \
            self.coordinate_correct(p_left_t, p_right_b, (self.wordPng_height, self.wordPng_width),
                                    (canvas.shape[0], canvas.shape[1]))

        # 获取要覆盖图像的alpha值，将像素值除以255，使值保持在0-1之间
        alpha_png = png_img[yy1:yy2, xx1:xx2, 3] / 255.0
        alpha_jpg = 1 - alpha_png

        # alpha_png = png_img[yy1:yy2, xx1:xx2, 3] / 255.0
        # alpha_jpg = alpha_png

        # 开始进行叠加
        for c in range(0, 3):
            canvas[y1:y2, x1:x2, c] = (
                    (alpha_jpg * canvas[y1:y2, x1:x2, c]) + (alpha_png * png_img[yy1:yy2, xx1:xx2, c]))

        return canvas

    def add(self):
        res = self.canvas
        if hasattr(self, 'canvas'):
            # try:
            res = self.overlay_img()
            res = cv2.cvtColor(res,cv2.COLOR_BGRA2BGR)
            # except Exception as err:
            #     print('绘制WordPng 出错', err)
        return res


if __name__ == '__main__':
    a = PngWord()
    print(a.font)
