import numpy as np
# np.set_printoptions(threshold=np.inf)
#
# t_n = np.ones((3,3,3))
# print(t_n)
#
# ty = np.array([[True,False,False],[True,False,False],[True,False,False]])
#
# t_n[ty] = [3,4,6]
#
# print(t_n)

from decimal import Decimal

a = Decimal(1.55).quantize(0)
print(int(a))