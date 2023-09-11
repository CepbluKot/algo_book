from random import randint, choice


initial_arr = [randint(0, 10) for _ in range(7)]
print("initial_arr: ", initial_arr)


def checkIsBaseCase(arr: list):
    return len(arr) <= 1


def baseJob(arr: list):
    if len(arr) == 1:
        return 1


def recursiveJob(arr: list):
    if checkIsBaseCase(arr):
        return baseJob(arr)

    else:
        arr.pop()
        return 1 + recursiveJob(arr)


print("res: ", recursiveJob(initial_arr))
