"""
B I N A R Y   S E A R C H   T R E E   I N   P Y T H O N
"""
"""
- Binary search tree (BST) is a tree which has the following properties:
    - The left sub-tree of a node has a key less than or equal to its parent node's key.
    - The right sub-tree of a node has a key greater than to its parent node's key.
- When searching, we traverse the nodes from left to right and then finally the parent.
"""
"""
I M P L E M E N T   A   B I N A R Y   S E A R C H   T R E E
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

    def findVal(self, searchedVal):
        if searchedVal < self.data:
            if self.left is None:
                return f"{str(searchedVal)} Not Found"
            return self.left.findVal(searchedVal)
        elif searchedVal > self.data:
            if self.right is None:
                return f"{str(searchedVal)} Not Found"
            return self.right.findVal(searchedVal)
        else:
            return f"{str(self.data)} Is Found"

    def printTree(self):
        if self.left:
            self.left.printTree()  # Print the left side of tree
        print(self.data),  # Print root
        if self.right:
            self.right.printTree()  # Print the right side of tree


root = Node(10)  # Set the root of the tree
root.insert(8)
root.insert(16)
root.printTree()  # Output: 8 10 16
root.insert(4)
root.insert(26)
root.printTree()  # Output: 4 8 10 16 26
root.findVal(10)  # Output: 10 Is Found
root.findVal(99)  # Output: 99 Not Found