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


ex = LL()
ex.add(1)
ex.add(2)
ex.add(3)
ex.add(5)

ex.insert_after(2, LLNode(123321))
ex.rm_node(2)
ex.read_all()
