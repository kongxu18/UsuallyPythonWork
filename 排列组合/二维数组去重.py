def clear_list(data):
    new_data = []
    for i in range(len(data)):
        src = data[i]

        is_repeat = False
        for j in range(len(new_data)):

            temp = new_data[j]


            # 二维数组内元素数组再比对
            wid = 0
            for t in temp:
                if t in src:
                    wid += 1
            if wid == len(src):
                is_repeat = True
                break

        if not is_repeat:
            new_data.append(src)

    return new_data


d = [[{'a'}, {'b'}, {'c'}, {'d'}],
     [{'d', 'b', 'c', 'a'}],
     [{'a'}, {'b'}, {'d', 'c'}],
     [{'a'}, {'c'}, {'d', 'b'}],
     [{'a'}, {'d'}, {'b', 'c'}],
     [{'b'}, {'c'}, {'d', 'a'}],
     [{'b'}, {'d'}, {'a', 'c'}],
     [{'c'}, {'d'}, {'b', 'a'}],
     [{'a'}, {'d', 'b', 'c'}],
     [{'b'}, {'d', 'c', 'a'}],
     [{'c'}, {'d', 'b', 'a'}],
     [{'d'}, {'b', 'a', 'c'}], [{'b', 'a'}, {'d', 'c'}], [{'c', 'a'}, {'d', 'b'}], [{'d', 'a'}, {'b', 'c'}]]



r = clear_list(d)
print(r)
