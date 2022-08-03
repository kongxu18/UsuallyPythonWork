def coordinate_converter(anchor: any, canvas):
    """
    坐标点转换
    （0，0）cv2 图片左上角
     数据（0，0）为图片的中心点
    """
    # print(canvas.shape)
    width, height = canvas.shape[1], canvas.shape[0]

    x, y = int(anchor[0]), int(anchor[1])
    x_offset = width // 2
    y_offset = height // 2

    return x + x_offset, -y + y_offset