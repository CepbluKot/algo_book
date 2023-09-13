import typing
from random import randint 
from typing import List
from math import sqrt



class Fruit:
    def __init__(self, name: str, size: int, color: int) -> None:
        self.size = size
        self.color = color
        self.name = name

def euclid_distance(dists1: List[int], dists2: List[int]) -> float:
    try:
        total_distance = 0
        if len(dists1) != len(dists2):
            raise ("error, hist lengths are not equal")

        element_id = 0
        while element_id < len(dists1):
            total_distance += (dists1[element_id] - dists2[element_id]) ** 2
            element_id += 1
        
        return sqrt(total_distance)
    except:
        raise ("error - calc hist distance")


def knn(input: list, num_of_neighbors: int, all_data: List[Fruit]):
    # 1 - sort
    top_k_min: List[Fruit] = [] 
    
    first_elem = all_data[0]
    first_elem_arr = [first_elem.color, first_elem.size]

    min_dist = euclid_distance(first_elem_arr, input)
    min_elem_id = 0

    while len(top_k_min) != num_of_neighbors:
        id = 0
        min_dist = euclid_distance(first_elem_arr, input)
        min_elem_id = 0
        for fruit in all_data:
            selected_fruit_arr = [fruit.color, fruit.size]
            dist = euclid_distance(input, selected_fruit_arr)
            if dist < min_dist:
                min_dist = dist

                min_elem_id = id

            id += 1

        top_k_min.append(all_data[min_elem_id ])
        del all_data[min_elem_id ]
    
    counted = {}
    for elem in top_k_min:
        if elem.name not in counted:
            counted[elem.name] = 0
        
        counted[elem.name] += 1
    
    counted = dict(sorted(counted.items(), key=lambda item: item[1]))
    return counted
    
# size, color
apple = [Fruit("apple", randint(1, 10), randint(1,10)) for _ in range(10)]
grapefruit = [Fruit("grapefruit", randint(30, 40), randint(30, 40)) for _ in range(10)]

elem_to_search  = [randint(1, 40), randint(1, 40)]
print('elem_to_search ', elem_to_search)

total_mass = apple
total_mass.extend(grapefruit)


print(knn(elem_to_search, 7, total_mass))
