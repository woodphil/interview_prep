class Graph:
    def __init__(self, value):
        self.val = value
        self.neighbours = []

    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def getNeighbours(self):
        return self.neighbours

    def removeNeighbour(self, neighbour):
        if neighbour in self.neighbours:
            return True


class GraphAdjacencyList:
    def __init__(self):
        self.graph = {}

    def addNode(self, node):
        self.graph[node] = []

    def addEdge(self, nodeA, nodeB):
        self.graph[nodeA].append(nodeB)
        self.graph[nodeB].append(nodeA)

    def removeEdge(self, nodeA, nodeB):
        self.graph[nodeA].remove(nodeB)
        self.graph[nodeB].remove(nodeA)



