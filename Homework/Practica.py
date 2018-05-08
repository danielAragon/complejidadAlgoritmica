#Pregunta 2
def potencia(base,exponente):
    if (exponente == 0): 
        return 1;
    if (exponente == 1): 
        return (base);
    if (exponente == 2): 
        return (base*base);
    temp = potencia(base,exponente//2);
    
    if (exponente%2!=0):
        return(temp*temp*base)
    else:
        return(temp*temp)

#print(potencia(3,4))

#Pregunta 3
#BF
def sumaSecuancial1(a = [10,12,-5,17,38,-6,7,9]):
    maxsuma = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[j] < 0:    #profe el algoritmo que se me ocurrio suma todas las cadenas secuenciales y solo si hay negativos grandes no devuelve la suma de toda la cadena
                i=j+1       #lo que le entendí en para este ejercicio es que simplemente por el hecho de ser negativo es un punto de corte y paso a las siguiente secuencia. en cualquiera de los casos lo unico que cambian son estas dos lineas
            suma = 0
            for k in range(i,j+1):
                suma += a[k]
            if suma > maxsuma:
                maxsuma = suma
    return maxsuma
"""
maxsuma = 0 #=> 1
for i       #=> n
for j       #=> n <- peor de los casos
if a[j]<0   #=> 1
suma=0      #=> 1
for k       #=> n <- peor de los casos
suma +=k    #=> 1
if suma>max #=> 1
O(n)=1+n*(n*(n+3)) = n^3+n = n^3
"""
#print(sumaSecuancial1())

#BT
def sumaSecuancial2(maxsuma=0,a = [10,12,-5,17,38,-6,7,9]):
    
    for i in range(len(a)):
        if a[i] < 0:
            if maxsuma < sum(a[:i]):
                maxsuma = sum(a[:i])
            sumaSecuancial2(maxsuma,a[i:])
    return maxsuma
 
print(sumaSecuancial2())