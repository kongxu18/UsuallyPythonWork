import pandas as pd

da = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]])
print(da.shape)
print(da.iloc[3:5])

import matplotlib.pyplot as plt

r, c = 250, 1200
dpi =300
# fig = plt.figure(figsize=(c/dpi,r/dpi),dpi=dpi)
fig, axes = plt.subplots(figsize=(1200/300, 250/300),dpi=dpi)

axes.plot([1,3,4])
plt.show()
plt.close()


import cv2 as cv


a = cv.imread('linker.png',-1)
b = cv.imread('linker_left.png',-1)
print(a.shape,a[0][0])
print(b.shape,b[0][0],'b')
row , col  = a.shape[:2]
print(row,col)

a = a[:,:int(col/2+3)]

# cv.imshow('a',a)
# cv.imshow('b',b)
# cv.waitKey(0)

# cv.imwrite('linker_left2.png',a)


a = '汉'
print(len(a))

a = 1.345
print(int(a))