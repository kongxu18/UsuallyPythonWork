class BaseHeader(object):
    def __init__(self):
        self.__data = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class CompanyHeader(BaseHeader):
    def __init__(self, data):
        super().__init__()

    def __setattr__(self, key, value):
        print(key, value)


if __name__ == '__main__':
    head = CompanyHeader(3)
    head.data = 7
    print(head.data)
