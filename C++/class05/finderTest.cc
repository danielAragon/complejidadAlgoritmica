#include <iostream>
#include "finder.h"

using namespace std;
int main(){
    int a[]={34,3,47,91,32,0};
    Finder* f = new Finder();
    int n = sizeof(a)/sizeof(int);
    cout<<"n=> "<<n<<" Max value: "<<f->maxValue(a,0,n);
    return(0); 
}