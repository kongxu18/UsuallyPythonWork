import cv2 as cv
import numpy as np
import pandas as pd


def small(img, per):
    height, width = img.shape[:2]
    reSize = cv.resize(img, (int(width / per), int(height / per)),
                       interpolation=cv.INTER_AREA)
    return reSize


def get_center(img):
    img = np.array(img)
    color = np.array([255, 0, 0])
    r, c, _ = img.shape
    for i in range(r):
        for j in range(c):
            obj = img[i][j]
            if obj[0] > 180 and obj[1] < 200 and obj[2] < 200:
                print(obj)

    color = np.array([255, 0, 0])
    loc = img == color

    return 0


# 画布
canvas = np.zeros((500, 1200, 3), dtype=np.uint8)
canvas[canvas == 0] = 255
# canvas = canvas.astype(np.uint8)

# 两点坐标
point_1 = (40, 250)
point_2 = (1130, 250)

# 绘制两个圆圈
# cv.circle(canvas, point_1, 63, 1, 1)  # 圆，-1为向内填充
# cv.circle(canvas, point_2, 63, 1, 1)  # 圆，-1为向内填充

cv.line(canvas, point_1, point_2, (0), 1)

# 绘制文字

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(canvas, 'Up', (9, 250), font, 0.5, (1), 1, cv.LINE_AA)
cv.putText(canvas, 'Down', (1150, 250), font, 0.5, (1), 1, cv.LINE_AA)

# 读取锁头
lock = cv.imread('lockhead.png')
# 获取中心点

center_arr = get_center(lock)

print(lock)
lock_small = small(lock, 2.8)

row, col = lock_small.shape[:2]

l = 40
r = l + col
t = (500 - row) // 2
b = t + row
canvas[t:b, l:r] = lock_small

# 对锁头进行矩阵翻转
lock_gray_r = np.flip(lock_small, axis=1)

r = 1140
l = r - col
canvas[t:b, l:r] = lock_gray_r

# 读取链条


link = cv.imread('linker.png')
link_small = small(link, 2.8)
row, col = link_small.shape[:2]
l = 300
r = l + col
t = (500 - row) // 2
b = t + row

canvas[t:b, l:r] = link_small

# pd_canvas.iloc[51:448, 366:985] = pd_link

# 为了演示，建窗口显示出来
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.resizeWindow('image', 1200, 500)  # 定义frame的大小
cv.imshow('image', canvas)

cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('picture.jpg', canvas)
import base64


def ndarray2b64(img, format='rgb'):
    if format == 'rgb':
        _, enc = cv.imencode('.jpg', img)
    elif format == 'bgr':
        _, enc = cv.imencode('.jpg', img)
    b64 = base64.urlsafe_b64encode(enc.tobytes())
    return b64


image_b64 = str(ndarray2b64(canvas), encoding='utf-8')



print(image_b64)
