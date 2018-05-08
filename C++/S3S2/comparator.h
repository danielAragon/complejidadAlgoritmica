#ifndef COMPARATOR_H
#define COMPARATOR_H

#include <limits>
#include <cmath>
#include "point.h"
#include "quicksort.h"

class FinderPoints{
public:
    Quicksort* qs = new Quicksort();
    int compareX(const void* a,const void* b){
        Point* p1 = (Point *)a;
        Point* p2 = (Point *)b;
        return (p1->x-p2->x);
    }

    int compareY(const void* a,const void* b){
        Point* p1 = (Point *)a;
        Point* p2 = (Point *)b;
        return (p1->y-p2->y);
    }

    float distance(Point p1, Point p2){
        return sqrt(pow((p1.x-p2.x),2)+pow((p1.y-p2.y),2));
    }

    float min(float x, float y){
        return (x<y)?x:y;
    }
    
    //BF
    
    float closestPairBF(Point P[],int n){
        float min = std::numeric_limits<float>::max();
        int a,b;
        for (int i=0; i<n; ++i)
            for (int j=i+1; j<n; ++j)
                if (distance(P[i],P[j])<min){
                    a=i;b=j;
                    min = distance(P[i],P[j]);
                }
        cout<<"P["<<P[a].x<<", "<<P[a].y<<"] & P["<<P[b].x<<", "<<P[b].y<<"]";
        return min;
    }
    
    //DC
    
    float stripClosest(Point strip[],int size,float d){
        float min = d;
        qs->sort(strip,size,sizeof(Point),compareY);
        for (int i=0; i<size; ++i)
            for (int j=i+1; j=<size&&(strip[j].y-strip[i].y)<min;++j )
                if (distance(strip[i],strip[j]<min))
                    min = distance(strip[i],strip[j]);
        return min;
    }
    
    float closestPairDCUtil(Point[],int n){
        if (n<=3) return closestPairBF(P,n);
        int mid=n/2;
        Point midPoint = P[mid];
        float dl = closestPairDCUtil(P,mid);
        float dr = closestPairDCUtil(P+mid,n-mid);
        float d = min(dl,dr);
        Point strip[n];
        int j = 0;
        
        for (int i=0; i<n; i++)
            if (abs(p[i].x-midPoint.x)<d)
            strip[j]=P[i];j++;
        return min(d,stripClosest(strip,j,d));
    }
    
    float closestPairDC(Point[],int n){
        
    }
};


#endif