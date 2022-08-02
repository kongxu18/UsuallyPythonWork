import cv2


class Line:
    def __init__(self, *args, **kwargs):
        self.canvas = None
        self.start_point, self.end_point = \
            kwargs.get('start_point'), kwargs.get('end_point')
        self.anchor = (self.start_point, self.end_point)
        self.color = kwargs.get('color')
        # 线条粗细
        self.thickness = kwargs.get('thickness') if kwargs.get('thickness') else 1
        # 位置传参数，线条渲染模式，这里默认抗锯齿
        self.lineType = kwargs.get('lineType')
        self._process_args(*args, **kwargs)

    def _process_args(self, *args, **kwargs):
        if args:
            for arg in args:
                if isinstance(arg, tuple):
                    if len(arg) == 2:
                        self.start_point, self.end_point = arg
                        self.anchor = (self.start_point,self.end_point)
                    elif len(arg) == 3:
                        self.color = arg
                elif isinstance(arg, int):
                    self.thickness = arg

    def add(self):
        res = self.canvas
        if hasattr(self, 'canvas'):
            """
            这里已经把画布传入
            添加直线
            """
            try:
                res = cv2.line(self.canvas,self.start_point,self.end_point,self.color,self.thickness)
                # res = cv2.line(self.canvas,(0,0),(511,511),(255,0,0),5)
            except Exception as err:
                print('绘制直线参数错误',err)

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
            try:
                res = cv2.arrowedLine(self.canvas, self.start_point, self.end_point,
                                      self.color, self.thickness,cv2.LINE_AA,self.shift,self.tipLength)
            except Exception as err:
                # print(self.start_point, self.end_point, self.color, self.thickness, '-----')
                print('绘制箭头直线参数错误', err)
        return res