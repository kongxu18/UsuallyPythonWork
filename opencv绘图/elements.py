import numpy as np
import cv2 as cv

"""
装饰器类
"""


class small(object):
    per = 3

    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        return self.small_img(*args, **kwargs)

    def small_img(self, *param, **kwargs):
        """
        :param param:
        :param kwargs: { 'img':None,'per':None}
        :return:
        # """
        img = kwargs.get('img')
        per = self.per
        height, width = img.shape[:2]
        reSize = cv.resize(img, (int(width / per), int(height / per)),
                           interpolation=cv.INTER_AREA)

        return self.fun(reSize)


class CRect:
    def __init__(self, l, t, w, h):
        self.l = l
        self.r = l + w
        self.t = t
        self.b = t + h
        self.w = w
        self.h = h


class Aest:
    @staticmethod
    @small
    def test(a):
        print(a)


class Canvas:
    """
    构建画布
    """

    def __init__(self, canvas_height, canvas_width):
        self.__canvas_height = canvas_height
        self.__canvas_width = canvas_width

    @property
    def get_canvas(self):
        canvas = np.zeros((self.__canvas_height, self.__canvas_width, 3), dtype=np.uint8)
        canvas[canvas == 0] = 255
        return canvas

    @property
    def canvas_height(self):
        return self.__canvas_height

    @property
    def canvas_width(self):
        return self.__canvas_width


class Linker:
    def __init__(self):
        pass


class Locker:
    def __init__(self, path, center_x=93.0, center_y=158.0):
        self.center_x, self.center_y = center_x, center_y
        self.path = path

    # def get_locker(self, canvas, *args):
    #     raise NotImplementedError('必须重写父类此方法')


class LeftLocker(Locker):
    def __init__(self, center_x, center_y, path):
        super().__init__(center_x, center_y, path)
        self.__locker = self.load()

    def load(self):
        return cv.imread(self.path)

    def get_shape(self):
        if self.__locker:
            temHeight, temWidth = self.__locker.shape
        else:
            raise Exception('图片读取失败')
        return temHeight, temWidth

    @staticmethod
    @small
    def change_size(img):
        return img

    @property
    def locker(self):
        return self.change_size(self.__locker)

    def get_leftLockCenter(self, canvas, *args):
        self.temHeight, self.temWidth = self.get_shape()
        # 读取锁头
        lock_cx = self.center_x / self.temWidth
        lock_cy = self.center_y / self.temHeight

        locker = self.locker

        row, col = locker.shape[:2]
        canvas_height = None
        if hasattr(canvas, 'canvas_height'):
            canvas_height = getattr(canvas, 'canvas_height', None)
        leftLockRect = CRect(10, (canvas_height - row) // 2, col, row)
        leftLockCenter = (
            int(leftLockRect.l + lock_cx * leftLockRect.w), int(leftLockRect.t + lock_cy * leftLockRect.h))
        return leftLockCenter


if __name__ == '__main__':
    c = Canvas(10, 10)
    # print(c.get_canvas)

    l = LeftLocker(1, 2, 3)
    # a = l.get_locker

    t = Aest()
    t.test(5)
