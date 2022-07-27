class A:
    x = 0

    def fun(self, x):
        self.x = x

    def fun2(self, x):
        A.x = x

    def p(self):
        print(self.x, end='')


a = A()
b = A()

# a.fun(1)
a.fun2(1)

print(a.x, b.x, A.x)
a.p()
b.p()

