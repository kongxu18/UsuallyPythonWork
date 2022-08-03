from .settings import CANVAS_HEIGHT, CANVAS_WIDTH, IMREAD_COLOR
import cv2
import numpy as np


class IMAGE(object):
    def __init__(self, path=None, width=None, height=None):
        self.path = path
        self.width = width if width else CANVAS_WIDTH
        self.height = height if height else CANVAS_HEIGHT


    def create(self):
        raise Exception('必须重写')


class BackGround(IMAGE):
    def __init__(self):
        super().__init__()

    def create(self):
        canvas = cv2.imread(self.path, IMREAD_COLOR)

        return canvas


class Canvas(IMAGE):
    def __init__(self):
        super().__init__()

    def _process_args(self):
        if isinstance(self.width, float):
            self.width = int(self.width)
        if isinstance(self.height, float):
            self.height = int(self.height)

    def create(self):
        self._process_args()
        # 画布

        canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        canvas[canvas == 0] = 255
        return canvas
