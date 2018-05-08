def imprimir(dist,V):
    print("Distancia mas corta entre pares de Vertices \n")
    for i in range(V):
        for j in range(V):
            if (dist[i][j] == "INF"):
                print("INF")
            else:
                print(dist[i][j])
        print("\n")

def floydWarshell (graph,V):
    dist = []
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if (dist[i][k] + dist[k][i] < dist[i][j]):
                    dist[i][j] = dist[i][k] + dist[k][i]
    imprimir(dist,V)
    
graph = [[0,5,"INF",10],
         ["INF",0,3,"INF"],
         ["INF","INF",0,1],
         ["INF","INF","INF",0]]
floydWarshell(graph,5)