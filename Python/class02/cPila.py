class Pila:
    def __init__(self):
        self.items=[]
        
    def push(self,x):
        self.items.append(x)
    
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila esta vacia")
    
    def isEmpty(self):
        return self.items == []