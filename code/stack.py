"""
S T A C K S   I N   P Y T H O N
"""
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