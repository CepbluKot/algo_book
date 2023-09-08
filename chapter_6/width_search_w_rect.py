def genRect(wid: int, len: int): # bug - works up to decs = 10, need 2 add hundreds , etc ...
    rect_dict = {}

    decs = 0
    for y in range(len):
        for x in range(wid):
            if x+(y*wid*decs) == 99:
                pass

            if wid > 1 and len > 1:
                if y == 0:
                    if x == 0:
                        rect_dict[str(x+(y*wid*decs))] = [str(x+(y*wid*decs)+1), str(x+(y*wid*decs)+wid)]
                    elif x == wid - 1:
                        rect_dict[str(x+(y*wid*decs))] = [str(x+(y*wid*decs)-1), str(x+(y*wid*decs)+wid)]
                    else:
                        rect_dict[str(x+(y*wid*decs))] = [str(x+(y*wid*decs)-1), str(x+(y*wid*decs)+1), str(x+(y*wid*decs)+wid)]
                        
                elif y == len - 1:
                    if x == 0:
                        rect_dict[str(x+(y*wid*decs))] = [str(x+(y*wid*decs)+1), str(x+(y*wid*decs)-wid)]
                    elif x == wid - 1:
                        rect_dict[str(x+(y*wid*decs))] = [str(x+(y*wid*decs)-1), str(x+(y*wid*decs)-wid)]
                    else:
                        rect_dict[str(x+(y*wid*decs))] = [str(x+(y*wid*decs)-1), str(x+(y*wid*decs)+1), str(x+(y*wid*decs)-wid)]
                
                elif x == 0:
                    rect_dict[str(x+(y*wid*decs))] = [ str(x+(y*wid*decs)+1), str(x+(y*wid*decs)-wid), str(x+(y*wid*decs)+wid)]
                
                elif x == wid - 1:
                    rect_dict[str(x+(y*wid*decs))] = [ str(x+(y*wid*decs)-1), str(x+(y*wid*decs)-wid), str(x+(y*wid*decs)+wid)]
                
                else:
                    rect_dict[str(x+(y*wid*decs))] = [str(x+(y*wid*decs)-1), str(x+(y*wid*decs)+1), str(x+(y*wid*decs)+wid), str(x+(y*wid*decs)-wid)]

            else:
                if wid == 1:
                    if y == 0:
                        rect_dict[str(x+(y*wid*decs))] = [ str(x+(y*wid*decs)+wid)]
                    
                    elif y == len - 1:
                        rect_dict[str(x+(y*wid*decs))] = [ str(x+(y*wid*decs)-wid)]
                    
                    else:
                        rect_dict[str(x+(y*wid*decs))] = [ str(x+(y*wid*decs)-wid), str(x+(y*wid*decs)+wid)]

                elif len == 1:
                    if x == 0:
                        rect_dict[str(x+(y*wid*decs))] = [ str(x+(y*wid*decs)+len)]
                    
                    elif x == wid - 1:
                        rect_dict[str(x+(y*wid*decs))] = [ str(x+(y*wid*decs)-len)]
                    
                    else:
                        rect_dict[str(x+(y*wid*decs))] = [ str(x+(y*wid*decs)-len), str(x+(y*wid*decs)+len)]

        if wid > 1:
            if (x + (y*wid*decs)) % (wid - 1) == 0: 
                decs += 1

        if wid == 1 or len == 1:
            decs = 1
        
    return rect_dict


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

init_graph = genRect(10, 10)

init_point_from = "0"
init_point_to = "99"

print(init_graph)

def widthSearch(graph: dict, point_from: str, point_to: str):
    path_history = {}

    to_search = Deck()
    checked = set()
    
    for x in graph[point_from]:
        to_search.add(x)
        path_history[x] = point_from
    
    point = to_search.get()
    
    while point:
        if point == point_to:
            # print(path_history)
        

            seq = point_to
            curr_point = point_to

            while curr_point != point_from:
                curr_point = path_history[curr_point]
                seq += " " + curr_point

            print(seq.replace(' ', ' <- '))
            # print(' <- '.join(seq))
            return True
        
        else:
            for x in graph[point]:
                if x != point_from and not to_search.isIn(x) and not x in checked:
                    to_search.add(x)
                    path_history[x] = point

            checked.add(point)
            point = to_search.get()

    

print(widthSearch(init_graph, init_point_from, init_point_to))
