import cv2

word = cv2.imread('a.png', flags=cv2.IMREAD_UNCHANGED)
print(word.shape)
print(word[0, 0],word[0, 1])
cv2.imshow('a', word)

img = cv2.imread('t.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
print(img[0, 0])

dst = cv2.addWeighted(img[:300, :600], 0.5, word, 1, 0)

img[:300, :600] = dst

cv2.imshow('b', img)

cv2.waitKey(0)
