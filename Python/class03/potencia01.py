def potencia(x,n):
    resultado = int(x);
    for i in range(1,n):
        resultado = resultado*x
        return(resultado)
        
def test():
    base = int(input("Base? "))
    expo = int(input("Expo? "))
    res = potencia(base,expo)
    
    print ("potencia=> "+ str(res))
    

test()