"""
Q U E U E S   I N   P Y T H O N
"""
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