import cv2

from .settings import BACKGROUND_HEIGHT, BACKGROUND_WIDTH
from .settings import IMREAD_COLOR
from .base import BackGround, Canvas
from .line import Line, ArrowLine,Rectangle
from .circle import Circle
from .word import Word
from . import components


class Draw(object):
    def __init__(self, path=None, **kwargs):
        self.path = path
        self.width = kwargs.get('width')
        self.height = kwargs.get('height')
        self.flags = IMREAD_COLOR
        self.components = components
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
        setattr(self.components, 'DrawLiving', self)

    def add_line(self, *args, **kwargs):
        """
        增加线条
        """
        DrawBuilder(self, typeFun='line').add_somethings(*args, **kwargs)

    def add_lines(self, line_list):
        for line in line_list:
            self.add_line(line)

    def add_rectangle(self, *args, **kwargs):
        """
        长方形
        """
        DrawBuilder(self, typeFun='rectangle').add_somethings(*args, **kwargs)

    def add_circle(self, *args, **kwargs):
        """
        增加圆形
        """
        DrawBuilder(self, typeFun='circle').add_somethings(*args, **kwargs)

    def add_circles(self):
        ...

    def add_word(self, *args, **kwargs):
        """
        word: AnyStr
        anchor: Tuple[int]
        color: Tuple[int]
        bottomLeftOrigin: bool :图像数据圆点的位置，默认位于左上角。若参数选择True, 则原点位于左下角

        以下需要 关键字传参数，也可以不传，有默认值
        font : 字体
        size: float:位置传参数,字体大小
        thickness: float :字体粗细
        china : bool
        """
        DrawBuilder(self, typeFun='word').add_somethings(*args, **kwargs)

    def add_words(self, word_list: list):
        ...

    def add_arrow(self, *args, **kwargs):
        """
        添加直线箭头
        """
        DrawBuilder(self, typeFun='arrow').add_somethings(*args, **kwargs)

    def add_arrows(self):
        ...

    def save(self):
        if self.background:
            self.background.save()


class DrawBuilder(object):
    COMPONENTS = {
        'word': Word,
        'line': Line,
        'circle': Circle,
        'arrow': ArrowLine,
        'rectangle':Rectangle
    }

    def __init__(self, draw, typeFun=None):
        self.__draw = draw
        self.typeFun = typeFun

    def add_somethings(self, *args, **kwargs):
        if self.typeFun in DrawBuilder.COMPONENTS:
            obj = DrawBuilder.COMPONENTS.get(self.typeFun)
            if not obj:
                raise ValueError('不要试图使用不存在的方法')
            living_example = obj(*args, **kwargs)
            # print(type(living_example), '对象')
            background = getattr(self.__draw, 'background', None)
            setattr(living_example, 'canvas', background)
            if hasattr(living_example, 'add'):
                try:
                    setattr(self.__draw, 'background', living_example.add())
                    # return living_example.add()
                except Exception as err:
                    print(err, '99')


if __name__ == '__main__':
    print(1)
