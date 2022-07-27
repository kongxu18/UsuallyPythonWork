# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
from typing import List, Tuple, Dict
import datetime

# 指定要使用的字体和大小；/Library/Fonts/是macOS字体目录；Linux的字体目录是/usr/share/fonts/
font = ImageFont.truetype('SimSun.ttf', 70)

data = [{'text': ['王保华', '2022-01-18 12:07:42.720', 'F1-下1', '328.3975', '295', '33.40'], 'path': '', 'loc': 'up-right',
         'ifUseOld': False}]

BACKUPPATH = '' \
             ''


# image: 图片  text：要添加的文本 font：字体
def add_text_to_image(path, text, font=font):
    image = Image.open(path)
    rgba_image = image.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    text_size_x, text_size_y = image_draw.textsize(text, font=font)
    # 设置文本文字位置
    print(rgba_image.size, text_size_x, text_size_y)
    text_xy = (rgba_image.size[0] - text_size_x, 0)
    # 设置文本颜色和透明度
    image_draw.multiline_text(text_xy, text, font=font, align='right', spacing=4, fill=(0, 255, 0, 200), stroke_width=5,
                              stroke_fill=(0, 0, 0, 200))

    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    return image_with_text


def backup(path):
    ...


def main(data: List[dict]):
    if data:
        for v_dict in data:
            text = v_dict.get('text')
            if isinstance(text, list):
                if len(text) < 5:
                    raise ValueError('list less then 5')
                name = text[0]
                time = text[1]
                number = str(text[2])
                param = str(text[3])
                recheck = str(text[4])
                offset = str(text[5])
                time = time.strftime("%Y-%m-%d %H:%M")
                text = name + ' ' + time + '\n ' + number + '\n ' + param + '\n ' + recheck + '\n ' + offset
            path = v_dict.get('path')
            loc = v_dict.get('loc')
            if_use_old = v_dict.get('ifUseOld')

            im_after = add_text_to_image(path, text)

            im_after = im_after.convert('RGB')
            im_after.save('im_after.jpg')
            return


if __name__ == '__main__':
    main(data)
