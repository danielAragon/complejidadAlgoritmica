class BellmanFord(object):
    def __init__(self,n = 5,E,e,d):
        self.NODES = n
        self.EDGES = E
        self.edges = e
        self.d = d
        self.infinity = 999999

    def showVectors(self,vex,num):
        print("\n")
        for i in range(num):
            print(i, vec+i)
    
    def BellmanFord(self,src):
        for i in range(self.nodes):
            d[i] = self.infinity
        d[src] = 0
        for i in range(self.NODES-1):
            for j in range(self.EDGES):
                if (self.d[self.edges[j].u] + edges[j].w < self.d[self.edges[j].v]):
                    self.d[self.edges[j].v] = edges[j].w + self.d[self.edges[j].w]
        for i in range(self.NODES-1):
            for j in range(self.EDGES):
                if (self.d[self.edges[j].u] + edges[j].w < self.d[self.edges[j].v]):
                    print("Graph contains a negative-weight cycle\n")
    