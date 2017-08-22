#include "classBF.cc"

int main(){
    cout<<"FB-Example01: String Match"<<endl;
    char* a= (char*)"UPC, exigete, innova";
    char* b= (char*)"exigete";
    StringMatching* sm = new StringMatching();
    
    int n = 20;
    int m = 7;
    double beginTime = clock();
    sm->findMatch(a,b,n,m);
    double endTime = clock();
    int t = endTime- beginTime;
    
    cout<<"Execution Time=> "<<(double)t/((double)CLOCKS_PER_SEC)<<endl;
    cout<<"string val=> "<<a<<endl;
    cout<<"string key=> "<<b<<endl;
    
    cout<<endl<<endl;
    
    string path[] = {"ab","aaab","abbb","aaabb","caabb","abc"};
    
    for (int i=0;i<6;i++) {
        string cad = (path[i]).c_str();
        char* subcad = &*cad.begin();
        int longitud = cad.size();
        
        cout<<cad<<" "<<longitud;
        cout<<path[i]<<" es=> ";
        cout<<sm->stringScanner(cad,longitud)<<endl;
    }
    
    
    return 0;
}