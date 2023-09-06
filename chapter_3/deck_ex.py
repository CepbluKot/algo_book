class Deck:
    def __init__(self) -> None:
        self.deck_list = []
    
    def add(self, elem):
        self.deck_list.append(elem)
    
    def get(self):
        if self.deck_list:
            return self.deck_list.pop(0)


def printAllDeck(de: Deck):
    got = de.get()

    if got:
        print(got)
        printAllDeck(de)

d = Deck()
d.add(1)
d.add(2)
d.add("bababoe")
d.add(321)
d.add("mr sugoma")
d.add(99)

printAllDeck(d)
