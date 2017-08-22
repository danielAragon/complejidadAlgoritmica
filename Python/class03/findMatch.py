def findMatch(key, val):
    M = len(key)
    N = len(val)
    
    for i in range(N-M+1):
        for j in range(M):
            if val[i+j] != key[j]:
                break
        if j == M-1: #if key[0,...M-1] = val[i, i+1,... i+M-1]
            print ("keytern found at index" + str(i))
            

val = "AABAACAADAABAAABAA"
key = "AABA"
findMatch(key,val)