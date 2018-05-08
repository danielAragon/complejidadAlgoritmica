#include<iostream>
#include<list>
using namespace std;
class Graph
{
public:
	int N;
	bool* visitado;
	list<int>*  adj;
	Graph(int N, int M) {
		adj = new list<int>[N];
		visitado = new bool[N];
		this->N = N;
	}

	void addEdge(int u, int v) {
		adj[u].push_back(v);
		adj[v].push_back(u);
	}
	int DFSUtil(int v, bool visitado[], int &cont) {
		visitado[v] = true;
		cout <<v<<endl;
		list<int>::iterator i;
		for (i = adj[v].begin(); i != adj[v].end(); ++i) {
			if (!visitado[*i]) {
				cont++;
				DFSUtil(*i, visitado, cont);
			}
		}
		return cont;
	}
	int DFS() {
		for (int i = 0; i < N; i++) {
			visitado[i] = false;
		}
		int max = 0;
		int cont = 0;
		for (int i = 0; i < N; i++) {
			if (!visitado[i]) {
				if (DFSUtil(i, visitado, cont) >= max)
					max = cont+1;
				cont = 0;
			cout << endl;
			}
		}
		cout<<"MAX = " << max;
		return max;
	}
};

int main() {
// 	Graph* test = new Graph(11, 12);
// 	test->addEdge(1, 2);
// 	test->addEdge(3, 1);
// 	test->addEdge(3, 4);
// 	test->addEdge(5, 4);
// 	test->addEdge(3, 5);
// 	test->addEdge(4, 6);
// 	test->addEdge(5, 2);
// 	test->addEdge(2, 1);
// 	test->addEdge(7, 1);
// 	test->addEdge(1, 2);
// 	test->addEdge(9, 10);
// 	test->addEdge(8, 9);
// 	cout << test->DFS();


    Graph* test;
    freopen("inEA", "rt", stdin);
    freopen("outEA", "wt", stdout);
    
    int casos;
    scanf("%d\n", &casos);
    
    while(casos-->0){
        int n,m;
        scanf("%d %d\n", &n, &m);
        test = new Graph(n,m);
        while(m-->0){
            int u, v;
            scanf("%d %d\n", &u,&v);
            test->addEdge(u,v);
        }
        test->DFS();
        cout << endl;
    }
    return 0;
}