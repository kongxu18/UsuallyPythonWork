import random
import numpy as np
p = []
for i in range(15):
    p.append((i, 0, 0))

random.shuffle(p)
print(p)

vec = [1, 1, 0]


def quickSort(arr, low, high, vec):
    # 递归结束条件
    if low >= high:
        return
    else:
        def partition(arr, low, high):
            # 索引往前走一个
            i = low - 1
            # 选择基准点
            try:
                pivot = arr[high]
            except:
                print(arr,low,high)
            for j in range(low, high):
                # 向量判断
                # 创建第一个点到当前点向量
                p_now = arr[j]
                p_now = np.array(p_now)
                pivot = np.array(pivot)
                vector = pivot-p_now
                print(vector)
                # vector = rs.VectorCreate(p_now, pivot)
                # dot = rs.VectorDotProduct(vector, vec)
                dot = np.dot(vector,vec)
                if arr[j] <= pivot:
                    # 相当于点大于基准点
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1,vec)
        quickSort(arr, pi + 1, high,vec)


paths = [[4,5,3,2,1]]

for path in paths:
    points = path
    vector = 3.5

    quickSort(points, 0, len(points)-1, vector)
    print(points)


try:
    s =1
except Exception:
    pass