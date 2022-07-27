# ('5.57','220*458，肋板-D600')
import re


def deal(string: str,i):
    char = string.split()
    pattern = re.compile(r'(.*)kg/件')
    res = pattern.findall(char[0])

    char[0] = res[0]
    char[1]=char[1].replace('，', '').replace('肋板-','')
    a = 'getdate()'
    char[0] = float(char[0])
    char[0] , char[1] = char[1],char[0]
    char = [1,0,0,'C'+str(i+1)] +char+[0]
    print(tuple(char), ',')


with open('string', 'r') as f:
    for i,line in enumerate(f.readlines()):
        deal(line,i)

# result1 = pattern.findall(string)

# print(result1)
