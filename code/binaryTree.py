"""
B I N A R Y   T R E E   I N   P Y T H O N
"""
"""
- Binary tree starts with a root node.
- Nodes are connected by edges.
- Every nodes (except the root) is associated with a parent node.
- Each node can have an arbitary number of child nodes.
"""
"""
I M P L E M E N T   A   B I N A R Y   T R E E
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()  # Print the left side of tree
        print(self.data),  # Print root
        if self.right:
            self.right.PrintTree()  # Print the right side of tree


root = Node(10)  # Set the root of the tree
root.insert(8)
root.insert(16)
root.PrintTree()  # Output: 8 10 16
root.insert(4)
root.insert(26)
root.PrintTree()  # Output: 4 8 10 16 26
root.insert(2)
root.insert(22)
root.insert(2)
root.insert(15)
root.PrintTree()  # Output: 2 4 8 10 15 16 22 26