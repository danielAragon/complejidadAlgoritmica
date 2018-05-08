#BRUTE FORCE

#ejercicio 1
def searchSpace(N, L, E,password=[]): 
    numeros = "1 2 3 4 5 6 7 8 9".split();
    letras="a b c d e f g h i j k l m n ñ o p q r s t u v w x y z".split()
    especiales = "! @ # $ % ^ & * ( ) _ + { } [ ] ; : ' < > / \ |".split()
    
    if N+E+L == 0:
        print(''.join(password))
        return
      
    if N>0:
        for j in numeros:
            password.append(j)
            searchSpace(N-1,L,E,password)
            password.pop()
    if L>0:
        for k in letras:
            password.append(k)
            searchSpace(N,L-1,E,password)
            password.pop()
    if E>0:
        for l in especiales: 
            password.append(l)
            searchSpace(N,L,E-1,password)
            password.pop()
    return

#ejercicio 2
def encontrarN1(A,n,key):
    for i in range(n):
        if A[i] ==  key:
            return i
    #=> par aun arreglo desordenado, la unica forma de buscar un elemento es linealmente

#ejercicio 3
class Producto(object):
    def __init__(self,producto, tipo):
        self.producto = producto
        self.tipo = tipo

def buscarProducto(Producto,listaPasillos):
    if Producto.tipo in listaPasillos:
        print("Ve al pasillo ",Producto.tipo)

#ejercicio 4

def sePuede(a, filPosible, colPosible): 
    for fila in range(8):
        if(a[fila] and (fila != filPosible or a[fila] != colPosible) ):
            if a[fila] == colPosible:
                return False
            if abs(fila - filPosible) == abs(a[fila]-colPosible):
                return False
    return True

def ochoReinas(a=[-1,-1,-1,-1,-1,-1,-1,-1],fila=0):
    if fila >= len(a):
        for i in range(len(a)):
            string = []
            for j in range(len(a)):
                if j == a[i]:
                    string.append("X")
                else:
                    string.append("0")
            print (string)
        print(">>>")
        return
    else :
        for i in range(len(a)):
            if sePuede(a,fila,i):
                a[fila] = i
                ochoReinas(a,fila+1)
                a[fila] = -1

#ejercicio 5
def potencia1(x,n):
    resultado = x
    for i in range(n):
        resultado = resultado*x
    return resultado

def potencia2(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == 2:
        return x*x
    y = potencia2(x,n//2)
    
    if n % 2 != 0:
        return y*y*x
    else:
        return y*y

#ejercicio 6
def selectionSort(a):
    for i in range(len(a)):
        minimo = i
        for j in range(i+1,len(a)):
            if a[j] < a[minimo]:
                minimo = a[j]
        temp = a[i]
        a[i] = a[minimo]
        a[minimo] = temp

#ejercicio 7
def sumaSecuancial(a):
    maxsuma = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            suma = 0
            for k in range(i,j+1):
                suma += a[k]
            if suma > maxsuma:
                maxsuma = suma
    return maxsuma
    
#ejercicio 8
def insertionSort(a):
    for i in range(len(a)):
        minimo = a[i+1]
        for j in range(i+1,len(a)):
            if a[j] < minimo:
                minimo = a[j]
        for k in range(i+1):
            if minimo >= a[k] and minimo <= a[k+1]:
                a.insert(k+1,minimo)
                a.remove(minimo)
                
                
                
ochoReinas()