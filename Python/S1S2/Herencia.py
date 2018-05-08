class Poligono(object):
    def __init__(self,id):
        self.id=id 
    verices = "dd"
    def toString(self):
        return (str(self.id) + str(self.verices))

class Rectangulo(Poligono):
    def __init__(self,id,width,height):
        super(self.__class__,self).__init__(id)
        self.shape = (width,height)
    def toString(self):
        s = super(self.__class__,self).toString()
        s = s + str(self.shape)
        return(s)
        
def main():
    p = Poligono(10)
    print("Poligono.toString()=>"+p.toString())
    
    r = Rectangulo(1,15,25)
    print("Rectangulo.toString()=>"+r.toString())

main()