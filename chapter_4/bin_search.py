from math import ceil, log2
from random import randint, choice


init_arr = [randint(1, 10) for x in range(10)]
init_arr.sort()


def isBaseCase(begin: int, end: int):
    return end - begin == 1


def baseCaseJob(arr: list, begin: int, end: int, elem_to_find: int):
    if arr[begin] == elem_to_find:
        return begin

    elif arr[end] == elem_to_find:
        return end


def recursiveCase(arr: list, begin: int, end: int, elem_to_find: int):
    print("\n begin with: ", arr[begin : end + 1], elem_to_find)

    select = (begin + end) // 2

    if arr[select] == elem_to_find:
        return select

    elif isBaseCase(begin, end):
        return baseCaseJob(arr, begin, end, elem_to_find)

    else:
        if arr[select] > elem_to_find:
            end = select
            return recursiveCase(arr, begin, end, elem_to_find)

        elif arr[select] < elem_to_find:
            begin = select
            return recursiveCase(arr, begin, end, elem_to_find)


# print('returned: ', recursiveCase(init_arr, 0, len(init_arr), choice(init_arr)))
print("returned: ", recursiveCase(init_arr, 0, len(init_arr), sorted(init_arr)[0]))
