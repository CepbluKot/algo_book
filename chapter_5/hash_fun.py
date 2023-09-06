class LLNode:
    def __init__(self, data) -> None:
        self.saved_object = data
        self.next_node = None


class LL:
    def __init__(self) -> None:
        self.begin_node = None
        self.last_node = None

    def add(self, data):
        if not self.begin_node:
            self.begin_node = LLNode(data)
            self.last_node = self.begin_node
        else:
            new_node = LLNode(data)
            self.last_node.next_node = new_node
            self.last_node = new_node

    def read_all(self):
        print('readin node ----')
        selected_node: LLNode = self.begin_node
        

        while selected_node.next_node:
            print(selected_node.saved_object)
            selected_node = selected_node.next_node
        
        print(selected_node.saved_object)
    
    def insert_after(self, id: int, new_node: LLNode):
        curr_id = 0
        curr_node = self.begin_node

        while curr_id != id:
            curr_node = curr_node.next_node
            curr_id += 1
        
        if curr_id == id:
            curr_node_next = curr_node.next_node
            curr_node.next_node = new_node
            
            new_node.next_node = curr_node_next

    def rm_node(self, id: int):
        curr_id = 0
        curr_node = self.begin_node

        while curr_id != id - 1:
            curr_node = curr_node.next_node
            curr_id += 1
        
        if curr_id == id - 1 and curr_node.next_node:
            next_nod: LLNode = curr_node.next_node
            
            if next_nod.next_node:
                next_nod = next_nod.next_node

                curr_node.next_node = next_nod
            
            else: 
                curr_node.next_node = None


from typing import List
from random import randint, choice


def getHash(inp: str, arr: list):
    sum_of_symbols = 0
    for x in inp:
        sum_of_symbols += ord(x)

    return sum_of_symbols % len(arr)

def add(obj, inp: str, arr: List[LL]):
    hash_of_str = getHash(inp, arr)
    
    if not arr[hash_of_str]:
        arr[hash_of_str] = LL()
    
    arr[hash_of_str].add(obj)

def getAllNonNanElems(arr: list):
    nonNans = []
    for x in arr:
        if x:
            nonNans.append(x)
    return nonNans

def add2( inp: str, arr: list):
    hash_of_str = getHash(inp, arr)
    
    if arr[hash_of_str] and arr[hash_of_str] != inp:
        elemsToAdd = getAllNonNanElems(arr)
        elemsToAdd.append(inp)
        
        arr = [None for _ in range(2*len(arr))]

        while elemsToAdd:
            toAdd = elemsToAdd.pop()
            arr = add2(toAdd, arr)
    
    else:
        arr[hash_of_str] = inp
    
    return arr

    
def get(inp: str, arr: list):
    hash_of_str = getHash(inp, arr)
    return arr[hash_of_str]


init_arr = [None for _ in range(5)]


init_arr = add2("embraer", init_arr)
init_arr = add2( "boeing", init_arr)
init_arr = add2("embraerr", init_arr)
print('xyu')
init_arr = add2( "learjet", init_arr)

print(init_arr)
# print(get("embraerr", init_arr).read_all())
