# Python program to explain
# cv2.polylines() method

import cv2
import numpy as np

image = cv2.imread('api.png')
# Window name in which image is
# displayed
window_name = 'Image'

# Polygon corner points coordinates
pts = np.array([[25, 160],
                [110, 200], [200, 160],
                [200, 70], [110, 20], [25, 70]],
               np.int32)

pts = pts.reshape((-1, 1, 2))

isClosed = False

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 1

# Using cv2.polylines() method
# Draw a Blue polygon with
# thickness of 1 px
print(pts)
cv2.polylines(image, [pts], isClosed, (0,0,0), thickness)

# Displaying the image


cv2.imshow('image', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
