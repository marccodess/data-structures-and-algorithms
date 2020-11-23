"""
Q U E U E S   I N   P Y T H O N
"""
"""
- Using the FIFO approach, three names will be added into a queue.
- Then an element is removed using this approach.
- Think of a queue outside a retail store, the first one to arrive is Marc. When able to enter, Marc leaves the queue first.
"""


from collections import deque

q = deque()
q.append("Marc")
q.append("Steve")
q.append("Sarah")
# Output: deque(['Marc', 'Steve', 'Sarah'])

q.popleft()
# Output: deque(['Steve', 'Sarah'])
"""
I M P L E M E N T   A   Q U E U E

- This is great knowledge for coding interviews and understanding data structures.
"""


class Queue:
    def __init__(self):
        self.elements = []
        self.length = 0
        self.first = None

    def __repr__(self):
        q = []
        for e in self.elements:
            q.append(str(e))
        return "[" + ", ".join(q) + "]"

    def add(self, element):
        self.elements.append(element)  # Append new element to the queue
        self.length += 1
        self.first = self.elements[0]

    def remove(self):
        if not self.first:
            raise Exception("Array is empty.")
        self.length -= 1
        # Select the first element in the queue
        firstElement = self.elements[0]
        # Remove the first element in the queue
        self.elements = self.elements[1:]
        self.first = self.elements[0]
        return firstElement


queue = Queue()  # Output: []
queue.add(2)
queue.add(5)
queue.add(12)
queue.add(3)
queue  # Output: [2, 5, 12, 3]
queue.remove()
queue  # Output: [5, 12, 3]
