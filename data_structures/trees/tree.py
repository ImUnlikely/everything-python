class Node:
    def __init__(self, data):
        self.data = data


class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def print_root(self):
        print(self.root.data)
