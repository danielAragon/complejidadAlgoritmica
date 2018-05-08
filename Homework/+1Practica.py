# def Pregunta1(string):
#     return
    
def Pregunta2(m,n):
    if m == 0:
        return  n+1
    if m > 0 and n == 0:
        return Pregunta2(m-1, 1)
    if m > 0 and n > 0:
        return Pregunta2(m-1,Pregunta2(m,n-1))

print(Pregunta2(1,1))
# def Pregunta3(H=[2,2,0,1],M=[2,1,0,3],N=[[]]):
#     return

# def Pregunta4(M,V[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],inicio=[0,0],llegada=[4,4]):
#     if inicio == llegada:
#         return "Finializado"
#     if se puede:
#         inicio[0]+=1
#         Pregunta4(M,V,inicio,llegada,)
        