import json


# 传入的json格式数据
class JsonData(object):
    def __init__(self, path: str, encode='utf8'):
        self.path = path
        self.encoding = encode

    @property
    def data(self) -> dict:
        with open(self.path, 'r', encoding=self.encoding) as f:
            res_data = json.loads(f.read())
        return res_data






