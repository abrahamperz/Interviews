class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linklist:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("l-list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("Node is not in ll")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("Node is not in ll")
        else:
            new_node = Node(data)
            n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Its empty")
        else:
            self.head == self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Its empty")
        else:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                n = self.head
                while n.ref.ref is not None:
                    n = n.ref
                n.ref = None

    def delete_by_value(self):
        if self.head is None:
            print("Its empty")
        if self.head.data == x:
            self.head = self.head.ref
        n = se;f.head
        while n.ref is not None:
            if x==n.ref.data:
                break
        n = n.ref
        if n.ref is None:
            print("no exists")
        else:
            n.ref-n.ref.ref




ll = Linklist()
ll.add_begin(10)
ll.add_begin(11)
ll.add_end(12)
ll.add_begin(9)
ll.add_after(90,9)
ll.print()
