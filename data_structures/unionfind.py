class UnionFind:
    def __init__(self):
        self.parentArray = []
        self.vertices = []

    def addNewVertex(self):
        currentVertexCount = len(self.vertices)
        self.parentArray.append(currentVertexCount)
        self.vertices.append(currentVertexCount)

    def union(self, vertexA, vertexB):
        # check if they are root nodes
        isVertexARoot = self.parentArray[vertexA] == vertexA
        isVertexBRoot = self.parentArray[vertexB] == vertexB

        # both root nodes
        if isVertexARoot and isVertexBRoot:
            # choose one to no longer be root node
            self.parentArray[vertexA] = vertexB
        # unioning a root node to a non-root
        elif isVertexARoot and not isVertexBRoot:
            self.parentArray[vertexA] = vertexB
        elif isVertexBRoot and not isVertexARoot:
            self.parentArray[vertexB] = vertexA
        # unioning two non-roots
        else:
            self.parentArray[vertexA] = vertexB

    def find(self, vertex):
        currentVertex = vertex

        while self.parentArray[currentVertex] != currentVertex:
            currentVertex = self.parentArray[currentVertex]

        return currentVertex

            
class UnionFindQuickFind:
    def __init__(self):
        self.parentArray = []
        self.vertices = []

    def addNewVertex(self):
        currentVertexCount = len(self.vertices)
        self.parentArray.append(currentVertexCount)
        self.vertices.append(currentVertexCount)

    def union(self, vertexA, vertexB):
        rootA = self.find(vertexA)
        rootB = self.find(vertexB)

        # change all previous values of rootA to rootB
        if rootA != rootB:
            for idx in range(len(self.parentArray)):
                if self.parentArray[idx] == rootA:
                    self.parentArray[idx] == rootB
                    
    def find(self, vertex):
        return self.parentArray[vertex]

    def connected(self, vertexA, vertexB):
        return self.find(vertexA) == self.find(vertexB)


class UnionFindQuickUnion:
    def __init__(self):
        self.roots = []

    def addNewVertex(self):
        currentVertexCount = len(self.roots)
        self.roots.append(currentVertexCount)

    def union(self, vertexA, vertexB):
        rootA = self.find(vertexA)
        rootB = self.find(vertexB)

        if rootA != rootB:
            self.roots[rootA] = rootB
                    
    def find(self, vertex):
        currentVertex = vertex

        while self.roots[currentVertex] != vertex:
            currentVertex = self.roots[currentVertex]

        return currentVertex 

    def connected(self, vertexA, vertexB):
        return self.find(vertexA) == self.find(vertexB)


class UnionFindUnionByRank:
    def __init__(self):
        self.roots = []
        self.ranks = []

    def addNewVertex(self):
        currentVertexCount = len(self.roots)
        self.roots.append(currentVertexCount)
        self.ranks.append(1)

    def find(self, vertex):
        currentVertex = vertex

        while self.roots[currentVertex] != vertex:
            currentVertex = self.roots[currentVertex]

        return currentVertex

    def union(self, vertexA, vertexB):
        rootA = self.find(vertexA)
        rootB = self.find(vertexB)

        if rootA != rootB:
            rankA = self.ranks[vertexA]
            rankB = self.ranks[vertexB]

            if rankA < rankB:
                self.roots[rankA] = rankB
            elif rankA > rankB:
                self.roots[rankB] = rankA
            else:
                self.roots[rankA] = rankB
                self.ranks[rankB] += 1

    def connected(self, vertexA, vertexB):
        return self.find(vertexA) == self.find(vertexB)


