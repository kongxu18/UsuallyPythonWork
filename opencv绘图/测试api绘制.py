from opencvapi.draw import Draw
from opencvapi.settings import Colour
import cv2

draw = Draw()

draw.add_line(((0, 0), (720, 720)), Colour.RED, 8)
draw.add_circle((200, 200), 30, (32, 32, 32), thickness=1)
draw.add_arrow(((50, 50), (50, 100)), Colour.BLUE, tipLength=0.2)

draw.add_word()
cv2.imshow('image', draw.background)
cv2.waitKey(0)
print(draw.background)

if __name__ == '__main__':
    ...
