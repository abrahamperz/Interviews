class Node:
    def __init__(self, data):
        self.left = None
        self.rigth = None
        self.data - data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if self.data < data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
