class A:
    def __init__(self):
        self.a = None

    def fun(self):
        c = self.a
        print('A fun')


class B(A):
    def __init__(self):
        super().__init__()


    def fun1(self):
        super(B, self).fun()
        self.fun()

    def fun(self):
        print('B fun')

b =B()
b.fun1()
