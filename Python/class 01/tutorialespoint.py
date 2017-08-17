def calcularAreaCirculo():
    radio = float(0.0)
    PI = float(3.14159)
    
    print("Radio Circulo? ")
    radio = input()
    
    area = PI * radio * radio
    
    print("Area Circulo =>" + str(area))
    
calcularAreaCirculo()