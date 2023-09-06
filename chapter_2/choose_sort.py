from random import randint, choice


initial_list = [randint(0, 10) for _ in range(10)]
print('before ', initial_list)

sorte = []

while initial_list:
    max_elem = initial_list[0]
    max_elem_id = 0

    for id in range(len(initial_list)):
        if initial_list[id] > max_elem:
            max_elem = initial_list[id]
            max_elem_id = id

    sorte.append(initial_list[max_elem_id])
    del initial_list[max_elem_id]

print('after ', sorte)
