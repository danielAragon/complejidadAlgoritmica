import random

def main():
    x=[]
    total = 0
    n = 10
    
    for i in range(0,n):
        x.append(random.randint(15,95))
        print(x[i])
        total = total + x[i]
    promedio = float (total/len(x))
    
    print("suma=>" + str(total))
    print("promedio=>" + str(total))
    
main()