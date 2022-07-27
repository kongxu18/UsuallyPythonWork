import requests

re = requests.get('https://www.tutukiki.com/m3u8/?url=https://c1.monidai.com/20210918/72XLNLEa/index.m3u8')


# print(re.text)


def fun():
    """bbbbbbb"""
    return 'aaaaaa'


fun.name = 'asd'
a = fun
print(a.__doc__)


class A:
    def get(self):
        print(self)

    @classmethod
    def get1(self):
        print(self)

    @staticmethod
    def num():
        print(a)
        return 1


class B(A):

    def num(self):
        print(2)

b = B()
b.num()
