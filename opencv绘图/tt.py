import cv2
import numpy as np

c = np.zeros((500, 500, 3))
c[c == 0] = 255
cv2.circle(c, (100, 100), 50, (0, 0, 0), 1, cv2.LINE_AA)
cv2.imshow('a', c)

cv2.imwrite('h1.png', c)

from opencvapi.draw import Draw

draw = Draw(width=500, height=500)
draw.add_circle((100, 100), 50, (0, 0, 0), thickness=1)
cv2.imshow('d', draw.background)
cv2.waitKey(0)
cv2.imwrite('h2.png', draw.background)
