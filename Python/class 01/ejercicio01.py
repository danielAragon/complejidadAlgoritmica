import math

def main():
    numero = int(161)
    centena = int(0)
    decena = int(0)
    unidad = int(0)
    
    centena = math.trunc(numero/100)
    decena = (numero%100)/10
    unidad = (numero%100)%10
    
    if centena == unidad:
        print("El numero es capicua")
    else:
        print("El numero NO es capicua")
        
        
main()