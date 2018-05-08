def grafo(b):
    base = ["0","1","x","y","z","8","9"]
    if len(b)==3:
        print (b)
    for i in range(2):
        b+base[i]
        for j in range(1,5):
            b+base[j]
            for k in range(5,7):
                b+base[k]
                print (b)
                grafo(b)
                
grafo("")
    