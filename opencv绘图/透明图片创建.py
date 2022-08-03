import numpy as np
import cv2

img_height, img_width = 500, 500
n_channels = 4
transparent_img = np.zeros((img_height, img_width, n_channels), dtype=np.uint8)
transparent_img[transparent_img == 0] = 255
transparent_img[:, :, 3] = 0

cv2.putText(transparent_img, 'abcdefg', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0, 255), 6)
cv2.line(transparent_img, (100, 100), (100, 500), (0, 255, 0))
# t = cv2.getTextSize('abcdefg', cv2.FONT_HERSHEY_SIMPLEX, 0.7, 1)

# m = cv2.getRotationMatrix2D((100, 100), -45, 1)
# dst = cv2.warpAffine(transparent_img, m, (500, 500))

img2 = np.zeros((img_height, img_width, n_channels), dtype=np.uint8)
# img2[img2 == 0] = 255
# img2[:, :, 3] = 0
cv2.line(img2, (0, 0), (500, 500), (0, 0, 255, 255))

fin = transparent_img + img2
print(transparent_img[0,0],img2[0,0],fin[0,0])

# Save the image for visualization
# cv2.imwrite("transparent_img.png", transparent_img)

cv2.imshow('a', transparent_img)
cv2.imwrite('a.png', transparent_img)
cv2.imshow('b', img2)
cv2.imshow('c', fin)
cv2.imwrite('c.png', fin)
cv2.waitKey(0)

p =cv2.imread('linker_left.png')
print(p)