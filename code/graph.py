"""
G R A P H S   I N   P Y T H O N
"""
"""
- Undirected graph has a series of nodes connected by edges with no direction between nodes.
- Directed graph has a series of nodes with direction, for example, routing of flights between cities.
- Unlike in a tree structure, graphs can have multiple paths between node pairs.
- Weighted graphs have weights attached to it's edges, for example, miles between airports.
- 
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
        path = path + [start]  # State where you are starting from
        if start == end:
            return [path]
        if start not in self.graphDict:  # Node does not exist in the graph
            return []
        sPath = None
        for node in self.graphDict[start]:
            if node not in path:
                sp = self.shortestPath(node, end, path)
                if sp:  # Ensure 'None' is not provided
                    if sPath is None or len(sp) < len(sPath):
                        sPath = sp

        return sPath


routes = [
    ("JFK", "LHR"),
    ("JFK", "LAX"),
    ("LHR", "DXB"),
    ("DXB", "LAX"),
    ("DXB", "HND"),
    ("LAX", "LGA"),
]
graph = Graph(routes)
graph.shortestPath("JFK", "HND")  # Output: [['JFK', 'LHR', 'DXB', 'HND']]
graph.shortestPath("JFK", "LGA")  # Output: [['JFK', 'LHR', 'DXB', 'HND']]

graph.getPaths("JFK", "LAX")


edges = routes
graphDict = {}
for start, end in edges:  # Outbound as key, inbound as value
    if start in graphDict:
        graphDict[start].append(end)
    else:
        graphDict[start] = [end]

sPath = None
path = [start]
for node in graphDict[start]:
    print(node)
    if node not in path:
        sp = graph.shortestPath(node, end, path)
        if sp:
            print(len(sp))
            if sPath is None or len(sp) < len(sPath):
                sPath = sp