"""
G R A P H S   I N   P Y T H O N
"""
"""
- Undirected graph has a series of nodes connected by edges with no direction between nodes.
- Directed graph has a series of nodes with direction, for example, routing of flights between cities.
- Unlike in a tree structure, graphs can have multiple paths between node pairs.
- Weighted graphs have weights attached to it's edges, for example, miles between airports.
"""
"""
I M P L E M E N T   A   G R A P H
"""


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graphDict = {}
        for start, end in self.edges:  # Outbound as key, inbound as value
            if start in self.graphDict:
                self.graphDict[start].append(end)
            else:
                self.graphDict[start] = [end]

    def getPaths(self, start, end, path=[]):
        path = path + [start]  # State where you are starting from
        if start == end:
            return [path]
        if start not in self.graphDict:  # Node does not exist in the graph
            return []
        paths = []
        for node in self.graphDict[
            start
        ]:  # Loop through graph where o is starting node
            if node not in path:
                newPaths = self.getPaths(node, end, path)  #
                for p in newPaths:
                    paths.append(p)
        return paths

    def shortestPath(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graphDict:  # Node does not exist in the graph
            return []
        shortest = None
        for node in self.graphDict[start]:
            if node not in path:
                newpath = self.shortestPath(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


routes = [
    ("JFK", "LAX"),
    ("LHR", "DXB"),
    ("LAX", "HND"),
    ("DXB", "JFK"),
    ("DXB", "DXB"),
    ("HND", "LHR"),
    ("HND", "LAX"),
]
graph = Graph(routes)
graph.shortestPath("JFK", "HND")  # Output: [['JFK', 'LAX', 'HND']]
graph.shortestPath("JFK", "LAX")  # Output: [['JFK', 'LAX']]