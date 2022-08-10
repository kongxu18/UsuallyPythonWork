class A:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b


def fun(**kwargs):
    return A(**args)


args = {'a': 123, 'b': 132}
a = fun(**args)
print(a.a)
print(a.b)
