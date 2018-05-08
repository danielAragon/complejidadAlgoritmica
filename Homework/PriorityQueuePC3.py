def swap(a,b):
    temp = a
    a = b
    b = temp
    
class PriorityQueue(object):
    
    def __init__(self):
        self.position = 0;
        self.heap = []
    # def agregar(self,value):
    #     if(self.position == self.capacidad):
    #         return
    #     self.heap[self.position] = value
    #     self.position+=1
    #     child = self.position -1
    #     parent = child//2
    #     while (self.heap[parent]>self.heap[child] and parent > 0):
    #         swap(self.heap[parent], self.heap[child])
    #         child = parent
    #         parent = child//2
    def agregar(self,value):
        self.heap.insert(self.position+1,value)
        child = self.position - 1
        parent = (child)//2
        while (self.heap[parent] < self.heap[child] and parent > 0):
            swap(self.heap[parent], self.heap[child])
            child = parent 
            parent = child//2
            
    def eliminar(self):
        val = self.heap[1]
        self.heap[1] = self.heap[self.position-1]
        self.position-=1
        i=1
        while(i<=len(self.heap)+1):
            lc = 2*i
            rc = 2*i+1
            if (lc>len(self.heap)+1 and rc>len(self.heap)+1):
                if (self.heap[lc]>self.heap[rc]):
                    cc = lc
                else:
                    cc=rc
                    
                if(self.heap[i]<self.heap[cc]):
                    swap(self.heap[i],self.heap[cc])
                i+=1
        return val

    def show(self):
        
        self.eliminar()
        print (self.heap)
        
a = PriorityQueue()

a.agregar(20)
a.agregar(10)
a.agregar(12)
a.agregar(7)
a.agregar(8)
a.agregar(6)
a.show()