from .settings import CANVAS_HEIGHT, CANVAS_WIDTH, IMREAD_COLOR, Colour
import cv2
import numpy as np


class IMAGE(object):
    def __init__(self, path=None, width=None, height=None, color=None):
        self.path = path
        self.width = width if width else CANVAS_WIDTH
        self.height = height if height else CANVAS_HEIGHT
        self.color = color if color is not None else Colour.BLACK

    def create(self):
        raise Exception('必须重写')


class BackGround(IMAGE):
    def __init__(self, path, width, height, color):
        super().__init__(path, width, height, color)

    def create(self):
        canvas = cv2.imread(self.path, IMREAD_COLOR)
        return canvas


class Canvas(IMAGE):
    def __init__(self, path, width, height, color):
        super().__init__(path, width, height, color)

    def _process_args(self):
        if isinstance(self.width, float):
            self.width = int(self.width)
        if isinstance(self.height, float):
            self.height = int(self.height)

    def create(self):
        self._process_args()
        # 画布
        canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        canvas[:,:] = self.color
        return canvas
