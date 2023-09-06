class Stack:
    def __init__(self) -> None:
        self.stack_list = []
    
    def add(self, elem):
        self.stack_list.append(elem)
    
    def get(self):
        if self.stack_list:
            return self.stack_list.pop()


def printAllStack(st: Stack):
    got = st.get()

    if got:
        print(got)
        printAllStack(st)

s = Stack()
s.add(1)
s.add(2)
s.add("bababoe")
s.add(321)
s.add("mr sugoma")
s.add(99)

printAllStack(s)
