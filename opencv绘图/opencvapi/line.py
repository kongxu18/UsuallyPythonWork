import cv2
import numpy as np

from .funs import coordinate_converter
from .settings import Colour


class Line:
    def __init__(self, *args, **kwargs):

        self.canvas = None
        self.anchor = kwargs.get('anchor')
        self.color = kwargs.get('color')
        # 线条粗细
        self.thickness = kwargs.get('thickness')
        # 位置传参数，线条渲染模式，这里默认抗锯齿
        self.lineType = kwargs.get('lineType')
        self.offsetCenter: bool = kwargs.get('offsetCenter')

        self.process_args(*args, **kwargs)

    def process_args(self, *args, **kwargs):
        if args:
            for arg in args:
                if isinstance(arg, tuple):
                    if len(arg) == 2:
                        self.anchor = arg
                    elif len(arg) == 3:
                        self.color = arg
                elif isinstance(arg, int):
                    self.thickness = arg
        if self.anchor:
            self.start_point, self.end_point = self.anchor
        if not self.thickness:
            self.thickness = 1
        if not self.color:
            self.color = Colour.BLACK
        if not self.offsetCenter:
            self.offsetCenter = False

    def add(self):
        res = self.canvas
        if hasattr(self, 'canvas'):
            """
            这里已经把画布传入
            添加直线
            """

            start = coordinate_converter(self.start_point, self.canvas, self.offsetCenter)
            end = coordinate_converter(self.end_point, self.canvas, self.offsetCenter)

            try:
                res = cv2.line(self.canvas, start, end, self.color, self.thickness, lineType=cv2.LINE_AA)
            except Exception as err:
                print('绘制直线参数错误', err)

        return res


class ArrowLine(Line):
    """
    InputOutputArray img, # 输入图像
    const Scalar &  color, # 颜色
    int thickness = 1, # 线宽
    int line_type = 8, # 渲染类型
    int shift = 0,
    double tipLength = 0.1
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # int类型的shift，该数值可以控制箭头的长度和位置，比如当其为1时，箭头的位置变为原先的1/2，长度也变为1/2，
        # 若该数值为2，则均变为原先的1/4。我猜测数值X和缩放的比例关系应该是2的X次方的倒数。
        self.shift = kwargs.get('shift') if kwargs.get('shift') else 0
        # double类型的tipLength，箭头和箭身的比例，默认为0.1
        self.tipLength = kwargs.get('tipLength') if kwargs.get('tipLength') else 0.1

    def add(self):
        res = self.canvas
        if hasattr(self, 'canvas'):
            """
            这里已经把画布传入
            添加直线
            """

            start = coordinate_converter(self.start_point, self.canvas, self.offsetCenter)
            end = coordinate_converter(self.end_point, self.canvas, self.offsetCenter)
            try:
                res = cv2.arrowedLine(self.canvas, start, end,
                                      self.color, self.thickness, cv2.LINE_AA, self.shift, self.tipLength)
            except Exception as err:
                # print(self.start_point, self.end_point, self.color, self.thickness, '-----')
                print('绘制箭头直线参数错误', err)
        return res


class Rectangle(Line):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shift = kwargs.get('shift')

    def add(self):
        res = self.canvas
        if hasattr(self, 'canvas'):
            """
            这里已经把画布传入
            添加矩形
            """

            start = coordinate_converter(self.start_point, self.canvas, self.offsetCenter)
            end = coordinate_converter(self.end_point, self.canvas, self.offsetCenter)
            try:
                res = cv2.rectangle(self.canvas, start, end,
                                    self.color, self.thickness, cv2.LINE_AA, self.shift)
            except Exception as err:
                # print(self.start_point, self.end_point, self.color, self.thickness, '-----')
                print('绘制箭头直线参数错误', err)
        return res


class PolyLine(Line):
    """
    多边形
    """

    def __init__(self, *args, **kwargs):
        self.anchors = kwargs.get('anchors') if kwargs.get('anchors') else None
        self.isClosed = kwargs.get('isClosed') if kwargs.get('isClosed') else True

        super().__init__(*args, **kwargs)
        self.fillcolor = kwargs.get('fillcolor') if kwargs.get('fillcolor') else self.color

    def process_args(self, *args, **kwargs):
        super().process_args(*args, **kwargs)
        if args:
            for arg in args:
                if isinstance(arg, list):
                    self.anchors = arg

    def reshape(self):
        if self.anchors:
            for i, point in enumerate(self.anchors):
                self.anchors[i] = coordinate_converter(point, self.canvas, offsetCenter=self.offsetCenter)
            self.anchors = np.array(self.anchors, dtype=np.int32).reshape((-1, 1, 2))

        else:
            raise ValueError('polyline 关键参数为空')

    def add(self):
        res = self.canvas
        if hasattr(self, 'canvas'):
            try:
                self.reshape()
                if self.thickness == -1:
                    thickness = 1
                    res = cv2.polylines(self.canvas, [self.anchors], self.isClosed, self.color, thickness)
                    res = cv2.fillPoly(self.canvas, [self.anchors], self.fillcolor)
                else:
                    res = cv2.polylines(self.canvas, [self.anchors], self.isClosed, self.color, self.thickness)

            except Exception as err:
                print('绘制多边形错误：', err)
        return res
