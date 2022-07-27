class Row(object):
    def __init__(self, row):
        self.__row = row

    @property
    def val(self):
        return self.__row

    @val.setter
    def val(self, num):
        self.__row += num


a = Row(1)

print(a.val)

a.val = 3

print(a.val)