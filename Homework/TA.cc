#include <iostream>
#include <list>
#include <queue>
#include <time.h>
using namespace std;
class Grafo {
private:
	int vertices;
	int aristas;
	int * Origen_Vertice;
	int * Destino_Vertice;
	int * padre;
	int * rango;
public:
	int Cortes_min;
	//list<int>* plista;
public:
	Grafo(int vertices, int aristas) {
		Cortes_min = 0;
		this->aristas = aristas;
		this->vertices = vertices;
		Origen_Vertice = new int[vertices];
		Destino_Vertice = new int[vertices];
		padre = new int[vertices];
		rango = new int[vertices];
		//plista = new list<int>[vertices];
	}
	~Grafo() {}
	void Agrega(int u, int v, int n) {
		Origen_Vertice[n] = u;
		Destino_Vertice[n] = v;
	}
	//int Regresa_Origen(int n) {
	//	return Origen_Vertice[n];
	//}
	//int Regresa_Destino(int n) {
	//	return Destino_Vertice[n];
	//}
	int Busca(int n) {
		if (padre[n] != n)
		{
			padre[n] = Busca(padre[n]);
		}
		return padre[n];
	}
	void Union(int origen, int destino) {
		int x = Busca(origen);
		int y = Busca(destino);
		if (rango[x] < rango[y])
		{
			padre[x] = y;
		}
		else if (rango[x] > rango[y])
		{
			padre[y] = x;
		}
		else
		{
			padre[y] = x;
			rango[x]++;
		}
	}
	int Karger() {
		for (int i = 0; i < vertices; i++)
		{
			padre[i] = i;
			rango[i] = 0;
		}
		int aux_ver = vertices;
		int n_cortes = 0;
		int cont = 0;
		while (aux_ver > 2)
		{
			int i = rand() % aristas;
			int aux_or = Busca(Origen_Vertice[i]);
			int aux_des = Busca(Destino_Vertice[i]);
			if (aux_des == aux_or)
			{
				continue;
			}
			else
			{
				cout << "Cortando la arista en: " << Origen_Vertice[i] << "-" << Destino_Vertice[i] << endl;
				aux_ver--;
				Union(aux_or, aux_des);
			}
			cont++;
		}
		for (int i = 0; i < aristas; i++)
		{
			int aux1 = Busca(Origen_Vertice[i]);
			int aux2 = Busca(Destino_Vertice[i]);
			if (aux1 != aux2)
			{
				n_cortes++;
			}
		}
		//cout << n_cortes << endl;
		cout << "-------------------------" << endl;
		return n_cortes;
	}

};

int main() {
	Grafo prueba(4, 5);
	prueba.Agrega(0, 1, 0);
	prueba.Agrega(0, 2, 1);
	prueba.Agrega(0, 3, 2);
	prueba.Agrega(1, 3, 3);
	prueba.Agrega(2, 3, 4);
	srand(time(NULL));
	int resultado;
	for (int i = 0; i < 100; i++)
	{
		resultado = prueba.Karger();
		if (i == 0)
		{
			prueba.Cortes_min = resultado;
			cout << prueba.Cortes_min<<endl;
		}
		else if (i > 0 && prueba.Cortes_min > resultado)
		{
			prueba.Cortes_min = resultado;
			cout << prueba.Cortes_min<<endl;

		}
	}

	cout << prueba.Cortes_min << endl;
	//system("pause");
	int asds;
	cin >> asds;
	return 0;
}