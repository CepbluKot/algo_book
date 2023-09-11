from math import ceil, log2
from random import randint, choice


init_arr = [randint(1, 10) for x in range(10)]


def binSearch(arr: list, elem_to_find: int):  # log2(len_of_arr) actions
    arr.sort()

    print("\n begin with: ", arr, elem_to_find)

    begin = 0
    end = len(arr) - 1
    select = ceil(end / 2)

    action_n = 0

    while action_n != ceil(log2(len(arr))):
        print("action_n", action_n, "selected id ", select)

        if arr[select] == elem_to_find:
            return select

        elif arr[select] > elem_to_find:

            end = select

            select = (begin + end) // 2

        elif arr[select] < elem_to_find:

            begin = select

            select = ceil((begin + end) / 2)

        action_n += 1


print("returned: ", binSearch(init_arr, choice(init_arr)))
# print('returned: ', binSearch(init_arr, sorted(init_arr)[9]))
