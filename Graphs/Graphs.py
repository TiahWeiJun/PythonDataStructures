class Vertex:
    def __init__(self, id):
        self.id = id
        self.connectedTo = {} #key is vertex obj, value is cost

    def __repr__(self):
        return str(self.id) + " " + str([x.id for x in self.connectedTo])

    def addNeighbour(self, vertex, cost=None):
        self.connectedTo[vertex] = cost

    def getNeighbours(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id

    #get cost of edge with another vertex
    def getWeight(self, vertex):
        if vertex in self.connectedTo.keys():
            return self.connectedTo[vertex]
        else:
            return None


class Graph:
    def __init__(self):
        self.vertexList = {} #key is id of vertex, value is vertex obj

    def __repr__(self):
        return "{}".format(self.vertexList.values())

    def addVertex(self, id):
        newVertex = Vertex(id)
        self.vertexList[id] = newVertex

    def getVertex(self, id): #returns vertex obj by passing id
        if id in self.vertexList:
            return self.vertexList[id]
        else:
            return None

    def addEdge(self, startid, endid, cost=None):
        if startid not in self.vertexList:
            self.addVertex(startid)
        if endid not in self.vertexList:
            self.addVertex(endid)
        self.vertexList[startid].addNeighbour(self.vertexList[endid], cost)

    def getVertices(self):
        return self.vertexList.values()
        

g = Graph()
g.addVertex("bukit panjang")
g.addVertex("cck")
g.addVertex("yck")
g.addEdge("cck", 'yck', 200)
g.addEdge("yck", 'cck', 300)
g.addEdge("east", 'west', 100)
print(g.vertexList['east'].getWeight(g.vertexList['west']))

    

