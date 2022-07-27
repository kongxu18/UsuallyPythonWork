from models import base


class DataFactory(object):
    font = None
    type = ''
    start_row = ''
    keyword = ''
    border = ''

    def __init__(self, DataClass, *args, **kwargs):
        self.DataClass = DataClass
        self.args = args
        self.kwargs = kwargs
        self.pic_dict = None

    def create(self):
        dataIns = self.DataClass(*self.args, **self.kwargs)
        dataIns.keyword = self.keyword
        if self.keyword == 'headerSetting':
            return dataIns
        dataIns.font = self.font
        dataIns.start_row = self.start_row
        dataIns.border = self.border

        return dataIns


class HeaderFactory(DataFactory):

    def __init__(self, DataClass, *args, **kwargs):
        super().__init__(DataClass, *args, **kwargs)
        self.font = Font(name='黑体', bold=True)
        self.border = border_style
        self.start_row = 2
        self.keyword = 'headers'


class TitleFactory(DataFactory):
    def __init__(self, DataClass, *args, **kwargs):
        super().__init__(DataClass, *args, **kwargs)
        self.border = border_style
        self.font = Font(name='黑体', bold=True, size=20)
        self.start_row = 1
        self.keyword = 'title'


class RowsFactory(DataFactory):
    def __init__(self, DataClass, *args, **kwargs):
        super().__init__(DataClass, *args, **kwargs)
        self.border = border_style
        self.font = Font(name='黑体', bold=True)
        self.start_row = 3
        self.keyword = 'rows'


class HeaderSettingFactory(DataFactory):
    def __init__(self, DataClass, *args, **kwargs):
        super().__init__(DataClass, *args, **kwargs)
        self.keyword = 'headerSetting'


class PictureFactory(DataFactory):
    def __init__(self, DataClass, *args, **kwargs):
        super().__init__(DataClass, *args, **kwargs)
        self.keyword = 'picture'
        self.font = None
        self.type = 'picture'

    def picture(self, pic):
        ...
