#include<iostream>
#include<time.h>
#define MULTIPLY a*b
using namespace std;

class Sumador {
public:
	void test() {
		long operando1 = 65432;
		long long operando2 = 10000000000;//1y 10 ceros   30 seg
		long long producto = 0;

		for (long long contador = operando2; contador > 0; contador--)
			producto = producto + operando1;

		cout << producto;
	}
};
int main() {
	Sumador* s = new Sumador();
	
	cout << "Dejame trabajar no te desesperes..." << endl;
	clock_t start = clock();
	s->test();
	clock_t end = clock();
	double time = (double)(end - start) / CLOCKS_PER_SEC*1000.0;
	cout << endl << "time=>" << time<<endl;

	system("pause");
}