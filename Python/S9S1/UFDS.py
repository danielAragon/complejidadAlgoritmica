class UFDSRankPathCom(object):
    def __init__(self,n):
        self.length = n
        self.parent=[i for i in range(n)]*n
        self.rank=[0]*n
    
    def findSet(self,x):
        if (x != self.parent[x]):
            self.parent[x] = self.findSet(self.parent[x])
        return self.parent[x]
    
    def sameSet(self,x,y):
        return self.findSet(x) == self.findSet(y)
    
    def __unionSetUtil(self,x,y):
        if (not self.sameSet(x,y)):
            if(self.rank[x] > self.rank[y]):
                self.parent[y] = x
            else:
                self.parent[x] = y
                if (self.rank[x] is self.rank[y]):
                    self.rank[x] += 1
    
    def unionSet(self,x,y):
        self.__unionSetUtil(self.findSet(x),self.findSet(y))
    
    def showSet(self):
        for i in range(self.length):
            print("parent of: " + str(i) + " is " + str(self.parent[i]) + "\n")

test = UFDSRankPathCom(6)
test.showSet()
print("\n")
test.unionSet(1,2)
test.unionSet(2,4)
test.unionSet(0,2)
test.unionSet(3,5)
print("\n")
test.showSet()