# excel 配置文件

DEFAULT_SET = {
    'ENCODING': 'utf8',
    'COMPANY': '上海海勃膜结构股份有限公司',
    'component': ['company_title', 'title', 'items', 'table_header', 'table_rows'],
    'company_title': {'start_row': 1},
    'title': {'start_row': 2},
    'items': {'start_row': 3},
}


class Settings(object):
    attr = {}

    def __init__(self):
        self.set_from_settings()

    @classmethod
    def set_from_settings(cls):
        if isinstance(DEFAULT_SET, dict):
            for key, val in DEFAULT_SET.items():
                cls.attr.update({key: val})
        else:
            assert TypeError('settings must be a dict')

    @property
    def data(self):
        return self.attr
