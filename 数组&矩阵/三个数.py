def main():
    num1 = int(input('数字1：'))
    num2 = int(input('数字1：'))
    num3 = int(input('数字1：'))

    tamp = []
    if (num1 < num2):
        max_ = num2
        min = num1
        tamp.append(min)
    else:
        max_ = num1
        min = num2
        tamp.append(min)
    if (max_ < num3):
        max_ = num3
        tamp = [num1, num2]
    else:
        tamp.append(num3)

    string = 'max value is %s' % (max_)
    string2 = 'it is %s,more than %s and %s more than %s'
    if len(tamp) < 2:
        tamp.append(max_)
    res = []
    for val in tamp:
        res.append(max_-val)
        res.append(val)

    # print(res)
    print(string)
    print(string2 % tuple(res))


if __name__ == '__main__':
    main()
