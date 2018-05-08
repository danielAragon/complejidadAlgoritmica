import UFDS
class Graph(object):
    def __init__(self,n,m):
        self.n = n
        self.lista = []

    def addEdge(self,u,v,w):
        self.lista.append([w,[u,v]])
        
    def kruskal(self):
        mst_wt=0
        self.lista.sort()
        ds = UFDS.UFDSRankPathCom(self.n)
        for it in self.lista:
            u = ds.findSet(it[1][0])
            v = ds.findSet(it[1][1])
            if (u is not v):
                print (str(u) + " - " + str(v) + "\n")
                mst_wt+= it[0]
                ds.unionSet(u,v)
        return mst_wt

def main():
    g = Graph(9,10)
    g.addEdge(0,1,4)
    g.addEdge(0,7,8)
    g.addEdge(1,2,8)
    g.addEdge(1,7,11)
    g.addEdge(2,3,7)
    g.addEdge(2,8,2)
    g.addEdge(2,5,4)
    g.addEdge(3,4,9)
    g.addEdge(3,5,14)
    g.addEdge(4,5,10)
    g.addEdge(5,6,2)
    g.addEdge(6,7,1)
    g.addEdge(6,8,6)
    g.addEdge(7,8,7)
    
    # g.addEdge(3,0,1)
    # g.addEdge(5,1,2)
    # g.addEdge(4,2,3)
    # g.addEdge(2,3,4)
    # g.addEdge(0,4,0)
    # g.addEdge(7,0,5)
    # g.addEdge(8,1,5)
    # g.addEdge(6,2,5)
    # g.addEdge(8,3,5)
    # g.addEdge(5,4,5)
    
    print ("Edges of MST are\n")
    mstWeight = g.kruskal()
    print ("\nWeight of MST is " + str(mstWeight))

main()

    