"""
类
"""


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name+'qqq'

    def show(self):
        print('父亲', self.age, self.name)


class Man(Person):
    def __init__(self, sex, age, name):
        super(Man, self).__init__(age, name)
        self.sex = sex


    def show(self):
        print('man')
        # print(self.age,self.name,self.sex)


class Woman(Person):
    def __init__(self, age, name,love):
        super().__init__(age, name)
        self.love = love

    def show(self):
        print('woman')
        # print('love',self.love,self.age,self.name)


class Child(Woman,Man):
    def __init__(self, dog, age, name, love):

        # super().__init__(age, name,love)
        self.dog = dog
        super(Child, self).show()

    def show(self):
        print('child',self.dog)


p = Man('n',11,'aaaa')
# p.show()
#
child = Child('dog-lili',1,'name--','dad')
child.show()

# woman = Woman(11,'ccc','dad')
# woman.show()


class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B(A):
    def __init__(self):
        super().__init__()


    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3
print('--------')
b = B()
b.add(2)
print(b.n)