import numpy as np
from elements import Canvas,small
import cv2 as cv


class Base(object):
    # 画布
    canvas = None
    # language
    language = None
    # 横线
    transverse_line = None
    # 竖线
    vertical_line = None
    # 圆
    circle = None
    # 锁头
    lock_head = None
    # 锁链
    linker = None

    @property
    def get_items(self):
        return self.__dict__

    def show(self):
        print(self.canvas)
        cv.imshow('t', self.canvas)
        cv.waitKey(0)


class PictureBuilder(object):
    """
    建造者
    """

    def __init__(self):
        self.picture = Base()

    def add_canvas(self, canvas):
        print('add__')
        self.picture.canvas = canvas
        return self.add_canvas

    def build(self):
        return self.picture


class Engineer(object):
    """
    指挥者
    """

    def __init__(self):
        self.builder = None

    def construct(self, **kwargs):
        self.builder = PictureBuilder()
        for key, val in kwargs.items():
            if key:
                key = 'add_' + str(key)
            print(key)
            if hasattr(self.builder, key):
                print('getattr')
                handle = getattr(self.builder, key)(val)

        return self.builder.build()


if __name__ == '__main__':
    # 参数
    canvas_height = 250
    canvas_width = 1200

    # ------

    canvas = Canvas(canvas_height=canvas_height, canvas_width=canvas_width)
    small.canvas = canvas
    small.per = 3



    eng = Engineer()
    r = eng.construct(canvas=canvas.get_canvas)
    r.show()
