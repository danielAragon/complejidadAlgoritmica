using namespace std;
class Merge{
    public:
    
    void swap (int* a, int*b){
        int t = *a;
        *a = *b;
        *b = t;
    }
    
    int partition(int arr[], int l, int h){
      
    }
    
    void ""?(int A[], int l, int h){
        if(l<h){
            int p = partition(A,l,h);
            sort(A,l,p-1);
            sort(A,p+1,h);
        }
    }
};
