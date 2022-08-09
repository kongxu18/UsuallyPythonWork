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
        draw.add_circle(anchor, r, Colour.RED, thickness=1, offsetCenter=True)

    elif _type == 'Line':
        anchor = ((comments['x1'], comments['y1']), (comments['x2'], comments['y2']))
        draw.add_line(anchor, Colour.BLUE, offsetCenter=True, thickness=1)

name = js['data_arr'][0]['name']
draw.components.add_title(name, 0.8, 1, (100, 100))

# draw.add_word('hello', (150, 100), (18, 18, 18), size=1, thickness=1)
# draw.add_word('hello2', (0, 0), (18, 18, 18), size=0.8, thickness=1,offsetCenter=True)
# draw.add_word('这个是中文', (100, 100), (0, 0, 255), size=18, china=True)
# draw.add_word('ABCDEFG', (100, 100), (0, 0, 255), size=1, china=False, revolve=0, offsetCenter=True,
#               alignment_type='center', alignment_spacing=25)
# draw.add_word('ABCDEFG', (100, 100), (0, 0, 255), size=1, china=False, revolve=0, offsetCenter=True,
#               alignment_type='left', alignment_spacing=25)
draw.add_word('ABCDEFG', (100, 100), (0, 0, 255), size=1, china=False, offsetCenter=False,
              alignment_type='left', alignment_spacing=25)

draw.add_line(((100, 0), (100, 200)), 1, (255, 255, 0), offsetCenter=False)
draw.add_line(((0, 100), (200, 100)), 1, (255, 255, 0), offsetCenter=False)

draw.add_line(((100, 0), (100, 200)), 1, (255, 255, 28), offsetCenter=True)
draw.add_line(((0, 100), (200, 100)), 1, (255, 255, 28), offsetCenter=True)
draw.resize(1.5)

cv2.imshow('image', draw.background)

cv2.imwrite('api.png', draw.background)
cv2.waitKey(0)
if __name__ == '__main__':
    ...
