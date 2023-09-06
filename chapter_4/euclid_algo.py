init_length = 1680
init_width = 640


def checkIsBaseCase(length, width):
    return not length % width or not width % length 


def recursionJob(length, width):
    while not checkIsBaseCase(length, width):
        if length > width:
            length = length % width
            return recursionJob(length, width)

        else:
            width = width % length
            return recursionJob(length, width)

    return min(length, width)

print(recursionJob(init_length, init_width))
