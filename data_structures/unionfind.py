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

            
