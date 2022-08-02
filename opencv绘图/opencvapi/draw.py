import cv2

from .settings import BACKGROUND_HEIGHT, BACKGROUND_WIDTH
from .settings import IMREAD_COLOR
from .base import BackGround, Canvas
from .line import Line, ArrowLine
from .circle import Circle


class Draw(object):
    def __init__(self, path=None, **kwargs):
        self.path = path
        self.width = kwargs.get('width')
        self.height = kwargs.get('height')
        self.flags = IMREAD_COLOR
        self.components = []
        self._process_args()

    def _canvas(self, *args):
        # 传入了一个背景，彩色默认
        self.canvas = BackGround() if self.path else Canvas()

        if hasattr(self.canvas, 'create'):
            self.canvas.width = self.width
            self.canvas.height = self.height
            self.canvas.path = self.path
            return self.canvas.create()
        else:
            raise Exception('画布初始化创建失败')

    def _process_args(self):
        if not self.width:
            self.width = BACKGROUND_WIDTH
        if not self.height:
            self.height = BACKGROUND_HEIGHT
        arg = {'path': self.path, 'width': self.width, 'height': self.height}
        self.background = self._canvas(arg)

    def add_line(self, *args, **kwargs):
        """
        增加线条
        """
        line = Line(*args, **kwargs)
        setattr(line, 'canvas', self.background)
        if hasattr(line, 'add'):
            try:
                self.background = line.add()
            except Exception as err:
                print(err)

    def add_lines(self, line_list):
        for line in line_list:
            self.add_line(line)

    def add_circle(self, *args, **kwargs):
        """
        增加圆形
        """
        circle = Circle(*args, **kwargs)
        setattr(circle, 'canvas', self.background)
        if hasattr(circle, 'add'):
            try:
                self.background = circle.add()
            except Exception as err:
                print(err)

    def add_circles(self):
        ...

    def add_word(self):
        ...

    def add_words(self):
        ...

    def add_arrow(self, *args, **kwargs):
        """
        添加直线箭头
        """
        arrow = ArrowLine(*args, **kwargs)
        setattr(arrow, 'canvas', self.background)
        if hasattr(arrow, 'add'):
            try:
                self.background = arrow.add()
            except Exception as err:
                print(err)

    def add_arrows(self):
        ...

    def save(self):
        if self.background:
            self.background.save()


class DrawBuilder(object):
    def add(self):
        ...



if __name__ == '__main__':
    print(1)
