import string

letter = string.ascii_uppercase


def get_letter_coord(col, row):
    col -= 1
    row -= 1
    row = str(row + 1)
    if col < 26:
        index = col + ord('A')
        return chr(index), row
    else:
        col_1 = (col // 26) - 1
        col_2 = (col % 26)
        return letter[col_1] + letter[col_2], row
