#include<iostream>
#include<list>
using namespace std;

class Graph{
private: 
    int n;
    list<int>* listAd;

public:
    Graph(int =10);
    void addEdge(int v, int w);
    void BFS(int v);
};

Graph::Graph(int n){
    this->n = n;
    listAd = new list<int>[n];
} 

void Graph::addEdge(int v, int w){
    listAd[v].push_back(w);
}

void Graph::BFS(int s){
    bool *visited = new bool[n];
    for(int i = 0; i<n ; i++)
        visited[i]=false;
    
    list<int> queue;
    visited[s] = true;
    queue.push_back(s);
    
    list<int>::iterator it;
    
    while(!queue.empty()){
        s = queue.front();
        cout<<s<<" ";
        queue.pop_front();
        
        for(it = listAd[s].begin();it != listAd[s].end();++it){
            if(!visited[*it]){
                visited[*it]=true;
                queue.push_back(*it);
            }
        }
    }
}

int main(){
    Graph g(4);
    g.addEdge(0,1);
    g.addEdge(0,2);
    g.addEdge(1,2);
    g.addEdge(2,0);
    g.addEdge(2,1);
    g.addEdge(2,3);
    g.addEdge(3,3);
    cout<<"DFS trasversal : initial vertex 2"<<endl;
    g.BFS(2);
    return 0;
}