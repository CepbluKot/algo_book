class Deck:
    def __init__(self) -> None:
        self.deck_list = []

    def add(self, elem):
        self.deck_list.append(elem)

    def get(self):
        if self.deck_list:
            return self.deck_list.pop(0)

    def isIn(self, elem):
        return elem in self.deck_list


def printAllDeck(de: Deck):
    got = de.get()

    if got:
        print(got)
        printAllDeck(de)


# init_graph = {}
# init_graph["a"] = ["b", "c", "d"]
# init_graph["b"] = ["a", "c", "e"]
# init_graph["c"] = ["a", "b", "f", "l"]
# init_graph["d"] = ["a"]
# init_graph["e"] = ["b"]
# init_graph["f"] = ["l", "c"]
# init_graph["l"] = ["f", "c"]

init_graph = {0: [1, 6], 1: [0, 7], 2: [3], 3: [2], 4: [5, 9], 5: [4, 6, 10], 6: [5, 7, 0, 11], 7: [6, 8, 1], 8: [7], 9: [10, 4], 10: [9, 11, 5, 14], 11: [10, 6], 12: [13, 16], 13: [12], 14: [10], 15: [], 16: [12]}

# init_point_from = "l"
# init_point_to = "e"

init_point_from = 8
init_point_to = 14

def widthSearch(graph: dict, point_from: str, point_to: str):
    path_history = {}

    to_search = Deck()
    checked = set()

    for x in graph[point_from]:
        to_search.add(x)
        path_history[x] = point_from

    point = to_search.get()

    while not point is None:
        if point == point_to:
            # print(path_history)

            seq = [point_to]
            curr_point = point_to

            while curr_point != point_from:
                curr_point = path_history[curr_point]
                seq.append( curr_point)

            print(seq[::-1])
            return True

        else:
            for x in graph[point]:
                if x != point_from and not to_search.isIn(x) and not x in checked:
                    to_search.add(x)
                    path_history[x] = point

            checked.add(point)
            point = to_search.get()


print(widthSearch(init_graph, init_point_from, init_point_to))
