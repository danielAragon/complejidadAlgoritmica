class MaxHeap(object):
    def __init__(self,cap):
        self.position = 0
        self.capacity = cap + 1
        self.heap = []

    def insert(self,value):
        self.heap.insert(self.position+1,value)
        child = self.position - 1
        parent = (child-1)//2
        while (self.heap[parent] > self.heap[child] and parent > 0):
            temp = self.heap[parent]
            self.heap[parent] = self.heap[child]
            self.heap[child] = temp
            child = parent 
            parent = child//2

    def show(self):
        print (self.heap)
        
        
a = MaxHeap(7)

a.insert(20)
a.insert(10)
a.insert(12)
a.insert(7)
a.insert(8)
a.insert(6)
a.show()