from random import randint, choice


init_arr = [randint(0, 10) for _ in range(10)]


def checkIsBaseCase(arr: list):
    return len(arr) <= 2


def baseCaseJob(arr: list):
    if len(arr) == 2:
        return [min(arr[0], arr[1]), max(arr[0], arr[1])]

    elif len(arr) <= 1:
        return arr


def parseElems(arr: list, elem_id: int):
    smaller = []
    greater = []

    for x in arr[:elem_id] + arr[elem_id + 1 :]:
        if x >= arr[elem_id]:
            greater.append(x)
        else:
            smaller.append(x)

    return smaller, greater


def recursionJob(arr: list):
    if checkIsBaseCase(arr):
        return baseCaseJob(arr)

    else:
        relative_elem_id = len(arr) // 2
        smaller, greater = parseElems(arr, relative_elem_id)

        return recursionJob(smaller) + [arr[relative_elem_id]] + recursionJob(greater)


print(recursionJob(init_arr))
