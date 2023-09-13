from typing import List
from math import sqrt


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


dista = [3, 4, 4, 1, 4]
distb = [4, 3, 5, 1, 5]
distc = [2, 5, 1, 3, 1]

print(euclid_distance(dista, distb), euclid_distance(dista, distc))
