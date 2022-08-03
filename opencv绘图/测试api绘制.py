from opencvapi.draw import Draw
from opencvapi.settings import Colour
import cv2

# draw.add_line(((0, 0), (720, 720)), Colour.RED, 8)
# draw.add_circle((200, 200), 30, (32, 32, 32), thickness=1)
# draw.add_arrow(((50, 50), (50, 100)), Colour.BLUE, tipLength=0.2)

# draw.add_word('123中文', (100, 500), Colour.BLACK, size=55,china =True)


# cv2.imshow('image', draw.background)
# cv2.waitKey(0)
# print(draw.background)

import json

with open('驳接爪出图数据.json', 'r') as f:
    js = json.loads(f.read())
    # print(js)

width = js['data_arr'][0]['width']
height = js['data_arr'][0]['height']

draw = Draw(width=width, height=height)
for comments in js['data_arr'][0]['draw_arr']:
    _type = comments['type']
    if _type == 'Circle':
        anchor = (comments['x'], comments['y'])
        r = comments['r']
        # print(anchor, r)
        draw.add_circle(anchor, r, Colour.RED, thickness=-1)

    elif _type == 'Line':
        anchor = ((comments['x1'], comments['y1']), (comments['x2'], comments['y2']))
        draw.add_line(anchor, Colour.BLUE)

name = js['data_arr'][0]['name']
# draw.components.add_title(name, 0.8, 1, (50, 50))
draw.add_word('h我是天才', (100, 100), (18, 18, 18), size=12, china=True)
draw.resize(1.5)
cv2.imshow('image', draw.background)
cv2.imwrite('t.png', draw.background)
cv2.waitKey(0)
if __name__ == '__main__':
    ...
