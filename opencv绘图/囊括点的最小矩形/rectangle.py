import re
from matplotlib.pyplot import plot


class File(object):
    def __init__(self, path):
        self.num = 0
        self.path = path
        self.data_dic = {}
        self.i = None
        self.name = ''

    @property
    def data(self):
        with open(self.path, 'r', encoding='utf8') as f:
            for i, line in enumerate(f):
                # print(i, line, type(line))
                self.analyse(line, i)
                # if i == 4:
                #     break
            data_dic = self.pop_data(self.data_dic)
        return data_dic

    def analyse(self, string, index):

        string = string.strip().split()
        first_str = string[0]
        if first_str and re.match('Fof', first_str):
            self.i = index
            self.num += 1
            self.name = 'Fof' + str(self.num)
            self.data_dic[self.name] = []

        if self.i and index > self.i:
            arr = self.data_dic.get(self.name)
            # 需要的数据
            if isinstance(arr, list):
                if len(string) == 5:
                    arr.append((string[1], string[2]))
                else:
                    self.name = ''

    def pop_data(self, data_dict):
        data_dict.pop('Fof' + str(self.num))
        data_dict.pop('Fof1')
        return data_dict


class Rectangle(object):
    max_width = 0
    max_height = 0
    x_min = 0
    x_max = 0

    def __init__(self, points, name='t'):
        self.points = points
        self.name = name
        self.w = 0
        self.h = 0
        self.l, self.r, self.b, self.t = float(points[0][0]), float(points[0][0]), float(points[0][1]), float(
            points[0][1])

    def detail(self):
        for x, y in self.points:
            x, y = float(x), float(y)
            if x < self.l:
                self.l = x
            if x > self.r:
                self.r = x
            if y < self.b:
                self.b = y
            if y > self.t:
                self.t = y
            self.w, self.h = abs(self.r - self.l), abs(self.t - self.b)
            if self.w > self.max_width:
                Rectangle.max_width = self.w
            if self.h > self.max_height:
                Rectangle.max_height = self.h

            if Rectangle.x_min:
                if x < Rectangle.x_min:
                    Rectangle.x_min = x
            else:
                Rectangle.x_min = x
            if Rectangle.x_max:
                if x > Rectangle.x_max:
                    Rectangle.x_max = x
            else:
                Rectangle.x_max = x

        return {self.name:
                    [self.l, self.r, self.b, self.t],
                'width': self.w, 'height': self.h, 'x_min': Rectangle.x_min, 'x_max': Rectangle.x_max}


if __name__ == '__main__':
    f = File('F3索网.EIN')

    for key, val in f.data.items():
        rect = Rectangle(val, key)
        res = rect.detail()
        print(res)
    print(Rectangle.max_width, Rectangle.max_height, Rectangle.x_min, Rectangle.x_max)

    # print(Rectangle.max_weight,Rectangle.max_height)m////
