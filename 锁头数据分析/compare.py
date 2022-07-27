"""
锁头数据比对
比较两个文件不一样
"""

import json
import numpy as  np
from decimal import Decimal

np.set_printoptions(suppress=True)


class Compare(object):
    KEYS = ["下层索头点Origin", "下层索头点X", "上层索头点Origin", "上层索头点X", "下层索头点Y", "上层索头点Y"]

    def __init__(self, old_path, new_path):
        self.old_path = old_path
        self.new_path = new_path
        self.err = []

    @staticmethod
    def __convert_to_json(path):
        with open(path, 'r',encoding='utf8') as f:
            dic = json.loads(f.read())
        return dic

    @property
    def old(self) -> dict:
        return self.__convert_to_json(self.old_path)

    @property
    def new(self) -> dict:
        return self.__convert_to_json(self.new_path)

    def deal(self):
        """
        比对
        :return:
        """
        if isinstance(self.old, dict):
            for i, dic in enumerate(self.old['data']):
                identify = dic['标识']
                # if identify == 'L2束索-32':
                for key, val in dic.items():
                    self.compare(i, key, val, identify)

        return self.err

    def compare(self, i, key, val, identify):

        dic_new = self.new['data'][i]
        new_val = dic_new.get(key)
        # print(val)
        # print(new_val)
        # print('-=--------------------------')
        if type(val) == type(new_val):
            if key in self.KEYS:
                val = self.round_2(val)
                new_val = self.round_2(new_val)
                # if list(val) != list(new_val):
                #     self.err.append((identify, key, val, new_val))
                self.difference(val, new_val, identify, key)
            elif key == '上层碰撞数据_arr' or key == '下层碰撞数据_arr':
                if len(val) == len(new_val):
                    关联索_dict = set()
                    关联索new_dict = set()
                    for arr_i, arr_val in enumerate(val):
                        关联索 = arr_val.get('关联索')

                        关联索_new = new_val[arr_i].get('关联索')
                        关联索_dict.add(关联索)
                        关联索new_dict.add(关联索_new)
                    set_len = len(关联索_dict)
                    union_set = 关联索_dict.union(关联索new_dict)
                    if set_len != len(union_set):
                        self.err.append((identify, key, 关联索_dict.symmetric_difference(关联索new_dict)))
                else:
                    self.err.append((identify, key, len(val), len(new_val)))
            else:
                if val != new_val:
                    self.err.append((identify, key, val, new_val))
        else:
            self.err.append((identify, key, val, new_val))

    def round_2(self, str_list: str):
        list_ = str_list.split(',')
        arr = np.array(list_, dtype=np.float64)
        arr = np.round(arr, 2)
        return arr

    def difference(self, old, new, identify, key):
        diff = old - new
        diff = abs(diff)
        diff_bool = diff >= 2.00
        if diff_bool.any():
            self.err.append((identify, key, diff))

    def out_put(self):
        print('------------------------------')
        dict_ = {}
        for items in self.err:
            print(items[0],items[1],items[2])
            dict_[items[0]] = (items[1],items[2])
        print('----end--=-=-=-=-=-=-=-=-=-=-=')
        return dict_



if __name__ == '__main__':
    # c = Compare('索头数据分析/F1索头位置数据_旧的.json', '索头数据分析/F1索头位置数据_20211101.json')
    # c.deal()
    # c.out_put()
    c2 = Compare('索头数据分析/F2索头位置数据_标准.json', '索头数据分析/F2索头位置数据_20211101(1).json')
    c2.deal()
    c2.out_put()
    # c3 = Compare('索头数据分析/F3索头位置数据_旧的.json', '索头数据分析/F3索头位置数据_20211101.json')
    # print(c3.deal())
