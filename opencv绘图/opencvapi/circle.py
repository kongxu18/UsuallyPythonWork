import cv2
from .funs import coordinate_converter, resize_args
from .settings import Colour


class Circle(object):
    def __init__(self, *args, **kwargs):

        self.canvas = None
        self.anchor = kwargs.get('anchor')
        self.radius = kwargs.get('radius')
        self.color = kwargs.get('color')
        # 位置传参数
        self.resize = kwargs.get('resize')
        self.thickness = kwargs.get('thickness') if kwargs.get('thickness') else 1
        self._process_args(*args, **kwargs)

    def _process_args(self, *args, **kwargs):
        if args:
            for arg in args:
                if isinstance(arg, int) or isinstance(arg, float):
                    self.radius = int(arg)
                elif isinstance(arg, tuple):
                    if len(arg) == 2:
                        self.anchor = arg
                    elif len(arg) == 3:
                        self.color = arg
        if not self.color:
            self.color = Colour.BLACK

    def add(self):
        res = self.canvas
        if hasattr(self, 'canvas'):
            """
            这里已经把画布传入
            添加圆圈
            """
            anchor = resize_args(self.anchor, self.resize)
            anchor = coordinate_converter(anchor, self.canvas)

            radius = resize_args(self.radius, self.resize)

            try:
                res = cv2.circle(self.canvas, anchor, radius, self.color, self.thickness, cv2.LINE_AA)

            except Exception as err:
                print('绘制圆形参数错误', err)

        return res
