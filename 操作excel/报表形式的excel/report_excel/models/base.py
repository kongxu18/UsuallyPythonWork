
class BaseData(object):
    keyword = ''
    start_row = ''

    def __init__(self, json_data: dict):
        self.json_data = json_data

    @property
    def data(self):
        return self.json_data.get(self.keyword)


class Header(BaseData):
    def __init__(self, json_data: dict):
        super().__init__(json_data)


class Rows(BaseData):
    def __init__(self, json_data: dict):
        super().__init__(json_data)


class Title(BaseData):
    def __init__(self, json_data: dict):
        super().__init__(json_data)


class HeaderSettings(BaseData):
    def __init__(self, json_data: dict):
        super().__init__(json_data)


class Picture(BaseData):
    def __init__(self, json_data: dict):
        super().__init__(json_data)
