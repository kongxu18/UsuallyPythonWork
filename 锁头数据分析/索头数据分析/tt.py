import numpy as np
a =np.array([1,3,4])
b= np.array([2,5,9])

c = a-b
c = abs(c)
v = (c>2)
print(c)
print(v)
print(v.any())
if v.any():
    print('sda')
np.set_printoptions(suppress = True)
a ="16.2590098550528,-130709.203697782,39695.763235931"
a = a.split(',')
a =np.array(a,dtype=np.float64)
print(a)

a= {'a','b'}
b = {'a','c'}

u  = a.union(b)
print(u)

d = a.symmetric_difference(b)
print(d)