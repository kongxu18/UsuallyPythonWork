from openpyxl import Workbook
from openpyxl.drawing.image import Image
#
book = Workbook()
sheet = book.active
# sheet.column_dimensions[]
#
# img = Image('1.jpeg')
# sheet['A1'] = 'img'
# cell = sheet.cell(row=1,column=2)
# sheet.add_image(img,(1,2))
# book.save('t.xlsx')

# import string
#
# letter = string.ascii_uppercase
#
#
# def num_to_letter(col, row):
#     col -= 1
#     row -= 1
#     row = str(row + 1)
#     if col < 26:
#         index = col + ord('A')
#         return chr(index) + row
#     else:
#         col_1 = (col // 26) - 1
#         col_2 = (col % 26)
#         return letter[col_1] + letter[col_2] + row
#
#
#
#
# print(num_to_letter(27, 12))
