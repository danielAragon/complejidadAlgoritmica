def potencia(x,n):
    if (n == 0): return 1;
    if (n == 1): return (x);
    if (n == 2): return (x*x);
    
    y = potencia(x,int(n/2));
    
    if (n%2!=0):
        return(y*y*x)
    else:
        return(y*y)
        
def test():
    base = int(input("Base? "))
    expo = int(input("Expo? "))
    res = potencia(base,expo)
    
    print ("potencia=> "+ str(res))
    
test()