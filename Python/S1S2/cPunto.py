class Punto:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def toString(self):
        strval = "p("+str(self.x)
        strval = strval + ", " + str(self.y)
        strval = strval + ")"
        return(strval)
        
p1 = Punto();
print("p1=>"+p1.toString())

p2 = Punto(8,7);
print("p2=>"+p2.toString())