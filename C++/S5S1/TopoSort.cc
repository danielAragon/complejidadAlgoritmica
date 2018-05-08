#include <iostream>
#include <list>
#include <queue>

using namespace std;

class Graph{
private:
    int n;
    list<int>* listAd;
    int* incoming;
public:
    Graph(int n=10);
    void addEdge(int v, int w);
    bool existsIncommingVertex();
    void topologicalSort();
};

Graph::Graph(int n){
    this->n = n;
    listAd = new list<int>[n];
    
    incoming = new int[n];
    for(int i=0; i<n; i++)
        incoming[i]=-1;
}

void Graph::addEdge(int u, int v){
    listAd[u].push_back(v);
    
    if(incoming[u]<0)
        incoming[u]=0;
        
    if(incoming[v]<0)
        incoming[v]=1;
    else
        incoming[v]++;
}

bool Graph::existsIncommingVertex(){
    for(int i=0; i<n; i++){
        if(incoming[i]==0)
            return(true);
    }
    return(false);
}

void Graph::topologicalSort(){
    queue<int> q;
    
    if(!existsIncommingVertex()) return;
    
    for(int i=0; i<n; i++){
        if(incoming[i]==0)
            q.push(i); 
    }
    
    while(!q.empty()){
        int u = q.front();
        q.pop();
        cout<<u<<" ";
        list<int>::iterator i;
        for(i = listAd[u].begin(); i!=listAd[u].end(); ++i){
            int v = *i;
            incoming[v]--;
            if(incoming[v]==0){
                q.push(v);
            }
        }
    }
    
}

int main(){
    Graph g(6);
    g.addEdge(2,4);
    g.addEdge(2,5);
    g.addEdge(1,3);
    g.addEdge(1,4);
    g.addEdge(0,3);
    g.topologicalSort();
    return 0;
    
    //Graph g(10);
    //g.addEdge(7,0);
    //g.addEdge(7,8);
    //g.addEdge(5,0);
    //g.addEdge(3,8);
    //g.addEdge(3,6);
    //g.addEdge(0,2);
    //g.addEdge(0,9);
    //g.addEdge(0,6);
    //g.addEdge(8,9);
    //g.topologicalSort();
    //return 0;
}