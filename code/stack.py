"""
S T A C K S   I N   P Y T H O N
"""
"""
- Using the LIFO approach, therefore the last element inserted into the stack will be removed first.
- In the example below, imagine you are navigating through a website. You find yourself on 'Page2'.
- Then you select the back button which returns you back to 'Page1', this is achieved using the LIFO approach.
"""


from collections import deque

q = deque()
q.appendleft("Homepage")
q.appendleft("Page1")
q.appendleft("Page2")
# Output: deque(['Page2', 'Page1', 'Homepage'])

q.popleft()
# Output: deque(['Page1', 'Homepage'])

"""
I M P L E M E N T   A   S T A C K

- This is great knowledge for coding interviews and understanding data structures.
"""


class Stack:
    def __init__(self):
        self.elements = []
        self.length = 0
        self.first = None

    def __repr__(self):
        s = []
        for e in self.elements:
            s.append(str(e))
        return "[" + ", ".join(s) + "]"

    def add(self, element):
        self.elements.append(element)  # Append new element to the stack
        self.length += 1
        self.first = self.elements[0]
        self.elements = self.elements.reverse()

    def remove(self):
        if not self.first:
            raise Exception("Array is empty.")
        self.length -= 1
        lastElement = self.elements[-1]  # Select the first element in the queue
        self.elements.pop()
        return lastElement


stack = Stack()  # Output: []
stack.add(2)
stack.add(5)
stack.add(12)
stack.add(3)
stack  # Output: [2, 5, 12, 3]
stack.remove()
stack  # Output: [2, 5, 12]