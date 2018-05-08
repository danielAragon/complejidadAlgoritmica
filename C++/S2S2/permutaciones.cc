#include<iostream>
using namespace std;

void permutations(string str, int i, int n){
    cout<<"i=> "<<i<<" n=> " <<n<<endl;
    cout<<"      >---------------------------------------------------<      "<<endl;
    if(i==n-1){
        cout<<"base=> "<<str<<endl;
        cout<<">---------------------------------------------------------------------<"<<endl;
        return;
    }
    for (int j = i; j < n; j++) {
        cout<<"\tfor(j="<<j<<"):"<<endl;
        cout<<"\t"<<"CAMBIO: "<<endl;
        cout<<"\t\tswap(str["<<i<<"])"<<str[i];
        cout<<";, str["<<j<<"]=>"<<str[j]<<")";
        
        swap(str[i],str[j]);
        //recurse for string [i+1, n-1]
        permutations(str,i+1,n);
        //BACKTRACK MECHANISM: Restore the string to its original state
        swap(str[j],str[i]);
    }
}

// main method
int main(){
    string str="ABC";
    //--
    permutations(str,0,str.length());
    
    return 0;
}