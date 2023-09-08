def genRect(width: int, length: int):
    rect_dict = {}

    for y in range(width):
        rect_dict[str(y)] = []
        for x in range(length):
            rect_dict[str(y)].append(str(x))

    return rect_dict

