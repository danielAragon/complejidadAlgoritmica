#include<iostream>
using namespace std;

class Finder{
    public: 
        int maxValue(int *a, int l, int r){
            cout<<l<<", "<<r;
            if (r-l==1){
                cout<<" condición"<<endl;
                return a[l];
            }
            int m = (l+r)/2;
            int u = maxValue(a,l,m);
            int v = maxValue(a,m,r);
            return u>v?u:v;
        }
};

