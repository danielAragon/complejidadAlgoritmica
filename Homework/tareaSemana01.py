#DE LA PPT 

#1. Encontrar el numero mayor en un arreglo de enteros
def maxNum(x):
    maxim = 0 #->1
    for i in x: #-> n
        if i >= maxim:
            maxim = i #-> 1
    return maxim
#O(n) = 1 + n = n 

#2. Ordenar un arreglo de numeros enteros
def bubble(a):
  for i in range(len(a)): #-> n
    for j in range(len(a)-1,i,-1): #-> n
      if (a[j]<a[j-1]):
            x = a[j] #-> 2 
            a[j] = a[j-1] #-> 3
            a[j-1] = x #-> 3
#O(n) = 7n^2 = n^2

#3. Eliminar el elemento en una posicion de un arreglo
def delete(a,i):
    del a[i] #-> 2
#O(n) = 0

#4. Buscar un numero en un arreglo
def find(a,i):
    for j in range(len(a)): #-> n
        if a[j] == i :
            return a[j] #-> 1
    return "no hay"
#O(n) = n 

#5. Calcular el factorial de N
def factorial(num):
    if num == 1:
        return 1  #-> 1
    else:
        return num*factorial(num-1) #-> 1 + (n-1)
#O(n) = max(n,1) 

#6. Determinar si un numero existe en un arreglo de enteros.
def determine(a,i):
    for j in a: #-> n
        if j == i :
            return True #-> 1
        else:
            return False #-> 1
#O(n) = max(n,n) = n

#7. Calcular cuantas veces se repite un numero X en un arreglo de enteros.
def count(a,i):
    counter=0 #-> 1
    for j in a: #-> n
        if j == i :
            counter +=1 #-> 2
    return counter
#O(n) = 1 + 2n = n

#8. Sumar los digitos de un numero entero positivo.
def digitSum(num):
    if num<10:
        return num  #-> 1
    else:
        return num%10 + digitSum(num//10) #-> 2 + n/10
#O(n) = max(1,2 + n/10) = n

#9. Determinar si un numero es primo o no.
def primo(num):
    for i in range(2, num//2): #-> n/2 -1
        if num % i == 0:
            return False #-> 1
    return True
#O(n) = (n/2(1) - 1) 1

#10. Determinar la cantidad de primos que existen en un arreglo de enteros.
def primosCount(a):
    count = 0 #-> 1
    for i in a: #-> n 
        if primo == True:
            count += 1 #-> 2
    return count
#O(n) =  1 + 2n = n

# DEL WORD

#1.	Busca el mayor valor en un arreglo de tamaño n.
def maxVal(n):
    maxim = 0  #-> 1
    for i in n: #-> n
        if i >= maxim:
            maxim = i #-> 1
    return maxim
#O(n) = 1 + n + n

#2.	Calcula el factorial de un entero n utilizando un algoritmo lineal (secuencial).
def factorialLin(num):
    asd = 1 #-> 1
    for i in range(num): #-> n
        asd *= i #-> 2
    return asd 
#O(n) = 1 + 2n = n 

#3.	Calcula la factorial de un entero n, utilizando una función recursiva.
def factorialRec(num):
    if num == 1:
        return 1  #-> 1
    else:
        return num*factorial(num-1) #-> n
#O(n) = max(n,1) = n

#4.	Calcula la serie de Fibonacci.
def fibonacci(n):
    if n<=1:
        return n #-> 1
    return fibonacci(n-1)+fibonacci(n-2)  #-> n-1 + n-2 
#O(n) = n -1 + n - 2 + 1 = n

#5.	Dado un vector A de n números, calcular otro vector B, tal que, a partir de una 
#   secuencia de números A, calculamos otra tal que cada uno de sus elementos es el 
#   promedio de todos los anteriores en A.
def func(b,a,length):
    sum = 0 #-> 1
    for i in range(length): #-> n
        sum += a[i] #-> 3
        b.append(sum/(i+1)) #-> 3
#O(n) = 1 + n(6) = n 

#6.	Calcula la mediana de un conjunto ordenado es un elemento tal que el número de 
#   elementos menores que la mediana difiere en cuando más 1 del número de elementos 
#   que son mayores, suponiendo que no hay empates.  El algoritmo halla la mediana de 
#   tres enteros distintos: a, b y c. 
def medianaFinderDeluxe(a):
    if len(a) % 2 == 0 :
        return ((a[len(a)//2-1]+a[len(a)//2])/2) #-> 9
    else:    
        return (a[len(a)//2]) #-> 3
#O(n) = max(0,3)= 0

#7.	Halla el segundo elemento más grande de un conjunto que contiene n elementos. 
#   Asuma que los datos no están ordenados. 
def maxVal2(n):
    maxim1 = 0 #-> 1
    maxim2 = 0 #-> 1
    for i in n: #-> n
        if i >= maxim1:
            maxim1 = i #-> 1https://ide.c9.io/daragonor/complejidad
    for i in n: #-> n
        if i >= maxim2 and i < maxim1:
            maxim2 = i #-> 1
    return maxim2
#O(n) = 2 + n + n = n

#8.	Halla el más pequeño y el más grande, de un conjunto de n elementos.
def minXmax(n):
    maxim = 0 #-> 1
    for i in n: #-> n
        if i >= maxim:
            maxim1 = i #-> 1
    minim = maxim #-> 1
    for i in n: #-> n
        if i <= minim:
            minim = i #-> 1
    return [maxim, minim]
#O(n) = 1 + n + 1 + n = n 
