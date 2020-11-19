"""
L I N K E D   L I S T S   I N   P Y T H O N
"""
"""
- Linked lists are an ordered collection of objects.
- Linked lists store elements in memory, lists do not.

- Each element of a linked list is called a node consisting of two fields, data and next.
- Data: Contains the value to be stored in the next node.
- Next: Contains a reference to the next node.

- A linked list is a collection of nodes, the first is called the head.
- The end of a linked list point to a None/Null value stating the end of the list.

- Linked lists are used to implement queues/stacks and graphs.
- Queues (H) use a FIFO approach, therefore the first element inserted is the first to be retrieved.
- Stacks (V) use a LIFO approach, therefore the last element is the first to be retrieved.

- Graphs are used to show the relationships between objects or represent types of networks.
- Adjacency Lists: A list of linked lists. Consists of a vertex (key) and linked list of vertices (value).
"""

graph = {
    1: [2, 3, None],
    2: [4, None],
    3: [None],
    4: [5, 6, None],
    5: [6, None],
    6: [None],
}

"""
- Memory usage is similar for lists and linked lists. Performance is best evaluated using time complexity.
"""

x = [1, 3, 5, 7, 3]

x.insert(0, 5)  # Insert 5 at element 0
x.remove(3)  # Remove 3 at the beginning of the list
x.append(9)  # Append 9 to the end of the list
x.pop()  # Pop off the last element in the list (you can also specify an element by position)

"""
- Time complexity will increase when an element is inserted closer to the beginning of a list (dependant on list size).
- Linked list time complexity is always consistant whereever you insert a new element (0(1)).
- Linked lists are prefered with queues due to their FIFO approach, therefore new elements are inserted/removed at the beginning of the list.
- Lists perform better than linked lists when looking up an element. This is because you have to traverse the entire linked list to find the element.
"""

from collections import deque  # Double-ended Queue

linkedList = deque(["a", "b", "c"])

# Remove elements from the right hand-side
linkedList.append("d")
linkedList.pop()

# Remove elements from the left hand-side
linkedList.appendleft("d")
linkedList.popleft()

"""
I M P L E M E N T   A   Q U E U E

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
I M P L E M E N T   A   S T A C K

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
I M P L E M E N T   A   L I N K E D   L I S T

- This is great knowledge for coding interviews and understanding data structures.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Define the two elements of every linked list

    def __repr__(self):
        return self.data  # Provides a helpful representation of the class


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None  # Where the linked list starts
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while (
            node is not None
        ):  # When condition is True, you are at the end of the list
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def addFirst(self, node):
        node.next = self.head  # Set current head as the next reference of new node
        self.head = node  # New head of the list is the inserted node

    def addLast(self, node):
        if not self.head:  # Traverse the list until you reach the end
            self.head = node
            return
        for currentNode in self:  # Set current node as last node in list
            pass
        currentNode.next = node  # Add new node as the next value of current node

    def removeNode(self, targetNode):
        if not self.head:
            raise Exception("linked list is empty.")
        if self.head.data == targetNode:
            self.head = self.head.next
            return

        previousNode = self.head
        for node in self:
            if node.data == targetNode:
                previousNode.next = node.next
                return
            previousNode = node

        raise Exception(f"Node with data {targetNode} not found.")


linkedList = LinkedList()
linkedList  # Output: None

firstNode = Node("a")
linkedList.head = firstNode
linkedList  # Output: a -> None

secondNode = Node("b")
firstNode.next = secondNode
linkedList  # Output: a -> b -> None

linkedList = LinkedList(["a", "b", "c", "d", "e"])
linkedList  # Ouput: a -> b -> c -> d -> e -> None

linkedList = LinkedList()
linkedList.addFirst(Node("a"))
linkedList  # Output: a -> None
linkedList.addFirst(Node("b"))
linkedList  # Output: b -> a -> None

linkedList = LinkedList(["a", "b", "c", "d"])
linkedList.addLast(Node("e"))
linkedList  # Output: a -> b -> c -> d -> e -> None
linkedList.addLast(Node("f"))
linkedList  # Output: a -> b -> c -> d -> e -> f -> None

linkedList = LinkedList()
linkedList.addFirst(Node("a"))
linkedList.addFirst(Node("b"))
linkedList.addFirst(Node("c"))
linkedList  # Output: c -> b -> a -> None
linkedList.removeNode("b")
linkedList  # Output: c -> a -> None
linkedList.removeNode("z")  # Output: "Node with data z not found."