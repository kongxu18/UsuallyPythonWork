from openpyxl import Workbook


class Excel(object):
    def __init__(self, path):
        self.path = path
        self.__wb = None

    def _wb_init(self):
        self.__wb = Workbook()
