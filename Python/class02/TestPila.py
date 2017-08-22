from cPila import Pila

def fillPila(p):
    for i in range(1,11):
        p.push(2*i+1)
        
    for i in range(1,11):
        if not p.isEmpty():
            print("Tope:{0}".format(p.pop()))

def main():
    pl=Pila()
    fillPila(pl)
    print(pl.isEmpty())
    
main()
