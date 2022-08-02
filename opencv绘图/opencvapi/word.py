import cv2
from typing import List, Tuple, AnyStr


class Word(object):
    def __init__(self, *args, **kwargs):
        self.canvas = None
        self.word: AnyStr = kwargs.get('word')
        self.anchor: Tuple[int] = kwargs.get('anchor')
        self.font = kwargs.get('font')
        self.color: Tuple[int] = kwargs.get('color')

        # 图像数据圆点的位置，默认位于左上角。若参数选择True, 则原点位于左下角
        self.bottomLeftOrigin: bool = kwargs.get('bottomLeftOrigin')

        # 位置传参数,字体大小
        self.size: float = kwargs.get('size')
        # 字体粗细
        self.thickness: float = kwargs.get('thickness')

        self._process_args(*args, **kwargs)

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
            添加直线
            """
            try:
                res = cv2.putText(self.canvas, text=self.word, org=self.anchor, fontFace=self.font,
                                  fontScale=self.size, color=self.color, thickness=self.thickness,
                                  lineType=cv2.LINE_AA, bottomLeftOrigin=self.bottomLeftOrigin)
            except Exception as err:
                # print(self.start_point, self.end_point, self.color, self.thickness, '-----')
                print('绘制箭头直线参数错误', err)
        return res
