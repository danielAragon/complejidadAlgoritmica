from random import randint
class Karger(object):
    origen_vertice = []
    destino_vertice = []
    padre = []
    rango = []
    
    def __init__(self,v, a):
        self.vertices = v
        self.aristas = a
        self.corte_min = 0
        
    def Agregar(self,u,v,n):
        self.origen_vertice.insert(n,u)
        self.destino_vertice.insert(n,v)
        
    def Busca(self,n):
        if (self.padre[n] != n):
            self.padre[n] = self.Busca(self.padre[n])
        return self.padre[n]
        
    def Union(self, o, d):
        x = self.Busca(o)
        y = self.Busca(d)
        if (self.rango[x]<self.rango[y]):
            self.padre[x] = y
        elif (self.rango[x]>self.rango[y]):
            self.padre[y] = x
        else:
            self.padre[y] = x
            self.rango[x] += 1
    
    def Algorithm(self):
        for j in range(self.vertices):
            self.padre.insert(j,j)
            self.rango.insert(j,0)
            
        aux_vertices = self.vertices
        n_cortes = 0
        cont = 0
        
        while(aux_vertices > 2):
            k = randint(0,self.aristas-1)
            aux_origen = self.Busca(self.origen_vertice[k])
            aux_destino = self.Busca(self.destino_vertice[k])

            if (aux_destino == aux_origen):
                continue
            else:
                print("Cortando la arista en: " + str(self.origen_vertice[k]) +" " + str(self.destino_vertice[k]))
                aux_vertices-=1
                self.Union(aux_origen,aux_destino)
            cont+=1
        for i in range(self.aristas):
            aux1 = self.Busca(self.origen_vertice[i])
            aux2 = self.Busca(self.destino_vertice[i])
            if (aux1 != aux2):
                n_cortes+=1
        print("-------------------------")
        return n_cortes

test = Karger(4,5)
test.Agregar(0, 1, 0)
test.Agregar(0, 2, 1)
test.Agregar(0, 3, 2)
test.Agregar(1, 3, 3)
test.Agregar(2, 3, 4)
for i in range(50):
    resultado = test.Algorithm()
    if i == 0:
        test.corte_min = resultado
    elif i > 0 and test.corte_min > resultado:
        test.corte_min = resultado
print (str(test.corte_min))