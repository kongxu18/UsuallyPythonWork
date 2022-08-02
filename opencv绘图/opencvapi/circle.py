import cv2


class Circle(object):
    def __init__(self, *args, **kwargs):
        self.canvas = None
        self.anchor = kwargs.get('anchor')
        self.radius = kwargs.get('radius')
        self.color = kwargs.get('color')
        # 位置传参数
        self.thickness = kwargs.get('thickness')
        self._process_args(*args, **kwargs)

    def _process_args(self, *args, **kwargs):
        if args:
            for arg in args:
                if isinstance(arg, int):
                    self.radius = arg
                elif isinstance(arg, tuple):
                    if len(arg) == 2:
                        self.anchor = arg
                    elif len(arg) == 3:
                        self.color = arg

    def add(self):
        res = self.canvas
        if hasattr(self, 'canvas'):
            """
            这里已经把画布传入
            添加圆圈
            """
            try:
                res = cv2.circle(self.canvas, self.anchor, self.radius, self.color, self.thickness,cv2.LINE_AA)
            except Exception as err:
                print('绘制圆形参数错误', err)

        return res
