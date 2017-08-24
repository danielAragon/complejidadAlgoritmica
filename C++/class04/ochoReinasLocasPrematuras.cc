#include <iostream>
#include <cstring>
using namespace std;

//M x N matrix
#define M 10
#define N 10

bool isSafe(int mat[M][N], int visited[M][N], int x, int y){
    if(mat[x][y]==0||visited[x][y])
        return false;
    return true;
}

bool isValid(int x, int y){
    if(x<M && y<N && x>=0 && y>=0)
        return true;
    return false;
}

void findLongestPath(int mat[M][N],int visited[M][N],
                     int i, int j, int x, int y,
                     int& max_dist, int dist){
    //if destination is found, update max_dist
    if( i == x && j == y ){
        max_dist = max(dist,max_dist);
        return;
    }
    //set (i,j) cell as visited 
    visited[i][j]=1;
    
    //go to right cell
    if( isValid(i+1,j) && isSafe(mat,visited,i+1,j) ){
        findLongestPath(mat,visited,i+1,j,x,y,max_dist,dist+1);
    }
    //go to left cell
    if( isValid(i+1,j) && isSafe(mat,visited,i-1,j) ){
        findLongestPath(mat,visited,i-1,j,x,y,max_dist,dist+1);
    }
    //go to upper cell
    if( isValid(i+1,j) && isSafe(mat,visited,i,j+1) ){
        findLongestPath(mat,visited,i,j+1,x,y,max_dist,dist+1);
    }
    //go to lower cell
    if( isValid(i+1,j) && isSafe(mat,visited,i,j-1) ){
        findLongestPath(mat,visited,i,j-1,x,y,max_dist,dist+1);
    }
    
    //Backtrack = Remove (i,j) from visted matrix
    visited[i][j]=0;
}

int main(){
    int mat[M][N] = {
        { 1, 0, 1, 1, 1, 1, 0, 1, 1, 1},
        { 1, 0, 1, 0, 1, 1, 1, 0, 1, 1},
        { 1, 1, 1, 0, 1, 1, 0, 1, 0, 1},
        { 0, 0, 0, 0, 1, 0, 0, 1, 0, 0},
        { 1, 0, 0, 0, 1, 1, 1, 1, 1, 1},
        { 1, 1, 1, 1, 1, 1, 1, 1, 1, 0},
        { 1, 0, 0, 0, 1, 0, 0, 1, 0, 1},
        { 1, 0, 1, 1, 1, 1, 0, 0, 1, 1},
        { 1, 1, 0, 0, 1, 0, 0, 0, 0, 1},
        { 1, 0, 1, 1, 1, 1, 0, 1, 0, 0}
    };
    int visited[M][N];
    memset (visited, 0, sizeof(visited));
    int max_dist = 0;
    findLongestPath(mat,visited,0,0,5,7,max_dist,0);
    cout<<max_dist;
    return 0;
}