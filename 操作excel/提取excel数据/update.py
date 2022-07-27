import json

path1 = ['F1索网.json', 'F2索网.json', 'F3索网.json']
path2 = ['变更索网1.json', '变更索网2.json', '变更索网3.json']
arr1 = []
for p in path1:
    with open(p, 'r', encoding='utf8') as f:
        s = f.read()
        _dict = json.loads(s)
        arr1 += _dict['数据']


def fun(path, json_path):
    with open(json_path, 'r', encoding='utf8') as f:
        s = f.read()
        _dict = json.loads(s)
        arr = _dict['数据']
    for index, dict_ in enumerate(arr):
        索号 = dict_['索号']
        dict_['变更来源'] = path
        for i, item in enumerate(arr1):
            if item['索号'] == 索号:
                arr1[i] = dict_


print(len(arr1))
# F2A20ZS-140A
fun('变更索网数据明细20211008.xlsx', path2[0])
fun('变更索网数据明细20211015.xlsx', path2[1])
fun('变更索网数据明细20211018.xlsx', path2[2])

with open('res.json','w',encoding='utf8') as f:
    js = json.dumps({'数据':arr1},ensure_ascii=False)
    f.write(js)
