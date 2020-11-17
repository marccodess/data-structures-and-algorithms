"""
L I N K E D    L I S T S
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
- 