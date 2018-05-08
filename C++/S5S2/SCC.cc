#include <iostream>
#include <list>
#include <stack>
using namespace std;

class Graph{
    
    int n;
    list<int> *adj;
    void FillStackByFinishTime(int v, bool visited[], stack<int> &Stack);
    void DFSUtil(int v, bool visited[]);
    
    
    public:
    Graph(int n);
    void AddEdge(int u, int v);
    Graph getTranspose();
    void PrintSCC();
};

Graph::Graph(int n){
    
    this->n = n;
    adj = new list<int>[n];
    
}

void Graph::DFSUtil(int u, bool visited[]){
    visited[u] = true;
    cout << u << " ";
    list<int>::iterator it;
    for(it = adj[u].begin(); it != adj[u].end(); ++it){
        if( !visited[*it]){
            DFSUtil(*it, visited);
        }
    }
}
Graph Graph::getTranspose(){
    Graph g(n);
    for(int v = 0; v < n; v++){
        list<int>::iterator it;
        for(it = adj[v].begin(); it != adj[v].end(); ++it){
            g.adj[*it].push_back(v);
        }
    }
    return g;
}

void Graph::AddEdge(int u, int v){
    adj[u].push_back(v);
}

void Graph::FillStackByFinishTime(int u, bool visited[], stack<int> &Stack){
    visited[u] = true;
    list<int>::iterator it;
    for(it = adj[u].begin(); it != adj[u].end(); ++it){
        if(!visited[*it]){
            FillStackByFinishTime(*it, visited, Stack);
        }
    }
    Stack.push(u);
}


void Graph::PrintSCC(){
    stack<int> Stack;
    bool *visited = new bool[n];
    
    for(int i = 0; i < n; i++){
        visited[i] = false;
    }
    for(int i = 0; i < n; i++){
        if(visited[i] == false){
            FillStackByFinishTime(i, visited, Stack);
        }
    }
    
    Graph gr = getTranspose();
    
    for(int i = 0; i < n; i++){
        visited[i] = false;
    }
    
    while(Stack.empty() == false){
        int v = Stack.top();
        Stack.pop();
        if(visited[v] == false){
            gr.DFSUtil(v, visited);
            cout << endl;
        }
    }
}

int main(){
    Graph* g;
    freopen("in", "rt", stdin);
    freopen("out", "wt", stdout);
    
    int casos;
    scanf("%d\n", &casos);
    
    while(casos-->0){
        int n,m;
        scanf("%d %d\n", &n, &m);
        g = new Graph(n);
        
        while(m-->0){
            int u, v;
            scanf("%d %d\n", &u,&v);
            g->AddEdge(u,v);
        }
        cout << "Sets: \n";
        g->PrintSCC();
        cout << endl;
    }
    return 0;
}