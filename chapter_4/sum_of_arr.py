from random import randint, choice


initial_arr = [randint(0, 10) for _ in range(5)]
print('initial_arr: ', initial_arr)


def checkIsBaseCase(arr: list):
    return len(arr) <= 2


def baseJob(arr: list):
    if len(arr) == 2:
        return arr[0] + arr[1]
    elif len(arr) == 1:
        return arr[0] 


def recursiveJob(arr: list):
    if checkIsBaseCase(arr):
        return baseJob(arr)
    
    else:
        return arr.pop() + recursiveJob(arr)

print('res: ', recursiveJob(initial_arr))
