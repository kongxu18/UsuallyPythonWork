def fun():
    while True:
        yield 1
        yield 2


a =fun()

print(a.__next__())
print(a.__next__())
print(a.__next__())